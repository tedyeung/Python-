# Building simple Web Crawler 
# Using python 3 version

# find link from web page
page = '<li class="mobile-link"><a href="https://enki.com/about/">About</a></li>'

def get_url_and_index(string): 
    start_index = string.find('<a href=')
    if start_index == -1:
        return None, 0  # no links 
    start_quote_index = string.find('"', start_index)
    end_quote_index = string.find('"', start_quote_index + 1)
    url = string[start_quote_index + 1:end_quote_index]
    return url, end_quote_index

url, end_index = get_url_and_index('<li class="mobile-link"><a href="https://enki.com/about/">About</a></li>')

if url:
    print ('Here: ', url)
    print ('End Index: ', end_index)
else:
    print ('Nothing Here')

print(get_url(page))

