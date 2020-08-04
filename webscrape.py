import webbrowser
import requests
import bs4
from googlesearch import *

#input any song here, can make it user input if you want
query = "Water by G Lyrics"

#website that will be searched
website = ''

#gives top result in google search(genius lyrics)
for j in search(query, tld="co.in", num=1, stop=1, pause=2):
    website = j
    #opens webpage
    webbrowser.open(j)
  
result = requests.get(website)

#parses html
soup = bs4.BeautifulSoup(result.text,'lxml')

#finds paragraph tag that contains the lyrics
lyrics = soup.select('p')

#prints the lyrics
print(lyrics[0].getText())

