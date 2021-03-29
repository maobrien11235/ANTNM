#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:40:03 2021

@author: matthewobrien
@purpose: This file will contain the import and cleaning functions
 to use on the input data. 
"""
import pandas as pd
from pandas import DataFrame

def import_data(path: str, file: str) -> DataFrame:
    """
    Parameters
    ----------
    path : str
        File path to project location of source data.
    file : str
        Name of csv file to be imported.

    Returns
    -------
    DataFrame
        Pandas DataFrame containing the project data.

    """
    return pd.read_csv(path + file)

