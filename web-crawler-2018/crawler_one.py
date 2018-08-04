# making web crawler using BeautifulSoup

import requests
from bs4 import BeautifulSoup as bs

load_page = requests.get('http://mimicom24.com/')
content_page = load_page.content
parse_content = bs(content_page, 'html.parser')

# see the html code
# print(parse_content.prettify())

all_divs = parse_content.find_all('h1')
all_a_tagas = parse_content.find_all('a')

for a in all_a_tagas:
    print(a.text)
