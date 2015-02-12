import urllib3

# step 1 - connect to the bls website
http = urllib3.PoolManager()
req = http.request('GET', 'http://download.bls.gov/pub/time.series/')

# step 2 - create a file
f = open('test.txt', 'wb')
f.write(req.data)
f.close()
req.release_conn()

# test