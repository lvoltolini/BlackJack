# import random 
# import numpy as np
# import pandas as pd
# import seaborn as sns 

# Implement to choose whether 52 ou 312 cards.
deck_option_52, deck_option_312 = '52', '312'

# Game class.
class Game:
    cards = np.array([f"{number}{color}" 
    for number in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for color in ["♤","♡","♢","♧" ]])
    def __init__(self, dealer, list_of_players, number_of_decks):
        self.cards = 
        self.dealer = dealer
        self.players = list_of_players

# Decisions to dealer and players (hit, blackjack, stop)
class Bets:
    player_or_dealer = True

    def change_money(self, amount):
        self.money = self.money + amount
    
    def Stop(self, amount):
        pass
    
# Decisions exclusive to players (double-down, split)
class Bets_of_players:
    player = True
    pot = 0
    def add_to_pot(self, amount, previous_pot = 0):
        self.pot = previous_pot + amount
    
    def Split(self, deck, pot):
        pass
    def Hit(self, deck):
        pass 
    def Double_Down(self, deck):
        pass
    def Stop(self, deck):
        pass

# If needed, considerations about Deck.
class Deck:
    pass
    
# Dealer Class
class Dealer(Bets):
    def __init__(self, money, stop_card):
        self.money = money
        self.stop_card = stop_card
        self.deck = []
        self.sum = sum(self.deck)
    
    def change_Money(self, amount):
        self.money = self.money + amount

# Players class
class Player(Bets):
    alive = True
    Breathing = True 
    def __init__(self, money, stop_card = 21, double_card = 100):
        self.money = money
        self.deck = []
        self.sum = self.deck
        self.stop_card = stop_card
        self.double_card = double_card
    

# Inicializando o jogo:

options_message = ' \nOpzioni: \n-------------------------------------------------------------------------------- \nS: Split \nH: Hit \nD: Double-Down \nF: Stop'

