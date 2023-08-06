import numpy as np
import pandas as pd


def create_random_normal_data(nb_rows, nb_numerical_col, mu, sigma, nb_categorical_col):
    np.random.seed(42)
    cat_value = 'a'
    data = {}
    for i in range(nb_numerical_col):
        col_name = 'col_num' + str(i)
        data[col_name] = np.random.normal(mu, sigma, size=nb_rows)
    for j in range(nb_categorical_col):
        col_name = 'col_cat' + str(j)
        data[col_name] = [cat_value] * nb_rows
    df = pd.DataFrame(data)
    return df
