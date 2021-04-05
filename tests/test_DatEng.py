# File to include test_() functions for any of the 
# data engineering pipeline functions.

import pytest



def test_extract_height(df, col):
    # Take str of height and return str of height in meters
    assert height_convert(df.col)[0] == "1.78 m"
    assert height_convert(df.col) == "1.78 m"

def test_convert_height():
    # take str of height in meters and return heigh in 
    # cm as a integer
    assert convert_height("1.78 m") == 178
    assert convert_height("1.70 m") == 170
    
def test_clean_age():
    # age has some entries with brackets.
    # this will test to ensure the ages are
    # correctly converted into ints
    assert clean_age("22") == 22
    assert clean_age("23[4]") == 23
    
