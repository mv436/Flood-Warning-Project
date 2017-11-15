"Sort stations by distance"
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Making station-distance list around Cambridge
    test_case = stations_by_distance(stations, (52.2053, 0.1218))
    x = [0]*len(test_case) #Creating a new list to store distances, names and towns of stations around Cambridge
    for i in range(len(test_case)):
        x[i] = (test_case[i][0].name, test_case[i][0].town, test_case[i][1])
    print("First Ten Entries")
    print(x[:10])
    print("Last Ten Entries")
    print(x[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")

    # Run Task1B
    run()