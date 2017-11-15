"Issuing flood warnings for towns"
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_by_distance, towns
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import sorted_by_key
import datetime
from floodsystem.prediction import creating_pd_frame, creating_regressor_line,creating_interval,creating_forest,predicting_future_level

def run():
    """Requirements for Task 2G"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    #Only concerned with stations where relative water level is at 1 or more
    at_risk_stations = stations_level_over_threshold(stations, 1)  
    at_risk_station_list = []
    for a in at_risk_stations:
        at_risk_station_list.append(a[0])
        
    # Builds a list of towns at risk with no duplicates
    town_list = towns(at_risk_station_list)
    print(len(town_list))

    station_risk_evaluation = []
    for t in town_list:
        n = 0 #Counts the number of stations in a town
        risk_score = 0 #Scores town risk
        for s in stations:
            if s.town == t:
                n += 1
                risk_score += 10 #Computes risk score based on relative water level
                if s.relative_water_level() is None: 
                    pass
                elif s.relative_water_level() > 1.33:
                    risk_score += 10
                    if s.relative_water_level() > 1.66:
                        risk_score += 10
                        if s.relative_water_level() > 2:
                            risk_score += 10
            else:
                pass
        risk_score_normalized = risk_score / n #Normalizes risk score to compensate for towns with many stations
        if risk_score_normalized <= 10:
            risk_level = "Low"
        elif risk_score_normalized <= 20:
            risk_level = "Moderate"
        elif risk_score_normalized <= 30:
            risk_level = "High"
        else:
            risk_level = "Severe"
        entry = (t, risk_level, risk_score_normalized)
        station_risk_evaluation.append(entry)
    station_risk_evaluation = sorted_by_key(station_risk_evaluation, 2) #sorts list risk score
    station_risk_evaluation.reverse()
    
    #Prints 5 most at risk stations
    for i in range(5):
        x = str(station_risk_evaluation[i][0])
        y = str(station_risk_evaluation[i][1])
        print('The town '+x+' has a '+y+' risk of flooding.')
        
    dt=1
    for i in range(6):
        for station in stations:
            if station.town == station_risk_evaluation[i][0] and station_risk_evaluation[i][1]== "Severe":
                dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
                if not dates:
                    pass
                else:
                    print(creating_interval(creating_pd_frame(dates,levels),dt,station.name,station.latest_level))
                    
    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    # Run Task2G
    run()