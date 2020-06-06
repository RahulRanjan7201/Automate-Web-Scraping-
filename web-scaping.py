import requests 
from bs4 import BeautifulSoup
webpage = requests.get("https://www.webscraper.io/test-sites/e-commerce/static")

print(type(webpage))
text = webpage.text

content = webpage.content

# Use the beautiful Soup class to parse the pareser 

result = BeautifulSoup(content, "html.parser")

#Get the content of head tag
print(result.head)
h2 = result.h2

print(h2)
title = result.title
print(title)


print(result.header.div.div.a.button)

res = result.find("div")
print(res)

res = result.find_all("h1")
print(res)
#Length of res h1 
print(len(result.find_all("h1")))