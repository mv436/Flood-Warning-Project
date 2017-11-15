"Assess flood risk by level"
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():

    stations=build_station_list()
    update_water_levels(stations)
    deliverables = stations_level_over_threshold(stations,tol=0.8)
    for a in deliverables:
        print(a[0].name)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    # Run Task2B
    run()