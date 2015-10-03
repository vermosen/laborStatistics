import Quandl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import pandas as pd
import numpy as np
from datetime import datetime as t
from getDataFromQuandl import getDataFromQuandl 

token = "H8VUjcUPEFHK_mFnjXp1"                                          # my Quandl token

# 1 - getting the interest rate data
print('getting time series from Quandl...')                             # message

rate = getDataFromQuandl("FED/SVENY",type="pandas")                     # fed rates
gdp  = getDataFromQuandl("FRED/GDP", type="pandas")                     # US GDP q/q

print('formatting data...')
df = pd.concat([gdp.diff(1), rate], axis=1)                             # concatenate data

print(df.tail(5))

print gdp[t(2015, 4, 1)]

gpdDiff = np.log(gdpData / gdpData.shift(1))                            # q/q growth rate

print('done')

# graph 1
plt.subplot(3,1,1)
plt.plot(rateData.index, (rateData['SVENY10'] - rateData['SVENY02'])* 10000)
plt.title('US rate')
plt.ylabel('2-10 spread (bps)')
plt.xlabel('time')

# graph 2
plt.subplot(3,1,2) 
plt.plot(gdpData.index, gdpData)
plt.ylabel('nominal GDP')
plt.xlabel('time')

# graph 3
plt.subplot(3,1,3) 
plt.plot(gpdDiff.index, gpdDiff)
plt.ylabel('nominal GDP (change %)')
plt.xlabel('time')

# create a data set 
tt = pd.concat((rateData, gdpData), copy=False)

filename = 'toto.txt'
tt.to_csv(filename, encoding='utf-8')


# display the graphs
plt.show()

