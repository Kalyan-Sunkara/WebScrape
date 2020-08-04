import webbrowser
import requests
import bs4
from googlesearch import *

query = "Water by G Lyrics"
website = ''
for j in search(query, tld="co.in", num=1, stop=1, pause=2):
    website = j
    webbrowser.open(j)
result = requests.get(website)
soup = bs4.BeautifulSoup(result.text,'lxml')
lyrics = soup.select('p')
print(lyrics[0].getText())
# webbrowser.open('https://soundcloud.com')
