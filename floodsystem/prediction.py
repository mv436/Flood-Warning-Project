"this module uses a regression module to predict future values of water level"

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import datetime


#transforming the data into a panda frame
def creating_pd_frame(dates,levels):
    dates_float= matplotlib.dates.date2num(dates)
    flood=pd.DataFrame(list(zip(dates_float,levels)) , columns=["Date","Level"])
    return flood


#creating a regressor line    
def creating_regressor_line(flood,dt,station_name):
    regressor= DecisionTreeRegressor()
    regressor.fit(np.array([flood["Date"]]).T, flood["Level"])
    
    now=datetime.datetime.utcnow()
    end= now-datetime.timedelta(days=dt)
    start= now+datetime.timedelta(days=1)
    index=pd.date_range(end,start, freq='15T')
    index_float=matplotlib.dates.date2num(index.to_pydatetime())
    xx=index_float.T
    predictions=[]
    for i in range(len(xx)):
        predictions.append(regressor.predict(xx[i]))
    plt.title(station_name)
    plt.plot(flood['Date'], flood['Level'], 'o', label='observation')
    plt.plot(xx, predictions, linewidth=4, alpha=.7, label='prediction')
    plt.xlabel('Dates')
    plt.ylabel('Level')
    plt.legend()
    plt.show()

#creating a forest    
def creating_forest(flood,dt,station_name):
    now=datetime.datetime.utcnow()
    end= now-datetime.timedelta(days=dt)
    start= now+datetime.timedelta(days=1)
    index=pd.date_range(end,start, freq='15T')
    index_float=matplotlib.dates.date2num(index.to_pydatetime())
    xx=index_float.T
    forest = RandomForestRegressor(max_depth=3, n_estimators=100)
    forest.fit(np.array([flood['Date']]).T, flood['Level'])
    predictions=[]
    for i in range(len(xx)):
        predictions.append(forest.predict(xx[i]))
    #plt.subplot(3,3,i+1)
    plt.title(station_name)
    plt.plot(flood['Date'], flood['Level'], 'o', label='observation')
    plt.plot(xx, predictions, linewidth=4, alpha=.7, label='prediction')
    plt.xlabel('Dates')
    plt.ylabel('Level')
    plt.legend()
    plt.show()


#creating a prediction interval
def predict_interval(x, ensamble, z=1.96):
    predictions=[estimator.predict(x) for estimator in ensamble.estimators_]
    mean=np.mean(predictions)
    std = np.std(predictions)
    return mean - z*std, mean, mean + z*std

#creating an interval where the predictions are accurate to a certain percent
def creating_interval(flood,dt,station_name,latest_level):
    now=datetime.datetime.utcnow()
    end= now-datetime.timedelta(days=dt)
    start= now+datetime.timedelta(days=1)
    index=pd.date_range(end,start, freq='15T')
    index_float=matplotlib.dates.date2num(index.to_pydatetime())
    xx=index_float.T
    forest = RandomForestRegressor(max_depth=3, n_estimators=100)
    forest.fit(np.array([flood['Date']]).T, flood['Level'])
    predictions=[]
    for i in range(len(xx)):
        predictions.append(forest.predict(xx[i]))
    low, mean, high = [],[],[]
    for i in range(len(xx)):
        low.append(predict_interval(xx[i],forest)[0])
        mean.append(predict_interval(xx[i],forest)[1])
        high.append(predict_interval(xx[i],forest)[2])
    plt.title(station_name)
    if forest.predict(matplotlib.dates.date2num(now))<latest_level:
        plt.fill_between(xx.T,mean,high, facecolor='blue', alpha=0.5, label='Prediction interval')
    else:
        plt.fill_between(xx.T, low, mean, facecolor='blue', alpha=0.5, label='Prediction interval')
        
    plt.plot(flood['Date'], flood['Level'], 'o', label='observation')
    plt.plot(xx.T, mean, linewidth=4, alpha=.7, label='prediction')
    plt.xlabel('Dates')
    plt.ylabel('Level')
    plt.legend()
    plt.show()

    
#prediction of future data
def predicting_future_level(flood):
    regressor= DecisionTreeRegressor()
    regressor.fit(np.array([flood["Date"]]).T, flood["Level"])
    now=datetime.datetime.utcnow()
    start= now+datetime.timedelta(hours=2)
    index=pd.date_range(now,start, freq='H')
    index_float=matplotlib.dates.date2num(index.to_pydatetime())
    xx=index_float.T
    predictions=[]
    for i in range(len(xx)):
        predictions.append(regressor.predict(xx[i]))
    return predictions