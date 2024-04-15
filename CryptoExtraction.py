import requests
from bs4 import BeautifulSoup
container1=[]

def CoinPrice(coin):
    url=requests.get(f'https://coinmarketcap.com/currencies/{coin}/')
    soup=BeautifulSoup(url.text,'lxml')
    PricePart=soup.find('div',{'class':'sc-f70bb44c-0 flfGQp flexStart alignBaseline'})
    Price=PricePart.find('span')

    VolumePart = soup.find_all('div', {"class": "sc-f70bb44c-0 sc-cd4f73ae-0 iowNqu flexBetween"})
    for i in VolumePart:
        container1.append(i.text)

    volume=list(filter(lambda element: 'Volume ' in element,container1))
    volume_value = '$'+volume[0].split('$')[1]
   
    circulationSupplyPart=list(filter(lambda element: 'Circulating supply' in element, container1))
    circulation_supply=circulationSupplyPart[0].split('\xa0')[1]
    
    containerDeeper=list(filter(lambda element: "Market cap" in element,container1))
    marketCapPart=list(filter(lambda element: "$" in element,containerDeeper))
    marketCap='$'+marketCapPart[0].split('$')[1]
    return volume_value,Price.text,circulation_supply,marketCap

