from selenium import webdriver
import sys

keyword = sys.argv[1]

url = 'http://www.google.com'
brower = webdriver.Chrome()
brower.get(url)
keyword_elem = brower.find_element_by_id('lst-ib')
keyword_elem.send_keys(keyword)
keyword_elem.submit()