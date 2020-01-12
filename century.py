#Steps to do:
#I. Game initialization
# - Create all Objects
#       - Game (New/Load)
#           - Deck
#               -  cards
#           - players
#               - score
#               - deck
#                   - cards
#               - resources
#           - status (turn)

#II. Create UI based on gameobjects
# - create area for Buyable cards
# - create area for Playable cards
# - create area for player1 hand
# - fill mentioned areas with cards 
# - create history area which contain description of last few actions
# - display current turn
# - display storage of all players
# - display points of all players


#III. Control the game (add methods for UI interface), check win conditions etc
# - monitore which player turn is now
# - monitore if someone win the game
# - buying riches cards
# - buying Playable cards
# - playing upgrade card
# - playing harvest card
# - playing trade card
# - additional actions on cards in player hand
#       - moving them
# - additional bonuses on riches cards in store
#       - show coins, get coins
# - additional bonuses on palayable cards in store
#       - show extra dies to get
# - system for drawing extre dies
# - system for



import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

from modules.view.Ui import Ui
from modules.model.Game import Game
from modules.controller.Controller import Controller
from modules.view.Popup import Popup

#Create Game Object
MyGame = Game(new_game=True)


#Configure and show UI
App = QtWidgets.QApplication(sys.argv) 
MyUi = Ui(MyGame)

#Create Popup to comunicate with player after he pressed something
MyPopup = Popup(Game=MyGame, Ui=MyUi)

#Control the game
MyController = Controller(MyGame, MyUi, MyPopup)

sys.exit(App.exec_())


