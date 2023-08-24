from BitCoin import BitCoinPrice
from Ethereum import EthereumPrice
from Cardano import CardanoPrice
from tkinter import *

root = Tk()
root.title('Crypto Currency View')
root.geometry('500x150')
root.resizable(width=False, height=False)
Crypto = StringVar()

# Frames
Frame1 = Frame(root, width=500, height=70)
Frame1.pack(side=TOP)

Frame2 = Frame(root, width=500, height=50)
Frame2.pack(side=TOP)

Frame3 = Frame(root, width=500, height=30, bg='green')
Frame3.pack(side=TOP)

Frame4 = Frame(root, width=500, height=90, bg='blue')
Frame4.pack(side=TOP)

# Labels
Label1 = Label(Frame1, text='Cryptos : Bitcoin, Ethereum, Cardano ')
Label1.pack(side=LEFT)

Label2 = Label(Frame2, text='What crypto currency do you want to view?')
Label2.pack(side=LEFT)

CryptoEntry = Entry(Frame2, textvariable=Crypto)
CryptoEntry.pack(side=LEFT)


# Identify Function
def Identify():
    crypto_choice = Crypto.get()  # Get the selected crypto from the Entry widget
    result = ""

    if crypto_choice == 'Bitcoin':
        try:
            getBitcoin = BitCoinPrice()
            result = f'Price : {getBitcoin[1]} \n Trading Volume(24h) : {getBitcoin[0]} \n Circulating Supply : {getBitcoin[2]} \n Market Capitalization : {getBitcoin[3]} '
        except:
            result = 'Sorry! Something went wrong!!! Please try again later.'
    elif crypto_choice == 'Ethereum':
        try:
            getEthereum = EthereumPrice()
            result = f'Price : {getEthereum[1]} \n Trading Volume(24h) : {getEthereum[0]} \n Circulating Supply : {getEthereum[2]} \n Market Capitalization : {getEthereum[3]} '
        except:
            result = 'Sorry! Something went wrong!!! Please try again later.'
    elif crypto_choice == 'Cardano':
        try:
            getCardano = CardanoPrice()
            result = f'Price : {getCardano[1]} \n Trading Volume(24h) : {getCardano[0]} \n Circulating Supply : {getCardano[2]} \n Market Capitalization : {getCardano[3]} '
        except:
            result = 'Sorry! Something went wrong!!! Please try again later.'
    else:
        result = 'Invalid crypto selection'

    ResultLabel.config(text=result)  # Update the ResultLabel with the result


# Button
ViewBtn = Button(Frame3, text='View', width=10, command=Identify)
ViewBtn.pack(side=LEFT)

# Result Frame
ResultLabel = Label(Frame4, text="")
ResultLabel.pack(side=LEFT)

root.mainloop()