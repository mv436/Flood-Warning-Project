"Stations within radius"
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Making station-distance list around Cambridge
    stations_around_cam = stations_within_radius(stations, (52.2053, 0.1218), 10)
    cam_station_names = [] #Creating a list of names
    for i in range(len(stations_around_cam)): 
        cam_station_names.append(stations_around_cam[i].name)
    cam_station_names.sort() #Sorting list of names
    print(cam_station_names)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")

    # Run Task1C
    run()