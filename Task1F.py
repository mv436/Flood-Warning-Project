"Typical low/high range consistency"
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""

    # Build list of inconsistent stations
    stations = build_station_list() 
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    
    inconsistent_stations_names = []     # Creates new list to store inconsistent station's names
    for i in range(len(inconsistent_stations)): # Extracts names and appends to list
        inconsistent_stations_names.append(inconsistent_stations[i].name)
    inconsistent_stations_names.sort() # Sorts list
    print(inconsistent_stations_names) # Prints Test list

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")

    # Run Task1F
    run()