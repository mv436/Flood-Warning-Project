"This module contains a collection of functions related to geographical data."

from .utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from .haversine import haversine
import operator

def rivers_with_stations(stations):
    rivers_set=set(station.river for station in stations) #creating a set with all the rivers that are on stations
    rivers=[a for a in rivers_set] #transforming into a list
    rivers.sort()
    return rivers


def stations_by_distance(stations, p): #Creates a list of tuples(station, distance) from a given coordinate p
    distance_list = []
    for s in stations:
        distance = haversine(s.coord, p) #Haversine is a function for finding distances between two coordinates
        entry = (s, distance)
        distance_list.append(entry)
    distance_list_sorted = sorted_by_key(distance_list, 1)
    return(distance_list_sorted)
    
def stations_within_radius(stations, centre, r): #Returns a list of all stations within a radius r of centre
    station_list  = []
    for s in stations:
        distance = haversine(s.coord, centre) #finds distance between centre and station
        if distance < r:
            station_list.append(s) #adds station to list if close enough
    return station_list

def stations_by_river(stations): #Creates a dictionary relating stations to their rivers
    river_station={} 
    for station in stations: 
        if station.river in river_station: 
            river_station[station.river].append(station.name)
        else:                                      
            river_station[station.river]=[station.name]
    for station in river_station: 
        river_station[station].sort() 
    return river_station
    
def towns(stations): #Creates a dictionary relating stations to their rivers
    towns = []
    for station in stations:
        if station.town in towns or station.town is None: # if the  river is in the new dic than add the station name to the list
            pass
        else:                                       # if not than create add that river to the dic with the corresponding river
            towns.append(station.town)
    towns.sort()
    return towns

def rivers_by_station_number(stations,N): #prints the river and the number of stations on that river in descending order
    river_station = stations_by_river(stations)
    river=[rivers for rivers in river_station]
    number=[len(river_station[rivers]) for rivers in river_station]
    river_number=list(zip(river,number))
    river_number.sort(key=operator.itemgetter(1), reverse=True)
    for i in range (N):
        print (river_number[i])
    