 # This program provides two GUI-based games for a user to play and allows the
# user to pick their game of choice.

# Credit for all playing card images and all dice images goes to Clip Art Library! (clipart-library.com).



from tkinter import Text, Button, Label, PhotoImage, Canvas
import tkinter as tk
import random
from PIL import Image, ImageTk
import os


def craps_game():
    global crapsRoot
    crapsRoot = tk.Toplevel()
    crapsRoot.geometry('500x500')
    crapsRoot.title("Craps Game")
    crapsRoot.configure(bg='#097969')
    crapsPlayLabel = Label(crapsRoot, text="Let's Play Craps!")
    crapsPlayLabel.configure(font=("Comic Sans MS", 20, "bold"), bg='#097969', fg="white")
    crapsPlayLabel.place(x=130, y=10)
    global rollButton
    rollButton = Button(crapsRoot, text="Roll", command=play_craps)
    rollButton.place(x=150, y=350)
    newGameButton = Button(crapsRoot, text="New Game", command=new_craps_game)
    newGameButton.place(x=300, y=350)


def play_craps():
    diceFileName = ['diceSide1.jpg', 'diceSide2.jpg', 'diceSide3.jpg', 'diceSide4.jpg', 'diceSide5.jpg', 'diceSide6.jpg']
    pickDice = random.randint(0, 5)
    global diceImage1Label
    diceImage1Label = tk.Label(crapsRoot)
    diceImage1 = Image.open('C:/Users/elect/OneDrive/Pictures/DICE/{}'.format(diceFileName[pickDice]))
    diceImage1Resize = diceImage1.resize((100, 100))
    diceImage1Final = ImageTk.PhotoImage(diceImage1Resize)
    diceImage1Label.image = diceImage1Final
    diceImage1Label['image'] = diceImage1Label.image
    diceImage1Label.place(x=120, y=80)
    pickDice2 = random.randint(0, 5)
    global diceImage2Label
    diceImage2Label = tk.Label(crapsRoot)
    diceImage2 = Image.open('C:/Users/elect/OneDrive/Pictures/DICE/{}'.format(diceFileName[pickDice2]))
    diceImage2Resize = diceImage2.resize((100, 100))
    diceImage2Final = ImageTk.PhotoImage(diceImage2Resize)
    diceImage2Label.image = diceImage2Final
    diceImage2Label['image'] = diceImage2Label.image
    diceImage2Label.place(x=260, y=80)
    diceValue = [1, 2, 3, 4, 5, 6]
    rollValue = diceValue[pickDice] + diceValue[pickDice2]
    global rollValLabel
    rollValLabel = Label(crapsRoot, text='Value for this roll: {}   '.format(str(rollValue)))
    rollValLabel.configure(bg='#097969', fg="white")
    rollValLabel.place(x=120, y=240)
    global winLoseLabel
    winLoseLabel = tk.Label(crapsRoot)
    if rollValue == 7 or rollValue == 11:
        winLoseLabel.configure(font=("Comic Sans MS", 20, "bold"), bg='#097969', fg="white", text="           Winner!                         ")
        winLoseLabel.place(x=80, y=270)
    else:
        winLoseLabel.configure(font=("Comic Sans MS", 20, "bold"), bg='#097969', fg="white", text="Sorry! Better Luck Next Time!")
        winLoseLabel.place(x=80, y=270)

    rollButton.configure(state="disabled")


def new_craps_game():
    diceImage1Label.destroy()
    diceImage2Label.destroy()
    rollValLabel.destroy()
    winLoseLabel.destroy()
    rollButton.configure(state="normal")
    


def card_game():
    global cardRoot
    cardRoot = tk.Toplevel()
    cardRoot.geometry('500x500')
    cardRoot.title("Card Game")
    cardRoot.configure(bg='#097969')
    playCardsLabel = Label(cardRoot, text="Let's Play Cards!")
    playCardsLabel.configure(font=("Comic Sans MS", 20, "bold"), bg='#097969', fg="white")
    playCardsLabel.place(x=150, y=30)
    intCardLabel = tk.Label(cardRoot)
    intCardImage = Image.open('C:/Users/elect/OneDrive/Pictures/DECK/cardbackcopy.jpg')
    intCardResize = intCardImage.resize((100, 150))
    intCardFinal = ImageTk.PhotoImage(intCardResize)
    intCardLabel.image = intCardFinal
    intCardLabel['image'] = intCardLabel.image
    intCardLabel.place(x=200, y=100)
    dealButton = Button(cardRoot, text="Deal", command=deal_card)
    dealButton.place(x=150, y=315)
    shuffleButton = Button(cardRoot, text="Shuffle", command=deal_card)
    shuffleButton.place(x=230, y=315)
    newDeckButton = Button(cardRoot, text="New Deck", command=new_deck)
    newDeckButton.place(x=320, y=315)
    
    
def deal_card():
    cardVal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k']
    cardValNames = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    cardSuit = ['c', 'h', 's', 'd']
    suitNames = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
    newValNum = random.randint(0, 12)
    newVal = cardVal[newValNum]
    suitNum = random.randint(0, 3)
    newSuit = cardSuit[suitNum]
    newCardLabel = tk.Label(cardRoot)
    newCardImage = Image.open('C:/Users/elect/OneDrive/Pictures/DECK/{}{}.png'.format(str(newVal), str(newSuit)))
    newCardResize = newCardImage.resize((100, 150))
    newCardFinal = ImageTk.PhotoImage(newCardResize)
    newCardLabel.image = newCardFinal
    newCardLabel['image'] = newCardLabel.image
    newCardLabel.place(x=200, y=100)
    newCardText = Label(cardRoot, text=f'{cardValNames[newValNum]} of {suitNames[suitNum]}           ')
    newCardText.configure(bg='#097969', fg="white")
    newCardText.place(x=200, y=275)
    cardVal.pop(newValNum)
    cardValNames.pop(newValNum)
    cardSuit.pop(suitNum)
    suitNames.pop(suitNum)

def new_deck():
    intCardLabel = tk.Label(cardRoot)
    intCardImage = Image.open('C:/Users/elect/OneDrive/Pictures/DECK/cardbackcopy.jpg')
    intCardResize = intCardImage.resize((100, 150))
    intCardFinal = ImageTk.PhotoImage(intCardResize)
    intCardLabel.image = intCardFinal
    intCardLabel['image'] = intCardLabel.image
    intCardLabel.place(x=200, y=100)
    coverLabel = Label(cardRoot, text='                                        ')
    coverLabel.configure(bg='#097969', fg='#097960')
    coverLabel.place(x=200, y=275)
    

   
    
     
root = tk.Tk()
root.title("Dual Game Project")
root.geometry('1000x1000')
root.configure(bg='#005900')

mainLabel = Label(root, text="Which game would you like to play?")
fontChoice = ("Comic Sans MS", 30, "bold")
mainLabel.configure(font=fontChoice, bg='#005900', fg="white")
mainLabel.place(x=150, y=200)
dicePhoto = ImageTk.PhotoImage(file='C:/Users/elect/OneDrive/Pictures/DICE/diceSide2.jpg')
crapsButton = Button(root, text="Craps", image=dicePhoto, command=craps_game)
crapsButton.place(x=650, y=400)
crapsLabel = Label(root, text="Craps")
crapsLabel.configure(font=("Comic Sans MS", 20, "bold"), bg='#005900', fg="white")
crapsLabel.place(x=660, y=500)
cardbackPhoto = Image.open('C:/Users/elect/Downloads/cardback.jpg')
cardbackPhotoResize = cardbackPhoto.resize((100, 100))
cardbackPic = ImageTk.PhotoImage(cardbackPhotoResize)
cardbackButton = Button(root, text="cards", image=cardbackPic, command=card_game)
cardbackButton.place(x=250, y=395)
cardbackLabel = Label(root, text="Cards")
cardbackLabel.configure(font=("Comic Sans MS", 20, "bold"), bg='#005900', fg="white")
cardbackLabel.place(x=260, y=500)



root.mainloop()




