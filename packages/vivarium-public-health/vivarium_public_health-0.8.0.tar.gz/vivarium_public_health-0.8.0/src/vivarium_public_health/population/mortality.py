import pandas as pd

from vivarium.framework.utilities import rate_to_probability
from vivarium.framework.values import list_combiner

from .data_transformations import get_cause_deleted_mortality


class Mortality:

    def setup(self, builder):
        self._all_cause_mortality_data = builder.data.load("cause.all_causes.cause_specific_mortality")
        self._cause_deleted_mortality_data = None

        self._root_location = builder.configuration.input_data.location
        self._build_lookup_handle = builder.lookup.build_table

        self.csmr = builder.value.register_value_producer('csmr_data', source=list, preferred_combiner=list_combiner)
        self.mortality_rate = builder.value.register_rate_producer('mortality_rate', source=self.mortality_rate_source)

        life_expectancy_data = builder.data.load("population.theoretical_minimum_risk_life_expectancy")
        self.life_expectancy = builder.lookup.build_table(life_expectancy_data, key_columns=[], parameter_columns=('age',))

        self.death_emitter = builder.event.get_emitter('deaths')
        self.random = builder.randomness.get_stream('mortality_handler')
        self.clock = builder.time.clock()
        builder.value.register_value_modifier('metrics', modifier=self.metrics)
        builder.value.register_value_modifier('epidemiological_point_measures', modifier=self.deaths)
        builder.value.register_value_modifier('epidemiological_span_measures',
                                              modifier=self.calculate_mortality_measure)

        self.population_view = builder.population.get_view(
            ['cause_of_death', 'alive', 'exit_time', 'age', 'sex', 'location', 'years_of_life_lost'])
        builder.population.initializes_simulants(self.load_population_columns,
                                                 creates_columns=['cause_of_death', 'years_of_life_lost'])
        builder.event.register_listener('time_step', self.mortality_handler, priority=0)

    def mortality_rate_source(self, index):
        if self._cause_deleted_mortality_data is None:
            csmr_data = self.csmr()
            cause_deleted_mr = get_cause_deleted_mortality(self._all_cause_mortality_data, csmr_data)
            self._cause_deleted_mortality_data = self._build_lookup_handle(
                cause_deleted_mr)

        return self._cause_deleted_mortality_data(index)

    def load_population_columns(self, pop_data):
        self.population_view.update(pd.DataFrame({'cause_of_death': 'not_dead',
                                                  'years_of_life_lost': 0.}, index=pop_data.index))

    def mortality_handler(self, event):
        pop = self.population_view.get(event.index, query="alive =='alive'")
        prob_df = rate_to_probability(pd.DataFrame(self.mortality_rate(pop.index)))
        prob_df['no_death'] = 1-prob_df.sum(axis=1)
        prob_df['cause_of_death'] = self.random.choice(prob_df.index, prob_df.columns, prob_df)
        dead_pop = prob_df.query('cause_of_death != "no_death"').copy()

        if not dead_pop.empty:
            dead_pop['alive'] = pd.Series('dead', index=dead_pop.index)

            dead_pop['exit_time'] = event.time

            dead_pop['years_of_life_lost'] = self.life_expectancy(dead_pop.index)

            self.death_emitter(event.split(dead_pop.index))

            self.population_view.update(dead_pop[['alive', 'exit_time', 'cause_of_death', 'years_of_life_lost']])

    def metrics(self, index, metrics):
        population = self.population_view.get(index)
        the_living = population[population.alive == 'alive']
        the_dead = population[population.alive == 'dead']
        metrics['years_of_life_lost'] = self.life_expectancy(the_dead.index).sum()
        metrics['total_population__living'] = len(the_living)
        metrics['total_population__dead'] = len(the_dead)

        for (condition, count) in pd.value_counts(the_dead.cause_of_death).to_dict().items():
            # TODO: consider changing name to 'death_by_{condition}' or somesuch
            metrics['{}'.format(condition)] = count

        return metrics

    def calculate_mortality_measure(self, index, age_groups, sexes, all_locations, duration, cube):
        pop = self.population_view.get(index)
        duration_s = duration.total_seconds()
        years_per_second = 1/pd.Timedelta(days=365).total_seconds()

        if all_locations:
            locations = set(pop.location) | {-1}
        else:
            locations = {-1}

        now = self.clock()
        window_start = now - duration

        causes_of_death = set(pop.cause_of_death.unique()) - {'not_dead'}
        for low, high in age_groups:
            for sex in sexes:
                for location in locations:
                    sub_pop = pop.query('age >= @low and age < @high and sex == @sex '
                                        'and (alive == "alive" or exit_time > @window_start)')
                    if location >= 0:
                        sub_pop = sub_pop.query('location == @location')

                    if not sub_pop.empty:

                        birthday = sub_pop.exit_time.fillna(now) - pd.to_timedelta(sub_pop.age, 'Y')

                        time_before_birth = (birthday - window_start).dt.total_seconds().copy()
                        time_before_birth[time_before_birth < 0] = 0
                        total_time_before_birth = time_before_birth.sum()

                        time_after_death = (now - sub_pop.exit_time.dropna()).dt.total_seconds().copy()
                        time_after_death[time_after_death < 0] = 0
                        time_after_death[time_after_death > duration_s] = duration_s
                        total_time_after_death = time_after_death.sum()

                        time_in_sim = (duration_s * len(sub_pop)
                                                          - (total_time_before_birth + total_time_after_death))
                        time_in_sim *= years_per_second
                        for cause in causes_of_death:
                            deaths_in_period = (sub_pop.cause_of_death == cause).sum()

                            cube = cube.append(
                                pd.DataFrame(
                                    {'measure': 'mortality', 'age_low': low, 'age_high': high, 'sex': sex,
                                     'location': location if location >= 0 else self._root_location, 'cause': cause,
                                     'value': deaths_in_period/time_in_sim, 'sample_size': len(sub_pop)},
                                    index=[0]
                                ).set_index(['measure', 'age_low', 'age_high', 'sex', 'location', 'cause'])
                            )

                        deaths_in_period = len(sub_pop.query('alive == "dead"'))

                        cube = cube.append(
                            pd.DataFrame(
                                {'measure': 'mortality', 'age_low': low, 'age_high': high, 'sex': sex,
                                 'location': location if location >= 0 else self._root_location, 'cause': 'all',
                                 'value': deaths_in_period/time_in_sim, 'sample_size': len(sub_pop)},
                                index=[0]
                            ).set_index(['measure', 'age_low', 'age_high', 'sex', 'location', 'cause'])
                        )
        return cube

    def deaths(self, index, age_groups, sexes, all_locations, duration, cube):
        pop = self.population_view.get(index, query="alive == 'dead'")

        if all_locations:
            locations = set(pop.location) | {-1}
        else:
            locations = {-1}

        now = self.clock()
        window_start = now - duration

        for low, high in age_groups:
            for sex in sexes:
                for location in locations:
                    sub_pop = pop.query('age > @low and age <= @high and sex == @sex')
                    sample_size = len(sub_pop)
                    sub_pop = sub_pop.query('exit_time > @window_start and exit_time <= @now')
                    if location >= 0:
                        sub_pop = sub_pop.query('location == @location')

                    cube = cube.append(
                        pd.DataFrame(
                            {'measure': 'deaths', 'age_low': low, 'age_high': high, 'sex': sex,
                             'location': location if location >= 0 else self._root_location, 'cause': 'all',
                             'value': len(sub_pop), 'sample_size': sample_size},
                            index=[0]
                        ).set_index(['measure', 'age_low', 'age_high', 'sex', 'location', 'cause'])
                    )

        return cube
