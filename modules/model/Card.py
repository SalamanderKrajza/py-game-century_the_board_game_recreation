from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class Card:
    """Class which contains all properties of single card"""
    def __init__(self, card_type, inputList=[], outputList=[], used=False, owner='game', points=0, bonus=0):
        self.card_type = card_type

        #QuicNote:
        #In case we're not need input&output (f.e. card have only cost to buy it or only produces something) 
        # we're using first list regardless if its input or output
        self.the_list = {0:inputList.copy(), 1:outputList.copy()}

        self.used = used
        self.owner = owner
        self.points =int(points)
        self.bonus = bonus
        self.resources = list() #This is list for resources left on card (player need to left something when he is taking card which is not last card on PlayableStore)
        self.popup_type = 'unknown' #This will change when card is clicked

