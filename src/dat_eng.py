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
    Function to import data into project.
    TODO: may delete as a 20-line function to call an existing may be a bit
    too much...
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

def extract_height(df: DataFrame, col: str) -> DataFrame:
    """
    Function extracts the meter height of contestants.

    Parameters
    ----------
    df : DataFrame
        Input ANTM data. Currently Manual_data.csv.
    col : str
        Column containing heights.

    Returns
    -------
    DataFrame
        Returns DataFrame of the ANTM data with height extracted to include
        just the metric value of height.

    """
    