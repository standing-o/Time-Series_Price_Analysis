import numpy as np
from datetime import datetime

def time_transform(df):
    date = datetime.strptime(df,'%b %d, %Y')
    return date.strftime("%Y-%m-%d")

def make_input(dataset, time_step=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-time_step-1):
        a = dataset[i:(i+time_step), 0]
        dataX.append(a)
        dataY.append(dataset[i + time_step, 0])
    return np.array(dataX), np.array(dataY)
