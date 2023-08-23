import requests
from bs4 import BeautifulSoup

def EthereumPrice():
    url=requests.get('https://coinmarketcap.com/currencies/ethereum/')
    soup=BeautifulSoup(url.text,'lxml')
    PricePart=soup.find('span',{'class':'sc-16891c57-0 dxubiK base-text'})
    VolumePart = soup.find_all('dd', {"class": "sc-16891c57-0 fRWxhs base-text"})[1].text
    CirculatingSupply = soup.find_all('dd', {'class': 'sc-16891c57-0 fRWxhs base-text'})[3].text
    MarketCapitalization = soup.find('dd', {'class': 'sc-16891c57-0 fRWxhs base-text'}).text

    # Find the index of the first `$` character.
    index = VolumePart.find("$")
    index1 = MarketCapitalization.find('$')

    # Return the substring starting from the index of the `$` character.
    Volume = VolumePart[index:]
    MarketCap = MarketCapitalization[index1:]

    return Volume, PricePart.text, CirculatingSupply, MarketCap

