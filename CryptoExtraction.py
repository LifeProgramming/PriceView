import requests
from bs4 import BeautifulSoup

def CoinPrice(coin):
    url=requests.get(f'https://coinmarketcap.com/currencies/{coin}/')
    soup=BeautifulSoup(url.text,'lxml')
    PricePart=soup.find('div',{'id':'section-coin-overview'})
    Price=PricePart.find('span',{"class":"sc-65e7f566-0 clvjgF base-text"})
    return Price.text
