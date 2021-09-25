from urllib.request import urlretrieve

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
filename = 'localcopy.log'

filename, headers = urlretrieve(url, filename)

AmazonLog = open(filename)

#Tokenize String

#Count Data

#Output Counts
