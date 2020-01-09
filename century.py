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
# - create area for buyable cards
# - create area for playable cards
# - create area for player1 hand
# - fill mentioned areas with cards 
# - create history area which contain description of last few actions
# - display current turn
# - display storage of all players
# - display points of all players


#III. Control the game (add methods for UI interface), check win conditions etc




import sys
import random
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

from modules.view.Ui import Ui
from modules.model.Game import Game


#Create Game Object
MyGame = Game(new_game=True)


#Configure and show UI
app = QtWidgets.QApplication(sys.argv) 
myUi = Ui(MyGame)
sys.exit(app.exec_())


