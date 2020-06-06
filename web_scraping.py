import pandas
import requests

from bs4 import BeautifulSoup 

#Getting the webpage 
webpage = requests.get("https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets")

#Loading the content 
content = webpage.content

#Parsing the content
result = BeautifulSoup(content,'html.parser')

#Identifying the products on the page by the div tag and the class name 
products = result.find_all("div", {"class": "col-sm-4 col-lg-4 col-md-4"})

#creating a list for each of the desired piece of information 
names = []
links = []
prices = []

#Iterating over the list of products and extracting the necessary info

for item in products:
    names.append(item.a.string)
    links.append("https://webscraper.io" + item.a['href'])
    prices.append(item.h4.string)

print(names, len(names))
print(links, len(links))
print(prices , len(prices))


data = list(zip(names, links, prices))

#Creating the pandas dataframe
d= pandas.DataFrame(data, columns = ['Name', 'Link', 'Price'])

# Writing the dataframe to a new Excel File 
try:
    d.to_excel("Products.xlsx");
except:
    print("\nSomething went wrong ! Please check your code.")
else:
    print("\nWeb data successfully written to Excel.")
finally:
    print("\nQuitting the program. Bye!")


# End of Program




























