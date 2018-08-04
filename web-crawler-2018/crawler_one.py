# making web crawler using BeautifulSoup

import requests
from bs4 import BeautifulSoup as bs4

load_page = requests.get('http://mimicom24.com/')
content_page = load_page.content
parse_content = bs4(content_page, 'html.parser')

# see the html code
# print(parse_content.prettify())

all_divs = parse_content.find_all('h1')

print(all_divs)
