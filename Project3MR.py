from urllib.request import urlretrieve
import os.path


url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
filename = 'localcopy.log'
totcount = 0
sixmoncount = 0

if not os.path.isfile(filename):
  filename, headers = urlretrieve(url, filename)

AmazonLog = open(filename)

for line in AmazonLog:
  if "1995" in line or "1994" in line:
    totcount = totcount + 1

AmazonLog.close()

AmazonLog = open(filename)

for line in AmazonLog:
  if "Oct" in line and "1995" in line:
    sixmoncount = sixmoncount + 1
    continue
  elif "Sep" in line and "1995" in line:
    sixmoncount = sixmoncount + 1
    continue
  elif "Aug" in line and "1995" in line:
    sixmoncount = sixmoncount + 1
    continue
  elif "Jul" in line and "1995" in line:
    sixmoncount = sixmoncount + 1
    continue
  elif "Jun" in line and "1995" in line:
    sixmoncount = sixmoncount + 1
    continue
  elif "May" in line and "1995" in line:
    sixmoncount = sixmoncount + 1
    continue
  
AmazonLog.close()
  

print("The total # of requests in the log: ",totcount)
print("The # of requests in the past 6 months: ",sixmoncount)
