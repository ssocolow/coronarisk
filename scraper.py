#gets coronavirus data from https://www.google.com/covid19-map/


#import the http requests lib
import requests
#import web scraping tool
from bs4 import BeautifulSoup as bs

#have the url to get the data from
url = "https://www.google.com/covid19-map/"

#get the page response
page = requests.get(url)

#parse it with bs
soup = bs(page.content, 'html.parser')

#get the data
results = soup.find_all("td",class_="uMsnNd HAChlc")

#the world confirmed, recovered, dead
wconfirmed = results[0].contents[0]
wrecovered = results[2].contents[0]
wdead = results[3].contents[0]

print("confirmed ", wconfirmed)
