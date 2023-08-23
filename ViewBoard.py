from  BitCoin import BitCoinPrice
from Ethereum import EthereumPrice
from Cardano import  CardanoPrice


print('cryptos : Bitcoin, Ethereum, Cardano')
print('What crypto currency do you want to view? ')
Crypto=input('Your crypto : ')
try:
    if Crypto=='Bitcoin':
        getBitcoin=BitCoinPrice()
        print(f' Price : {getBitcoin[1]} \n Trading Volume(24h) : {getBitcoin[0]} \n Circulating Supply : {getBitcoin[2]} \n Market Capitalization : {getBitcoin[3]} ')
    elif Crypto=='Ethereum':
        getEthereum=EthereumPrice()
        print(f' Price : {getEthereum[1]} \n Trading Volume(24h) : {getEthereum[0]} \n Circulating Supply : {getEthereum[2]}  \n Market Capitalization : {EthereumPrice()[3]}')
    elif Crypto=='Cardano':
        getCardano=CardanoPrice()
        print(f' Price : {getCardano[1]} \n Trading Volume(24h) : {getCardano[0]}\n Circulating Supply : {getCardano[2]}  \n Market Capitalization : {getCardano[3]}')
except:
    print('Sorry! Something went wrong!!! Pease try again later.')