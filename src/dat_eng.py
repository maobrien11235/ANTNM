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
    return pd.read_csv(path + file)

