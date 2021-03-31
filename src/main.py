#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:36:20 2021

@author: matthewobrien
@title: main.py
@purpose: File for main modeling and execution of the surivival
analysis.
"""
# todo: research why my relative imports were failing.
from ANTNM_Survival_Analysis.src.dat_eng import (
    import_data
    )
import confuse

test = import_data("/Users/matthewobrien/Documents/Learning/ANTNM_Survival_analysis/",
            "Manual_data.csv")
test.info()

import re

test['Height']


test['Height'].str.split(r'm')