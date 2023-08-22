import requests
from bs4 import BeautifulSoup


def BitCoinPrice():
    url=requests.get('https://coinmarketcap.com/currencies/bitcoin/')
    soup=BeautifulSoup(url.text,'lxml')
    PricePart=soup.find('span',{'class':'sc-16891c57-0 dxubiK base-text'})

    return PricePart.text

