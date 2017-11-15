"Rivers with a station(s)"
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river
def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    
    test_case_1=rivers_with_stations(stations)
    print(len(test_case_1))
    for i in range (10):
        print(test_case_1[i])
    
    test_case_2=stations_by_river(stations)
    print(test_case_2["Thames"])

    
    


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
