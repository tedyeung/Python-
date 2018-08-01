# Building simple Web Crawler 
# Using python 3 version

# extrating link from web page
page = '<a href="http://www.mimicom24.com"></a>'

def find_url(page): 
    start_link = page.find('<a href=')
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url

print(find_url(page))

