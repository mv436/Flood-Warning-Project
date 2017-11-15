"Function Fitting"
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime

def run():

    #Building list of stations to fetch data for
    stations=build_station_list()
    update_water_levels(stations)
    N_stations_at_risk = stations_highest_rel_level(stations,5)
    
    #Variables
    dt = 2     # Fetch data over past 2 days
    p = 4 #Polynomial degree
    i = 0 #Counter
    
    for s in N_stations_at_risk:
        i += 1
        dates, levels = fetch_measure_levels(s[0].measure_id,dt=datetime.timedelta(days=dt)) #Compiling dates and water levels
        if not dates:
            print('Insufficient Data')
        else:
            d0, poly = polyfit(dates, levels, p) #Creating polynomial
            #Plotting data, polynomial and typical high/low
            plt.subplot(3,3,i+1)
            plt.plot(dates, levels)
            plt.plot(dates, poly((mpl.dates.date2num(dates)-d0)))
            plt.axhline(y=s[0].typical_range[0], color='y')
            plt.axhline(y=s[0].typical_range[1], color='r')
            plt.xlabel('date')
            plt.ylabel('water level (m)')
            plt.xticks(rotation=45)
            plt.title(s[0].name)
    plt.show()
    

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")

    # Run Task2F
    run()