from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

#This is part of Ui class
def display_game_window(self):
    """This method defines all properties of window which contains the Game"""
    self.Screen = QtWidgets.QWidget() #MyGame_Screen is entire screen which contains all objects (Cards, score etc)
    self.Screen.setObjectName("MyGame_Screen") #Thanks to setObjectName we can configure style for this object by giving its name
    self.Screen.resize(1400, 800) #This dimenshion describes whole Game
    self.Screen.setStyleSheet(
        "*{margin: 0; padding: 1px; line-height: 40px;}"
        #"*{border: 1px solid #000; padding: 0;}\n" #Used for show grid while testing card; we have to replace padding because border make the same effect
        #"#test{border: 1px solid #F00}" 
        "#MyGame_Screen{background-image: url(images/board2.png)}"
        #"#MyGame_Screen{background-color: #b38b79"
        "QPushButton{"
        "background-color: #b19686; "
        "border: 1px solid black;"
        "border-radius: 8;"
        "font-size: 12px;  font-weight: 500;"
        "}"
        "QPushButton:hover{"
        "background-color: #e5e2d7;"
        "}"

        )