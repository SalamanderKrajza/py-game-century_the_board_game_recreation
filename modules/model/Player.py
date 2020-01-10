from modules.model.Card import Card
import sys

class Player():
    """Class which contains all properties of single player"""
    def __init__(self, name, no):
        pass

        #All basic properties
        self.name = name
        self.points = 0
        self.no = no
        self.riches_count = 0
        self.riches_points = 0
        self.coins_gold = 0
        self.coins_silver = 0
        self.coins_points = 0

        #Create PlayerHand
        self.player_hand = list()

        #Pick starter cards
        self.player_hand.append(Card(card_type='Harvest', \
            inputList=['k1', 'k1', '', '', ''], \
                outputList=['', '', '', '', ''], \
                    used=False, owner=self.name))
        self.player_hand.append(Card(card_type='Upgrade', \
            inputList=['2', '', '', '', ''], \
                outputList=['', '', '', '', ''], \
                    used=False, owner=self.name))

        #Pick pick some starting resources based on player order
        if self.no == 0:
            self.resources = ['k1','k1','k1']
        elif self.no == 1:
            self.resources = ['k1','k1','k1', 'k1']
        elif self.no == 2:
            self.resources = ['k1','k1','k1', 'k1']
        elif self.no == 3:
            self.resources = ['k1','k1','k1', 'k2']
        elif self.no == 4:
            self.resources = ['k1','k1','k1', 'k2']
        else:
            print('\nWarning\nThere is more than 5 players which is unusual\nGame was projected for maximum 5 players for best experience')
            self.resources = ['k1','k1','k1', 'k1', 'k2']

        self.resources_count = len(self.resources)
        self.resources_points = self.resources_count - self.resources.count('k1') #every  die other than k1 gives 1 point

        self.total_points = self.resources_points + self.riches_points + self.coins_points
        #calculate score points at end of the turn