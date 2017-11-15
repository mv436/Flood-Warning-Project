"This module provides funtions to help with the analysis of water levels"
import operator
import numpy as np
import matplotlib as mpl

def polyfit(dates, levels, p):
""" given the water level time history (dates, levels) for a station computes 
    a least-squares fit of polynomial of degree p to water level data."""
    
    x = mpl.dates.date2num(dates) - mpl.dates.date2num(dates[0]) #Converts dates to workable floats and shifting data for analysis
    p_coeff = np.polyfit(x, levels, p) #Finding polynomial variables
    poly = np.poly1d(p_coeff)
    d0 = mpl.dates.date2num(dates[0])
    return d0, poly