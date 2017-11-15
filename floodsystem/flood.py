"This module contains the main functions to asses the flood situation of stations"
from .utils import sorted_by_key
import operator

def stations_level_over_threshold(stations, tol): #Returns list of tuples of stations where water level is over tol and water level
    stations_over_tol= []
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level()> tol:
            rel_value = station.relative_water_level()
            entry = (station, rel_value)
            stations_over_tol.append(entry)
    stations_over_tol = sorted_by_key(stations_over_tol, 1) #sorts list by rel water level
    return stations_over_tol
    
def stations_highest_rel_level(stations, N): #Return list of top N stations where water level is highest relative to normal
    stations_at_risk = []
    for s in stations:
        if s.relative_water_level() is not None:
            rel_value = s.relative_water_level()
            entry = (s, rel_value)
            stations_at_risk.append(entry) #Creates list of tuples where first entry is station and second entry is rel water level
    stations_at_risk = sorted_by_key(stations_at_risk, 1) #sorts list by rel water level
    stations_at_risk.reverse()
    stations_at_risk = stations_at_risk[0:N] #Pick out top N stations
    return stations_at_risk