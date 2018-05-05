from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

keyword = sys.argv[1]

url = 'http://www.google.com'
brower = webdriver.Chrome()
brower.get(url)
keyword_elem = brower.find_element_by_id('lst-ib')
keyword_elem.send_keys(keyword)
keyword_elem.submit()