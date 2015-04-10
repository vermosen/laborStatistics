import Quandl
import matplotlib.pyplot as plt
#import matplotlib.pylab as pylab
import pandas as pd
from numpy import log

token = "H8VUjcUPEFHK_mFnjXp1"                                          # my Quandl token

# 1 - getting the interest rate data
print('getting interest rate data from quandl...')                      # message

rateData = Quandl.get("FED/SVENY", authtoken=token, returns="pandas")   # fed rates

print('computing 2-10 spread history from %s to %s' %                            
     (rateData.first_valid_index(), rateData.last_valid_index()))       # message

print('done')

# 2 - getting the GDP data
print('getting GDP data from quandl...')                                # message

gdpData = Quandl.get("FRED/GDP", authtoken=token, returns="pandas")     # us GDP
gpdDiff = log(gdpData / gdpData.shift(1))                              # q/q growth rate

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
#plt.show()

