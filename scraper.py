from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

page = urlopen(Request("https://www.reddit.com/r/worldnews/comments/459bpr/gravitational_waves_from_black_holes_detected/?limit=500", headers={'User-Agent': 'Mozilla'}))



soup = BeautifulSoup(page, 'html.parser')
print(type(soup))
# print(soup.prettify())

allParagraphs = soup.find_all('p')
print(allParagraphs)

