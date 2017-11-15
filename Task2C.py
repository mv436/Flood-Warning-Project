"Most at risk stations"
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():

    stations=build_station_list() 
    update_water_levels(stations)
    N_stations_at_risk = stations_highest_rel_level(stations,10) #create a list of N stations at risk
    for a in N_stations_at_risk:
        print(a[0].name+' '+str(a[1])) #print name and station level

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    # Run Task2C
    run()