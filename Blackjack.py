import time as t
import random as ra
import tkinter as tk

CardValues = {"A♠":11,"2♠":2,"3♠":3,"4♠":4,"5♠":5,"6♠":6,"7♠":7,"8♠":8,"9♠":9,"10♠":10,"J♠":10,"Q♠":10,"K♠":10,
              "A♥":11,"2♥":2,"3♥":3,"4♥":4,"5♥":5,"6♥":6,"7♥":7,"8♥":8,"9♥":9,"10♥":10,"J♥":10,"Q♥":10,"K♥":10,
              "A♣":11,"2♣":2,"3♣":3,"4♣":4,"5♣":5,"6♣":6,"7♣":7,"8♣":8,"9♣":9,"10♣":10,"J♣":10,"Q♣":10,"K♣":10,
              "A♦":11,"2♦":2,"3♦":3,"4♦":4,"5♦":5,"6♦":6,"7♦":7,"8♦":8,"9♦":9,"10♦":10,"J♦":10,"Q♦":10,"K♦":10}
Cards = ["A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠",
         "A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
         "A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣",
         "A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦"]


print("Welcome to our casino, sadly the only game we have that you can play is blackjack so thats what youll be doing. \nwe'll start you off with 5000 chips, good luck ")
t.sleep(1)
print("Hello I will be your dealer for today \n lets get started")
chips = 5000
pHand = []
spHand = []
pHandValue = 0
dHand = []
dHandValue = 0

def placeBets():
    global pbet
    pbet = input("What would you like to bet? \n")
    if pbet > chips:
        print("you dont have that amount of chips please bet lower")
        placeBets()
    else:
        print("lets get started")

def dealCards():
    global pHandValue
    global dHandValue
    for i in range(2):
        pHand.append(Cards[ra.randint(1, 52)])
        dHand.append(Cards[ra.randint(1, 52)])
    if pHand[0] == pHand[1]:
        pHand.pop(1)
        pHand.append(Cards[ra.randint(1, 52)])
    else:
        print("You're hand is " + str(pHand))
        pHandValue += CardValues[pHand[0]]
        pHandValue += CardValues[pHand[1]]

    if dHand[0] == dHand[1]:
        dHand.pop(1)
        dHand.append(Cards[ra.randint(1, 52)])
    else:
        print("the dealers hand is "+ str(dHand[0]) +", Hidden")
        dHandValue += CardValues[dHand[0]]
        dHandValue += CardValues[dHand[1]]
    print(pHandValue, dHandValue)
                                         
def blackjack():
    global chips
    if pHandValue == 21:
        print("You've got a blackjack!")
        chips += pbet * 2
    elif dHandValue == 21:
        print("Dealers got a blackjack")
        chips - pbet 

def outcome():
    global chips 
    if pHandValue > dHandValue:
        print("you win this one")
        chips += pbet*2 
    elif dHandValue > pHandValue:
        print("dealer wins this one")
        chips -= pbet 
    else:
        print("its a draw (no chips taken or given)")

def dealer_draw():
    global dHandValue
    if dHandValue == 17:
        print("Dealer will stay at 17")
    elif dHandValue > 21:
        print("Dealer is a bust")
    else:
        i = 3
        while dHandValue < 21: 
            dHand.append(Cards[ra.randint(1, 52)])
            dHandValue += CardValues[dHand[i]]
            print("Dealer drew " + str(dHand(i)))
            i += 1

def pSplit():


            




    
        
def pDecision():
    play = str(input("would you like to hit, stand, or double down? (enter withput caps) \n"))
    if play == "hit":
        pass
    elif play == "stand":
        pass
    elif play == "double down":
        if pbet * 2 > chips:
            ("you dont have enou'print'gh chips to double down\ntry again")
            pDecision()
        
    elif play == "split":
        pSplit
    else:
        print("answer the question right")
        pDecision()
