from bs4 import BeautifulSoup
import requests
def best__games():
    #Getting into the website and scraping the data
    google ='https://www.gamesradar.com/best-games-2022/'
    source = requests.get(google).text
    soup = BeautifulSoup(source,'lxml')
    print("These are the best games of 2022 (according to gameradar.com)\n\n\n")
    #prints every game from the website
    for i in soup.find_all("h2"): print(i.text+"\n")
    input("") 
#Stops the application from auto close
best__games()
