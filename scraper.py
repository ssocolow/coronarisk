#gets coronavirus data from https://www.google.com/covid19-map/


#import the http requests lib
import requests
#import web scraping tool
from bs4 import BeautifulSoup as bs

#have the url to get the data from
url = "https://www.google.com/covid19-map/"
url2 = "https://www.google.com/search?client=ubuntu&hs=Y9p&sxsrf=ALeKk02iNo1zo5r28N8uVFuv59HYAt3QPg%3A1588167007653&ei=X4GpXseyJ6K1ggf6v6qwDw&q=maine+counties+covid+cases&oq=maine+counties+co&gs_lcp=CgZwc3ktYWIQARgAMgIIADoECAAQRzoECCMQJzoFCAAQkQI6BQgAEIMBOggIABCDARCRAjoHCAAQgwEQQzoECAAQQzoHCAAQFBCHAlCaKFjsR2D2U2gCcAR4AIAB6wKIAYcakgEIMC4xMy40LjKYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab"

#get the page response
page = requests.get(url2)

#parse it with bs
soup = bs(page.content, 'html.parser')

#get the data
#results = soup.find_all("td",class_="uMsnNd HAChlc")
results = soup.find_all("td",class_="LeGwof")

print(results)

#the world confirmed, recovered, dead
wconfirmed = results[0].contents[0]
wrecovered = results[2].contents[0]
wdead = results[3].contents[0]

print("confirmed ", wconfirmed)
