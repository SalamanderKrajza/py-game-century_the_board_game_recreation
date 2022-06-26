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
            self.set_game_settings()
            self.create_lists_for_game_objects()
            self.create_players_object()
            self.create_decks_objects()

            #Starting shop that contains playable cards (used to get resources)
            self.lay_out_store_cards(
                target_list=self.playable_store_cards_list, 
                source_deck=self.DeckPlayable, 
                amount_of_cards_to_be_picked=6
                )

            #Starting shop that contains rihces cards (required to win the game)
            self.lay_out_store_cards(
                target_list=self.buyable_store_cards_list, 
                source_deck=self.DeckBuyable, 
                amount_of_cards_to_be_picked=5
                )

            self.create_current_game_state_variables()

    def set_game_settings(self):
        """Method describes game parameters like target ammount of riches, limits for resources that player may have etc."""
        self.riches_maximum = 1
        self.resources_maximum = 10
        self.gold_coins_counter = 10 
        self.silver_coins_counter = 10
    
    def create_lists_for_game_objects(self):
        """This method creates all lists that will contains game objects like players, decks etc."""
        #Create empty list for players
        self.players_list = list()
        
        #Create empty lists of cards aviable on gameboard
        self.playable_store_cards_list = list()
        self.buyable_store_cards_list = list()

    def create_players_object(self, number_of_players=2, names=False):
        """
        Method creates player
        In final versions it may be customizable with different names and amount of players
        """
        if not names:
            names = [f'player{number_of_players+1}' for number_of_players in range(0, number_of_players)]
        
        for player_number in range(0, number_of_players):
            self.players_list.append(Player(name=names[player_number], player_number=player_number)) 

    def create_decks_objects(self):
        """Decks objects contains cards prepared in csv files"""
        self.DeckPlayable = Deck(source_file='Playable')
        self.DeckBuyable = Deck(source_file='Buyable')

    def lay_out_store_cards(self, target_list, source_deck, amount_of_cards_to_be_picked):
        """Pick cards that needs to be on board to be buyed by players"""
        for number_of_card in range(0, amount_of_cards_to_be_picked):
            target_list.append(source_deck.pickOneCard())

    def create_current_game_state_variables(self):
        """Variables that trakcs current player and turn number"""
        self.current_player_no = self.players_list[0].player_number
        self.CurrentPlayer = self.players_list[0]
        self.turn_no = 0