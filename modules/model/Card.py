from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class Card:
    """Class which contains all properties of single card"""
    def __init__(self, card_type, inputList=[], outputList=[], used=False, owner='game', points=0, bonus=0):
        self.card_type = card_type
        self.the_list = {0:inputList.copy(), 1:outputList.copy()}
        self.used = used
        self.owner = owner
        self.points =int(points)
        self.bonus = bonus
        self.popup_type = 'unknown' #This will change when card is clicked

