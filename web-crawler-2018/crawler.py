# Building simple Web Crawler 
# Using python 3 version
# find link from web page
from urllib.request import urlopen

# download full page from url
def page(url):
    return urlopen(url).read()

# find url 
def get_url_and_index(string): 
    start_index = string.find('<a href=')
    if start_index == -1:
        return None, 0  # no links 
    start_quote_index = string.find('"', start_index)
    end_quote_index = string.find('"', start_quote_index + 1)
    url = string[start_quote_index + 1:end_quote_index]
    return url, end_quote_index


# print all links from the page
def all_urls(page):
    while get_url_and_index != None:
        url, end_index = get_url_and_index(page)
        count = 1
        if url:
            print (count,'.Url: ', url)
            page = page[end_index]
            count = count + 1
        else:
            print ('All Links are Print!!!')
            break




test =
'<head><a href="https://enki.com/bootstrap.e6c03554.js"/><a href="https://enki.com/templates/src/views/Home.d0ad70e7.js"/><a href="https://enki.com/main.179bbdbe.js"/><a href="https://enki.com/styles.5ad2ab75.css"/><a href="https://enki.com/styles.5ad2ab75.css"/><meta charSet="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>'

print(all_urls(test))
