# making web crawler using BeautifulSoup

import requests
from bs4 import BeautifulSoup

load_page = requests.get('http://mimicom24.com/')
type(load_page)
