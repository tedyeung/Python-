# Building simple Web Crawler 
# Using python 3 version

# extrating link from web page
page = '<a href="http://www.mimicom24.com"></a>'

def find_url(string): 
    start_link = string.find('<a href=')
    start_quote = string.find('"', start_link)
    end_quote = string.find('"', start_quote + 1)
    url = string[start_quote + 1:end_quote]
    return url, end_quote

print(find_url(page))

