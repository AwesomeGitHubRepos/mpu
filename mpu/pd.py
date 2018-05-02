"""Pandas utility functions."""

# core modules
from datetime import datetime

# 3rd party modules
import pandas as pd


def example_df():
    """Create an example dataframe."""
    country_names = ['Germany',
                     'France',
                     'Indonesia',
                     'Ireland',
                     'Spain',
                     'Vatican']
    population = [82521653, 66991000, 255461700, 4761865, 46549045, None]
    population_time = [datetime(2016, 12, 1),
                       datetime(2017, 1, 1),
                       datetime(2017, 1, 1),
                       None,  # Ireland
                       datetime(2017, 6, 1),  # Spain
                       None,
                       ]
    euro = [True, True, False, True, True, True]
    df = pd.DataFrame({'country': country_names,
                       'population': population,
                       'population_time': population_time,
                       'EUR': euro})
    df = df[['country', 'population', 'population_time', 'EUR']]
    return df