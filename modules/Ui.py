from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

from functools import partial
import datetime

from modules.ScrollBox import ScrollBox

class Ui:
    """Class responsible for management of graphic interface of game"""
    def __init__(self, game):
        pass
        self.game = game

        #Game window
        self.displayGameWindow()

        #Prepare space to contain cards
        #playable
        self.buyableStore = ScrollBox(parentWidget=self.Screen, cardsCnt=5, \
            leftMargin=700, topMargin=100, height=170)
        #buyable
        self.playableStore = ScrollBox(parentWidget=self.Screen, cardsCnt=6, \
            leftMargin=570, topMargin=280, height=170)
        #player hand
        self.playerHand = ScrollBox(parentWidget=self.Screen, cardsCnt=8, \
            leftMargin=300, topMargin=550, height=220)

        #Display last played card

        #Display cards in storages        
        for card in game.playable_store_cards:
            self.displayCard(card=card, target=self.playableStore.HorizontalLayout)

        for card in game.buyable_store_cards:
            self.displayCard(card=card, target=self.buyableStore.HorizontalLayout)

        #Display cards in player hand
        for card in game.players[0].playerHand:
            self.displayCard(card=card, target=self.playerHand.HorizontalLayout)
        #Resize playerhand scrollbox (this have not fixed size)
        self.playerHand.scrollAreaWidgetContents.resize(130*len(game.players[0].playerHand), self.playerHand.scrollAreaWidgetContents.height())

        #self.displayCard(card=card, target=self.buyableStore.HorizontalLayout)

        #Display "Current Player"
        
        #Display history
        self.history = ScrollBox(parentWidget=self.Screen, cardsCnt=4, \
            leftMargin=10, topMargin=100, height=370, orientation='vertical')
        self.history.scrollAreaWidgetContents.resize(self.history.scrollAreaWidgetContents.width(), 20)



        #Filling the history with something for tests
        for x in range(1, 22):
            now = datetime.datetime.now()
            qtemp = QtWidgets.QLabel(f'<font color=\"blue\">[{now.hour:02d}:{now.minute:02d}:{now.second:02d}]</font> \
                [Player{x}] has played [Trade] card [1 times].<br> \
                    Player traded [1{self.img("k1")}, 1{self.img("k2")}, 1{self.img("k3")}, 1{self.img("k4")}] for [3{self.img("k1")}, 3{self.img("k4")}]')
            self.history.VerticalLayout.addWidget(qtemp)
            self.history.scrollAreaWidgetContents.resize(self.history.scrollAreaWidgetContents.width(), self.history.scrollAreaWidgetContents.height()+30)
            


        #show screen
        self.Screen.show()

        #Scroll history to the last line (need to be called AFTER shwoing gamewindow)
        last_widget = self.history.VerticalLayout.itemAt(self.history.VerticalLayout.count()-1).widget() 
        self.history.scrollArea.ensureWidgetVisible(last_widget)

    def displayGameWindow(self):
        """This method defines all properties of window which contains the game"""
        self.Screen = QtWidgets.QWidget() #MyGame_Screen is entire screen which contains all objects (Cards, score etc)
        self.Screen.setObjectName("MyGame_Screen") #Thanks to setObjectName we can configure style for this object by giving its name
        self.Screen.resize(1400, 800) #This dimenshion describes whole game
        self.Screen.setStyleSheet(
            "*{margin: 0; padding: 1px; line-height: 40px;}"
            #"*{border: 1px solid #000; padding: 0;}\n" #Used for show grid while testing card; we have to replace padding because border make the same effect
            "#test{border: 1px solid #F00}" 
            "#MyGame_Screen{background-image: url(images/board.png)}"
            )

    def displayCard(self, card, target):
        """Defines how and where given card should be displayed"""
        used = card.used
        card_type = card.card_type
        the_list = card.the_list
        
        #define bacground based on card card_type
        bg_images = {"Trade":"tradecard", "Upgrade":"upgradecard", "Harvest":"harvestcard", "Treasure":"treasurecard"}

        tooltips = {"Trade":"<u><b>Card description</b></u><br>\
            Replaces dies from left side of the card by dies from the right side<br><br> \
            Can be used multiple time (if player have enough dies)",
            "Upgrade":"<u><b>Card description</b></u><br>\
            Upgrades specific amount of dies according to rules displayed on the card)",
            "Harvest":"<u><b>Card description</b></u><br>\
            Produces dies when played",
            "Treasure":"<u><b>Card description</b></u><br>\
            You can buy it to get the score",
        }
            

        descriptions = {"Trade":"<u><b>Card description</b></u><br>\
            Replaces left dies with right dies",
            "Upgrade":"<u><b>Card description</b></u><br>\
            Upgrades specific amount of dies",
            "Harvest":"<u><b>Card description</b></u><br>\
            Produces dies when played",
            "Treasure":""
        }

        #CB is space for card and area below reserved for buttons/additional dies/additional money
        self.Whole_Widget = QtWidgets.QWidget()
        self.Whole_Widget.setObjectName("Whole_Widget") #Needed to configure styleSheet
        self.Whole_Widget.resize(120, 200) #This dimenshion describe both, card and buttons below it

        #Inside this container we have WholeLayout which separates card and stuff from below into 2 elements
        self.Whole_VerticalLayout = QtWidgets.QVBoxLayout(self.Whole_Widget)
        self.Whole_VerticalLayout.setSpacing(0)
        self.Whole_VerticalLayout.setContentsMargins(0,0,0,0)


        #Create card widget
        self.CardWidget = QtWidgets.QWidget()
        self.CardWidget.setFixedSize(120, 160)
        self.CardWidget.setObjectName("CardWidget")
        self.CardWidget.setStyleSheet(
            f"#CardWidget{{background-image: url(images/{used*'BW'}{bg_images[card_type]}.png); background-repeat: none;}}"
            )

        #Add Tooltip
        self.CardWidget.setToolTip(tooltips[card_type])

        #Add grid which will contains all inputs/outputs
        self.CardGrid = QtWidgets.QGridLayout(self.CardWidget) #Create grid inside CardWidget
        self.CardGrid.setHorizontalSpacing(20)
        self.CardGrid.setVerticalSpacing(2)

        #Fill the card grid basing on card_type
        self.fillGrid(the_list, descriptions, card_type)

        #Add CardWidget to Whole_Vertical layout which contains card and buttons/extra content
        self.Whole_VerticalLayout.addWidget(self.CardWidget)

        ###################################################################################
        #
        #Replacing mouseRelaseEvent with my function. 
        #it's a little weird because event is not triggering while click on description
        #but works while clicking on something else
        
        #print(self.Whole_Widget)
        self.CardWidget.mouseReleaseEvent=partial(self.takeCard, target, self.Whole_Widget)
        #
        ###################################################################################
        
        #Add Whole_Widget to target layout in the game window
        target.addWidget(self.Whole_Widget)
        print(target.indexOf(self.Whole_Widget))
        
    ###################################################################################
    #
    def takeCard(self, target, WholeWidget, event):
        #print('widget removed')
        #print(target)
        #print(target.itemAt(1))
        #print(target.indexOf(WholeWidget)) #Not working with self.Whole_Widget
        #WholeWidget.hide()

        self.playerHand.HorizontalLayout.addWidget(WholeWidget)
        self.playerHand.scrollAreaWidgetContents.resize(self.playerHand.scrollAreaWidgetContents.width()+130, self.playerHand.scrollAreaWidgetContents.height())

        #target.removeWidget(WholeWidget)

    #
    ###################################################################################

    def fillGrid(self, the_list, descriptions, card_type):
        if card_type == 'Trade' or card_type == 'Harvest':
            for row in range (0, 5):
                for column in range (0,2):
                    #Add all inputs and outputs to the grid
                    element = QtWidgets.QLabel()
                    element.setText = ""
                    if the_list[column][row] != "":
                        element.setStyleSheet(
                            f"background-image: url(images/{the_list[column][row]}.png);"
                            "background-repeat: none; "
                            "background-position: center;"
                            )
                    self.CardGrid.addWidget(element, row, column)

            #Add description
            self.description = QLabel(descriptions[card_type])
            #description.setTextFormat(QtCore.Qt.RichText) #In my version of python this line is no needed (it detects html automatically)
            self.description.setWordWrap(True)
            self.description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.description.setObjectName("description")
            self.description.setFixedHeight(60)
            self.description.setStyleSheet("*{font-size:10px; padding-top: 11px;}")
            self.CardGrid.addWidget(self.description, 7, 0, 1, 2) #row, column, how many rows, how many columns

        if card_type == 'Upgrade':
            #add first input to two first fields in the grid
            element = QtWidgets.QLabel()
            element.setText = ""
            element.setStyleSheet(
                f"background-image: url(images/{the_list[0][0]}.png);"
                "background-repeat: none; "
                "background-position: center;"
                )
            self.CardGrid.addWidget(element, 0, 0, 2, 1)

            #Fill the grid with empty labels
            for row in range (0, 5):
                for column in range (0,2):
                    if row <=1 and column == 0: continue
                    element = QtWidgets.QLabel()
                    element.setText = ""

                    self.CardGrid.addWidget(element, row, column)

            #Add description
            self.description = QLabel(descriptions[card_type])
            #description.setTextFormat(QtCore.Qt.RichText) #In my version of python this line is no needed (it detects html automatically)
            self.description.setWordWrap(True)
            self.description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.description.setObjectName("description")
            self.description.setFixedHeight(60)
            self.description.setStyleSheet("*{font-size:10px; padding-top: 11px;}")
            self.CardGrid.addWidget(self.description, 7, 0, 1, 2) #row, column, how many rows, how many columns

    def img(self, file_name, height=10, widht=10):
        return f'<img src="images/{file_name}.png" height="{height}", wdith="{widht}">'

    def addToHistory(self, note_type='custom'):
            if note_type=='custom':
                now = datetime.datetime.now()
                qtemp = QtWidgets.QLabel(f'<font color=\"blue\">[{now.hour:02d}:{now.minute:02d}:{now.second:02d}]</font> \
                    [Player{x}] has played [Trade] card [1 times].<br> \
                        Player traded [1{self.img("k1")}, 1{self.img("k2")}, 1{self.img("k3")}, 1{self.img("k4")}] for [3{self.img("k1")}, 3{self.img("k4")}]')
                self.history.VerticalLayout.addWidget(qtemp)
                self.history.scrollAreaWidgetContents.resize(self.history.scrollAreaWidgetContents.width(), self.history.scrollAreaWidgetContents.height()+30)
                