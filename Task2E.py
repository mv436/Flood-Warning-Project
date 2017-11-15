"Plot water level"
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt
def run():

     # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    dt=10
    names=[name for name,level in stations_level_over_threshold(stations,0.8)]
    print(names)
    for i in range(6):
        for station in stations:
            if station.name == names[i]:
                dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
                    
                print(plot_water_levels(station,dates,levels,i))
            
    plt.show()
    
    
    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    # Run Task2E
    run()
