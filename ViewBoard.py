from CryptoExtraction import CoinPrice
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
Label1 = Label(Frame1, text='Crypto Information')
Label1.pack(side=LEFT)

Label2 = Label(Frame2, text='What crypto currency do you want to view?')
Label2.pack(side=LEFT)

CryptoEntry = Entry(Frame2, textvariable=Crypto)
CryptoEntry.pack(side=LEFT)



def convertWords(coin):
    word=coin.lower().replace(" ", "-")
    return word


def Identify():
    crypto_choice = Crypto.get() 
    coin=convertWords(crypto_choice)
    result = ""

    if coin:
        try:
            getcoin = CoinPrice(coin)
            result = f'Price : {getcoin[1]} \n Trading Volume(24h) : {getcoin[0]} \n Circulating Supply : {getcoin[2]} \n Market Capitalization : {getcoin[3]} '
        except:
            result = 'Sorry! Something went wrong!!! Please try again later.'
    else:
        result = 'Enter your crypto!!!'

    ResultLabel.config(text=result) 


# Button
ViewBtn = Button(Frame3, text='View', width=10, command=Identify)
ViewBtn.pack(side=LEFT)

# Result Frame
ResultLabel = Label(Frame4, text="")
ResultLabel.pack(side=LEFT)

root.mainloop()