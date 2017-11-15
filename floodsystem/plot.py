"This module plots the time and water level for a specific water station"
import matplotlib.pyplot as plt




def plot_water_levels(station, dates, levels, i): #plolt water levels against the date for a station
    plt.subplot(3,3,i+1)
    plt.plot(dates, levels)
    plt.axhline(y=station.typical_range[0], color='y')
    plt.axhline(y=station.typical_range[1], color='r')
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    
    plt.tight_layout()
    

