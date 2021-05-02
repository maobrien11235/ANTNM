# File to include test_() functions for any of the 
# data engineering pipeline functions.

import pytest
import pandas as pd
from src.dat_eng import (
    import_data,
    extract_height
    )
pd.DataFrame(data="5 ft 9 in (1.75 m)", columns="test_col")
# should functions operate within pandas 
def test_extract_height():
    # Create dataframe of tests.
    test_height = pd.DataFrame({"test_col": "5 ft 9 in (1.75 m)"})
    test2 = "1.78 m (5 ft 10 in)"
    # Take str of height and return str of height in meters
    assert extract_height(test1) == "1.75"
    assert extract_height(test2) == "1.78"

# def test_convert_height():
#     # take str of height in meters and return heigh in
#     # cm as a integer
#     assert convert_height("1.78 m") == 178
#     assert convert_height("1.70 m") == 170
#
# def test_clean_age():
#     # age has some entries with brackets.
#     # this will test to ensure the ages are
#     # correctly converted into ints
#     assert clean_age("22") == 22

#     assert clean_age("23[4]") == 23

"""
We will build an experimentation system to evaluate different personalized product recommendation algorithms. To that end, we will run A/B tests with live data ingestion and querying.

1. Implement a function that randomly decides on which recommendation algorithm to use based on the desired population percentages (e.g. 50-50).

function returns string of one of the recommendation algos
    return algo
    which algo to use

