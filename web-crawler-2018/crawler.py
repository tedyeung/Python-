# Building simple Web Crawler 
# Using python 3 version


page = '<a href="http://www.mimicom24.com"></a>'
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote)
url = page[start_quote + /:end_quote]
print (url)



