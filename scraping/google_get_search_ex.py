import urllib.request
import sys
from bs4 import BeautifulSoup
import json
import re

target = r'#####'


url = "https://www.google.co.jp" 
parameter = "/search?q={0}".format(urllib.parse.quote(format(sys.argv[1])))
req_url = url + parameter
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }


page_count = 10
if len(sys.argv) > 2:
  page_count = int(sys.argv[2])

repattern = re.compile(target)
for i in range(page_count) :
  request = urllib.request.Request(req_url, headers=headers)
  response = urllib.request.urlopen(request)
  s = BeautifulSoup(response, 'lxml')
  #require lxml
  #pip install lxml
  h3 = s.select(".r")
  url_list = []

  rank = 1
  for result in h3:
    get_url = result.a.get("href")
    if repattern.match(get_url):
      rank_url = {str(i) + str(rank): get_url}
      url_list.append(rank_url)
    rank = rank + 1
  if len(url_list) < 1:
    t = s.select("table .pn")
    for pn in t:
      q = pn.get("href")
      req_url = url + q
  else:
    json_str = json.dumps(url_list)
    print (json_str)
    
    break