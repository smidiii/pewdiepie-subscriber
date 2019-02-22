from urllib.request import urlopen
import json
import time

key = "/*get the api key by google*/"

datapewds = urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+"pewdiepie"+"&key="+key).read()
subspewds = int(json.loads(datapewds.decode('utf-8'))["items"][0]["statistics"]["subscriberCount"])

datatseries = urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+"tseries"+"&key="+key).read()
substseries = int(json.loads(datatseries.decode('utf-8'))["items"][0]["statistics"]["subscriberCount"])

diff = subspewds-substseries

#print("Pewdiepie: " + "{:,d}".format(subspewds))
#print("T-Series: " + "{:,d}".format(substseries))
#print("Difference: " + "{:,d}".format(diff))

f = open('pewdiepie_vs_tseries.csv', 'a+')
date = time.strftime("%d.%m.%Y")
time = time.strftime("%H:%M:%S")
f.write(date + ';' +  time  + ';' + str(subspewds) + ';'  + str(substseries) + ';' + str(diff) + ';' + '\n')
f.close
