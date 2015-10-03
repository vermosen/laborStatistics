import Quandl as qdl
import sys
import time
from datetime import datetime as t
import os.path
import pandas as pd

token = "H8VUjcUPEFHK_mFnjXp1"                                          # my Quandl token
path  = "/tmp/data/"
ndays = 30                                                              # the delay after which the data has to be refreshed

def getDataFromQuandl(idx, type):
    
    update = False
    filename = path + idx + ".csv"                                      # create the full path nqme
    
    if os.path.isfile(filename):                                        # we need to decide if the data should be updated

        if (t.fromtimestamp(os.path.getmtime(filename) + ndays * 24 * 60 * 60) < t.fromtimestamp(time.time())):
            update = True
            
        
    else:        
        
        if not os.path.exists(os.path.dirname(filename)):               # otherwise create the directory
            
            update = True
            os.makedirs(os.path.dirname(filename))
        
    if update:                                                          # if the file hqs to be updated
        
        df = qdl.get(idx, authtoken=token, returns=type)
        df.to_csv(filename)
    
    df = pd.read_csv(filename)                                          # and finally return the dataframe
    df = df.rename(columns=lambda x: x.upper())                         # uppercase
    df.index = pd.to_datetime(df['DATE'])                               # format the index
    
    return df.drop('DATE', 1)
