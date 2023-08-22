import requests
from bs4 import BeautifulSoup

def EthereumPrice():
    url=requests.get('https://coinmarketcap.com/currencies/ethereum/')
    soup=BeautifulSoup(url.text,'lxml')
    PricePart=soup.find('span',{'class':'sc-16891c57-0 dxubiK base-text'})

    return PricePart.text

