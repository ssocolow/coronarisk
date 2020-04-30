#import web scraping tool
from bs4 import BeautifulSoup as bs

#open file
f = open("htext.txt","r")
htmltext = f.read()
f.close()

#parse it with bs
soup = bs(htmltext, 'html.parser')

#results = soup.find_all("td",class_="uMsnNd HAChlc")
results = soup.find_all("tr",class_="viwUIc")

print(results)
