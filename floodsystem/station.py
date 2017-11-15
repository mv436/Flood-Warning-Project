"This module provides a model for a monitoring station, and tools for manipulating/modifying station data"



class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += " measure id: {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
        
    def typical_range_consistent(self):
        if self.typical_range is None: #Checking if variable is empty
            return False
        elif self.typical_range[0] > self.typical_range[1]: #Checking if typical low is greater than typical high
            return False
        else:
            return True
    
    def relative_water_level(self):
        if self.typical_range_consistent() is False or self.latest_level is None :
            rel_value= None
        elif  type(self.typical_range[0]) is not float or type(self.typical_range[1]) is not float or type(self.latest_level) is not float:
            rel_value= None
        else: 
            rel_value= (self.latest_level-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
        return rel_value
            
def inconsistent_typical_range_stations(stations): #Builds a list of stations which have inconsistent typical ranges
    inconsistent_stations = []
    for s in stations:
        if s.typical_range_consistent() == False: #checks if data is inconsistent and appends them to list if so
            inconsistent_stations.append(s)
    return inconsistent_stations
    
    
            
            
    
        

