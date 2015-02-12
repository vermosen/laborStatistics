import Quandl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

# test 
token = "H8VUjcUPEFHK_mFnjXp1"                      # Quandl token

mydata = Quandl.get("FED/SVENY", authtoken=token)   # fed rates

plt.plot(mydata['SVENY10'] - mydata['SVENY02'])
plt.ylabel('2-10 year spread from the fed zero-coupon curve')
plt.show()

print("job done !")

