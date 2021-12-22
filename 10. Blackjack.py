#Blackjack
#this is the first project I genuinly couldn't finish after 5+ hours of research and testing
#the  problem occures when I try to add the different values for the cards to get 21
#right now I didn't find a way to do it with using classes, they dont give out ["Number", "type"] but instead ["Number Type"]
#while this may seem like a big knock, I actually think that I learned a lot in this project
#it gave me a really good understanding of classes and how to use them, and especially when to not use them  

import random

#setup for the game to start
class card():
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def show_cards(self):
        print(self.value, self.color)   

#all the types        
colors = ["diamond", "heart", "spades","clubs"]
deck = [card(value, color) for value in range(1, 14) for color in colors]

#shuffle deck
def deck_shuffle():
    random.shuffle(deck)
deck_shuffle()

#number of cards in deck and field
cards_in_deck = len(deck)
cards_on_field = 0

#how many still on deck and on field
status = cards_on_field, cards_in_deck

#which cards are on the field
field = []

#drawing a card updates all information
def draw_card():
    global cards_in_deck
    cards_in_deck = cards_in_deck - 1

    global cards_on_field
    cards_on_field = cards_on_field + 1

    if cards_in_deck <= 0:
        print("Restart Game")
        exit()
    else:
        pass

    global status
    status = cards_on_field, cards_in_deck
    
    #add card drawn to field/remove it from the deck
    field.append(deck[cards_in_deck - cards_in_deck])
    new_field_card = deck[cards_in_deck - cards_in_deck]
    deck.remove(deck[cards_in_deck - cards_in_deck])

    #show the card you drew
    print("You drew")
    card.show_cards(new_field_card)

    
draw_card()
card.show_cards(field[0])


#game begin
goal = 21
loop = True


while loop:
    loop = False
    











