import urllib.request
import sys
from bs4 import BeautifulSoup
import json

url = "https://www.google.co.jp/search?q={0}".format(sys.argv[1])
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
s = BeautifulSoup(response, 'lxml')
#require lxml
#pip install lxml
h3 = s.select(".r")
url_list = []
for result in h3:
  url_list.append(result.a.get("href"))

json_str = json.dumps(url_list)
print (json_str)
