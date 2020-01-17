from PyQt5 import QtWidgets, QtCore
from modules.controller.Deck import Deck
from modules.model.Player import Player
import sys


class Game:
    """Class which contains objects and variables needed to making game working"""
    def __init__(self, new_game=True):

        if new_game==False:
            print('\nImplementation error\nThere is not "Load game" option implemented yet!\nPlease, try start a new game')
            sys.exit()

        else:
            #Create Players
            self.players = list()
            for x in range (0, 2):
                self.players.append(Player(name=f'player{x+1}', no=x)) #It could be any names but for now we're creating players 1, 2 etc

            #Define some game attributes
            self.riches_maximum = 9
            self.resources_maximum = 10
            self.gold_coins_counter = 10 
            self.silver_coins_counter = 10

            #Create Deck of Playable cards based on source_filefile. Cards are not objects yet
            self.DeckPlayable = Deck(source_file='Playable')

            #Create Deck of buyabe cards based on source_file. Cards are not objects yet
            self.DeckBuyable = Deck(source_file='Buyable')

            #Create empty lists of cards aviable on gameboard
            self.playable_store_cards = list()
            self.buyable_store_cards = list()

            #Pick 6 Playable cards from deck to store (these cards are available for players to interact with)
            for x in range(0, 6): 
                self.playable_store_cards.append(self.DeckPlayable.pickOneCard())

            #Pick 5 Buyable cards from deck to store (these cards are available for players to interact with)
            for x in range(0, 5): 
                self.buyable_store_cards.append(self.DeckBuyable.pickOneCard())

            #Create variable which monitor current player
            self.current_player_no = self.players[0].no
            self.CurrentPlayer = self.players[0]
            self.turn_no = 0
