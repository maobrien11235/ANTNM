#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:36:20 2021

@author: matthewobrien
@title: main.py
@purpose: File for main modeling and execution of the surivival
analysis.
"""
import ANTNM_Survival_Analysis as antnm
dir(antnm.src.dat_eng.import_data)

# Project Imports
from antnm.src.dat_eng import (
    import_data
    )


test = import_data("/Users/matthewobrien/Documents/Learning/ANTNM_Survival_analysis/",
            "Manual_data.csv")
test.info()

