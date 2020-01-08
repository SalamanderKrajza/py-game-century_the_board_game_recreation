from modules.Card import Card
import sys

class Player():
    """Class which contains all properties of single player"""
    def __init__(self, name, no):
        pass

        #All basic properties
        self.name = name
        self.points = 0
        self.no = no

        #Create PlayerHand
        self.playerHand = list()

        #Pick starter cards
        self.playerHand.append(Card(card_type='Harvest', \
            inputList=['k1', 'k1', '', '', ''], \
                outputList=['', '', '', '', ''], \
                    used=False, owner=self.name))
        self.playerHand.append(Card(card_type='Upgrade', \
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

        #calculate score points at end of the turn