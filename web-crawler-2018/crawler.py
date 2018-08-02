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
    count = 0
    while get_url_and_index != None:
        url, end_index = get_url_and_index(page)
        count = count + 1
        if url:
            print (count,'.Url: ', url)
            page = page[end_index:]
        else:
            print ('All Links are Print!!!')
            break


test = 'Hello slavo <a href="test1"> welcome <a href="test2"> we are varu welcome to reach you <a href="test3">'

print(all_urls(test))

# In Python 3.5 String and Bytes are not same as in Python2.7, the manual conversion between them need to do using and encode<==> decode method.
print('============== MimiCom24 =====================')
print(all_urls(page('http://mimicom24.com/').decode()))

# print('========== ENKI ==============================')
# print(all_urls(page('https//enki.com').decode()))
