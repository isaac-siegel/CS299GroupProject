from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


def openPage():
    page = urlopen(Request("https://www.reddit.com/r/worldnews/comments/459bpr/gravitational_waves_from_black_holes_detected/?limit=500", headers={'User-Agent': 'Mozilla'}))
    soup = BeautifulSoup(page, 'html.parser')
    return soup

def getComments(soup):
    usertexts = soup.find_all("div", class_="usertext-body")
    divs = list(map(lambda x: x.find( class_="md"), usertexts))

    listOfPs = []
    for md in divs:
        oneCommentPs = md.find_all('p')
        for p in oneCommentPs:
            listOfPs.append(p.getText())

    listOfComments = listOfPs[32:]
    return listOfComments

def driver():
    soup = openPage()

    comments = getComments(soup)

    for thing in comments:
        print(thing)
    print(len(comments))

driver()


