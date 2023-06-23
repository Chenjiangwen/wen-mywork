import math
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.compat import jobconf_from_env

class proj1(MRJob):

    SORT_VALUES = True

    JOBCONF = {
        'mapreduce.job.output.key.comparator.class': 'org.apache.hadoop.mapred.lib.KeyFieldBasedComparator',
        'stream.num.map.output.key.fields': '2',
        'stream.map.output.field.separator': '\t',
        'mapreduce.partition.keycomparator.options': '-k1,1 -k2,2nr',
    }

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_calculate_tf),
            MRStep(mapper=self.mapper_calculate_idf,
                   reducer=self.reducer_calculate_weights),
            MRStep(reducer=self.reducer_filter_and_sort)
        ]

    def mapper(self, _, line):
        date, terms = line.strip().split(',')
        year = date[:4]
        for term in terms.split():
            yield (term, year), 1

    def reducer_calculate_tf(self, key, values):
        tf = sum(values)
        term, year = key
        yield term, (year, tf)

    def mapper_calculate_idf(self, term, year_tf):
        year, tf = year_tf
        yield term, (year, tf, 1)

    def reducer_calculate_weights(self, term, year_tf_count):
        n_years = int(jobconf_from_env('myjob.settings.years'))
        year_tf_count_list = list(year_tf_count)

        # calculate IDF
        idf = math.log10(n_years / len(year_tf_count_list))

        # calculate weights and yield
        for year, tf, count in year_tf_count_list:
            weight = tf * idf
            yield (term, year), weight

    def reducer_filter_and_sort(self, term_year, weights):
        beta = float(jobconf_from_env('myjob.settings.beta'))
        weight = sum(weights)
        if weight > beta:
            yield term_year, weight

if __name__ == '__main__':
    proj1.run()
