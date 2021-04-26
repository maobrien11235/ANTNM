# File to include test_() functions for any of the 
# data engineering pipeline functions.

import pytest
import pandas as pd
from src.dat_eng import (
    import_data,
    extract_height
    )

# should functions operate within pandas 
def test_extract_height():
    # Create dataframe of tests.
    test1 = pd.DataFrame("5 ft 9 in (1.75 m)")
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
    
