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
    import_data,
    extract_height
    )
import re
import confuse

test = import_data("/Users/matthewobrien/Documents/Learning/ANTNM_Survival_analysis/",
            "Manual_data.csv")
test.info()

import re


# proposed regex ([0-9.]*)\W?(?:m)

test_extract_height()