name = "ytsr"
import urllib
from urllib.request import urlopen 
from bs4 import BeautifulSoup

def yt_search(s1):
    query=urllib.parse.quote(s1)
    url="https://www.youtube.com/results?sp=EgIQAQ%253D%253D&search_query="+query
    res=urlopen(url)
    html=res.read()
    soup=BeautifulSoup(html,features="html.parser")
    li1=[]
    li2=[]
    li3=[]
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        li1.append('https://www.youtube.com' + vid['href'])
    for b in soup.findAll(attrs={'data-ytimg':"1"}):
        if "hqdefault.jpg" in b['src']:
            li3.append(b['src'])
            for c in b['src'].split("?"):
                if "hqdefault.jpg" in c:
                    li2.append(c)
    li4=[li1,li2,li3]
    return li4
    
