from modules.model.Card import Card
import sys

class Player():
    """Class which contains all properties of single player"""
    def __init__(self, name, player_number):

        self.generate_basic_attributes(name, player_number)
        self.create_list_for_cards_in_player_hand()
        self.pick_starter_cards()
        self.pick_starter_resources()
        self.calculate_amount_of_resources_and_points()

    def generate_basic_attributes(self, name, player_number):
        """All attributes that describes players and may be keeped as variables"""
        self.name = name
        self.points = 0
        self.player_number = player_number
        self.riches_count = 0
        self.riches_points = 0
        self.coins_gold = 0
        self.coins_silver = 0
        self.coins_points = 0

    def create_list_for_cards_in_player_hand(self):
        """Creates empty list that will contain player cards"""
        self.player_hand = list()

    def pick_starter_cards(self):
        """Generates cards that every player should have at start of the game"""
        self.player_hand.append(Card(
            card_type='Harvest',
            inputList=['k1', 'k1', '', '', ''],
            owner=self.name
            ))

        self.player_hand.append(Card(
            card_type='Upgrade',
            inputList=['2', '', '', '', ''],
            owner=self.name
            ))

    def pick_starter_resources(self):
        """Amount of started resources is different for players basing of their number"""
        if self.player_number == 0:
            self.resources = ['k1','k1','k1']
        elif self.player_number == 1:
            self.resources = ['k1','k1','k1', 'k1']
        elif self.player_number == 2:
            self.resources = ['k1','k1','k1', 'k1']
        elif self.player_number == 3:
            self.resources = ['k1','k1','k1', 'k2']
        elif self.player_number == 4:
            self.resources = ['k1','k1','k1', 'k2']
        else:
            print('\nWarning\nThere is more than 5 players which is unusual\nGame was projected for maximum 5 players for best experience')
            self.resources = ['k1','k1','k1', 'k1', 'k2']

    def calculate_amount_of_resources_and_points(self):
        """
        Calculates values to display on player panel
        This method sould be replaced with similar inside controller module if controller will be refactorized
        """
        self.resources_count = len(self.resources)
        self.resources_points = self.resources_count - self.resources.count('k1') #every die other than k1 gives 1 point
        self.total_points = self.resources_points + self.riches_points + self.coins_points