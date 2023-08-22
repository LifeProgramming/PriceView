from  BitCoin import BitCoinPrice
from Ethereum import EthereumPrice
from Cardano import  CardanoPrice


print('cryptos : Bitcoin, Ethereum, Cardano')
print('What crypto currency do you want to view? ')
Crypto=input('Your crypto : ')
try:
    if Crypto=='Bitcoin':
        print(BitCoinPrice())
    elif Crypto=='Ethereum':
        print(EthereumPrice())
    elif Crypto=='Cardano':
        print(CardanoPrice())
except:
    print('Sorry! Something went wrong!!! Pease try again later.')