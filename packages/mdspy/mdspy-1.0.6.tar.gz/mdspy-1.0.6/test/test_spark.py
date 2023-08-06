# -*- coding: utf-8 -*-

import unittest

from mdspy.data_creation import create_random_normal_data
from mdspy.spark import run_spark_job_concat_dfs


class Spark_test(unittest.TestCase):
    """Basic test cases."""

    def test_spark_concat_dfs(self):
        # df = pd.read_csv('../data/energydata_complete.csv')
        df = create_random_normal_data(10, 2, 3, 4, 5)
        parameters = [df.head(10), df.tail(10)]

        def funct(df):
            return df.head(5)

        df_res = run_spark_job_concat_dfs(parameters, funct, nb_cores='*')
        expected = 10
        actual = len(df_res)
        self.assertEqual(expected, actual)
