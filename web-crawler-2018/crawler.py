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

url, end_index = get_url_and_index('<li class="mobile-link"><a href="https://enki.com/about/">About</a></li>')


# print all links from the page
def all_urls(page):
    while get_url_and_index != None:
        url, end_index = get_url_and_index(page)
        if url:
            print ('Url: ', url)
            page = page[end_index]
        else:
            print ('All Links are Print!!!')
            break


print ('All Links: ')
# print(page('https://enki.com'))

print(all_urls(page('https://enki.com')))
