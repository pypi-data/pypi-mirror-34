import pandas as pd

from vivarium_public_health.util import make_cols_demographically_specific, make_age_bin_age_group_max_dict


class CalculateIncidence:
    def __init__(self, disease_col, disease, disease_states):
        """
        disease_col: str
            name of the column name that contains the disease state of interest
        disease: str
            name of the disease of interest
        disease_states: list
            list of states that denote a simulant as having the disease (e.g.
            ['severe_diarrhea', 'moderate_diarrhea', 'mild_diarrhea']).
            If a simulant does not have the disease of interest, we say that they are in the susceptible state
        """
        self.disease_col = disease_col
        self.disease = disease
        self.disease_time_col = disease + "_event_time"
        self.disease_states = disease_states
        self.collecting = False
        self.incidence_rate_df = pd.DataFrame({})

    def setup(self, builder):
        self.susceptible_person_time_cols = make_cols_demographically_specific("susceptible_person_time",
                                                                               age_group_id_min=2,
                                                                               age_group_id_max=21,
                                                                               builder=builder)
        self.event_count_cols = make_cols_demographically_specific("{}_event_count".format(self.disease),
                                                                   age_group_id_min=2,
                                                                   age_group_id_max=21,
                                                                   builder=builder)
        self.age_bin_age_group_max_dict = make_age_bin_age_group_max_dict(age_group_id_min=2,
                                                                          age_group_id_max=21,
                                                                          builder=builder)
        builder.value.register_value_modifier('epidemiological_span_measures',
                                              modifier=self.calculate_incidence_measure)

        self.root_location = builder.configuration.input_data.location
        self.clock = builder.time.clock()
        columns = [self.disease_col, self.disease_time_col, "exit_time", "age", "sex", "alive"]
        self.population_view = builder.population.get_view(columns)
        builder.population.initializes_simulants(self.update_incidence_rate_df)

        builder.event.register_listener('begin_epidemiological_measure_collection', self.set_flag)
        builder.event.register_listener('collect_metrics', self.get_counts_and_susceptible_person_time)

    def update_incidence_rate_df(self, pop_data):

        if self.collecting:
            new_df = pd.DataFrame({})
            for col in self.susceptible_person_time_cols + self.event_count_cols:
                new_df[col] = pd.Series(0, index=pop_data.index)

            self.incidence_rate_df = self.incidence_rate_df.append(new_df)

    def set_flag(self, event):
        """
        Set the collecting flag to True
        """
        self.collecting = True
        for col in self.susceptible_person_time_cols:
            self.incidence_rate_df[col] = pd.Series(0, index=event.index)
        for col in self.event_count_cols:
            self.incidence_rate_df[col] = pd.Series(0, index=event.index)

    def get_counts_and_susceptible_person_time(self, event):
        """
        Gather all of the data we need for the incidence rate calculations (event counts and susceptible person time)
        """
        if self.collecting:
            susceptible_time = event.step_size.days / 365

            population = self.population_view.get(event.index)
            pop = population[(population['alive'] == 'alive') | (population['exit_time'] == event.time)]

            sick = pop[self.disease_col].isin(self.disease_states)
            got_sick_this_time_step = pop[self.disease_time_col] == event.time

            for sex in ["Male", "Female"]:
                last_age_group_max = 0
                for age_bin, upr_bound in self.age_bin_age_group_max_dict:
                    appropriate_age_and_sex = ((pop['age'] < upr_bound)
                                               & (pop['age'] >= last_age_group_max)
                                               & (pop['sex'] == sex))

                    event_count_column = '{}_event_count_{}_among_{}s'.format(self.disease, age_bin, sex)
                    susceptible_time_column = 'susceptible_person_time_{}_among_{}s'.format(age_bin, sex)

                    cases_index = pop[appropriate_age_and_sex & sick & got_sick_this_time_step].index
                    susceptible_index = pop[~sick & appropriate_age_and_sex].index

                    self.incidence_rate_df[event_count_column].loc[cases_index] += 1
                    self.incidence_rate_df.loc[susceptible_index, susceptible_time_column] += susceptible_time

                    last_age_group_max = upr_bound

    def calculate_incidence_measure(self, index, age_groups, sexes, all_locations, duration, cube):
        """
        Calculate the incidence rate measure and prepare the data for graphing
        """
        pop = self.population_view.get(index)

        if all_locations:
            locations = set(pop.location) | {-1}
        else:
            locations = {-1}

        for sex in sexes:
            for location in locations:
                location_index = pop.query('location == @location').index if location >= 0 else pd.Index([])
                location_index = pop.index if location_index.empty else location_index
                incidence_rates = self.incidence_rate_df.loc[location_index]

                last_age_group_max = 0
                for age_bin, upr_bound in self.age_bin_age_group_max_dict:

                    event_count_column = '{}_event_count_{}_among_{}s'.format(self.disease, age_bin, sex)
                    succeptible_time_column = 'susceptible_person_time_{}_among_{}s'.format(age_bin, sex)

                    susceptible_person_time = incidence_rates[succeptible_time_column].sum()
                    num_cases = incidence_rates[event_count_column].sum()

                    if susceptible_person_time != 0:
                        cube = cube.append(pd.DataFrame({'measure': 'incidence',
                                                         'age_low': last_age_group_max,
                                                         'age_high': upr_bound,
                                                         'sex': sex,
                                                         'location': location if location >= 0 else self.root_location,
                                                         'cause': self.disease,
                                                         'value': num_cases/susceptible_person_time,
                                                         'sample_size': susceptible_person_time}, index=[0]).set_index(
                            ['measure', 'age_low', 'age_high', 'sex', 'location', 'cause']))
                    last_age_group_max = upr_bound

        self.collecting = False

        for col in self.susceptible_person_time_cols + self.event_count_cols:
            self.incidence_rate_df[col] = 0

        return cube
