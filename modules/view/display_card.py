
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
def display_card(self, card, target):
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
    self.fill_grid(the_list, descriptions, card_type)

    #Add CardWidget to Whole_Vertical layout which contains card and buttons/extra content
    self.Whole_VerticalLayout.addWidget(self.CardWidget)

    ###################################################################################
    #
    #Replacing mouseRelaseEvent with my function. 
    #it's a little weird because event is not triggering while click on description
    #but works while clicking on something else
    
    #print(self.Whole_Widget)
    self.CardWidget.mouseReleaseEvent=partial(self.take_card, target, self.Whole_Widget)
    #
    ###################################################################################
    
    #Add Whole_Widget to target layout in the Game window
    target.addWidget(self.Whole_Widget)
    print(target.indexOf(self.Whole_Widget))
    
def fill_grid(self, the_list, descriptions, card_type):
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
