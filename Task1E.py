"Rivers by number of stations"
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    
    test_case_1=rivers_by_station_number(stations,N=10)
    print(test_case_1)
    
    
    


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
