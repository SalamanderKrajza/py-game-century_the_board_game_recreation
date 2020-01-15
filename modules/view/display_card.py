
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.img import img

from PyQt5.QtWidgets import QStyleOption, QStyle
from PyQt5.QtGui import QPainter
from modules.view.dictionaries import bg_images, tooltips, descriptions




class CardWidget(QtWidgets.QWidget):
    """We want to let card widget hold some additional variables about itself"""
    def __init__(self, Card, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.Card = Card
        self.BelowCardWidget_PlayerHand = 'This will be replaced with widget'
        self.BelowCardWidget_PlayableStore ='This will be replaced with widget'

    def paintEvent(self, event):
        #Subclasses from QWidget loses their ability to use StyleSheets
        #In order to use the StyleSheets you need to provide a paintEvent to the custom widget.
        #This part of code is based on https://stackoverflow.com/questions/2565963/pyqt4-qwidget-subclass-not-responding-to-new-setstylesheet-background-colour
        opt = QStyleOption()
        #opt.init(self)
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

#This is part of Ui class
def display_card(self, Card, Target, position_in_layout=0, for_popup=False):
    """Defines how and where given card should be displayed"""

    #CB is space for card and area below reserved for buttons/additional dies/additional money
    WholeWidget = QtWidgets.QWidget()
    WholeWidget.setObjectName("WholeWidget") #Needed to configure styleSheet
    WholeWidget.resize(120, 200) #This dimenshion describe both, card and buttons below it

    #Inside this container we have WholeLayout which separates card and stuff from below into 2 Elements
    WholeVerticalLayout = QtWidgets.QVBoxLayout(WholeWidget)
    WholeVerticalLayout.setSpacing(0)
    WholeVerticalLayout.setContentsMargins(0,0,0,0)

    #Create CardWidget
    MyCardWidget = CardWidget(Card)
    MyCardWidget.setFixedSize(120, 160)
    MyCardWidget.setObjectName("CardWidget")
    MyCardWidget.setStyleSheet(
        f"#CardWidget{{background-image: url(images/{Card.used*'BW'}{bg_images[Card.card_type]}.png); background-repeat: none;}}"
        )

    #Add Tooltip
    MyCardWidget.setToolTip(tooltips[Card.card_type])

    #Add grid which will contains all inputs/outputs
    CardGrid = QtWidgets.QGridLayout(MyCardWidget) #Create grid inside CardWidget
    CardGrid.setHorizontalSpacing(20)
    CardGrid.setVerticalSpacing(2)

    #Fill the card grid basing on Card.card_type
    self.fill_grid(Card=Card, CardGrid=CardGrid, descriptions=descriptions)

    #Add CardWidget to Whole_Vertical layout
    WholeVerticalLayout.addWidget(MyCardWidget)


    #Add WholeWidget to Target layout in the Game window
    if Target.parent().parent().objectName() != 'PopupWidget': 
        Target.insertWidget(position_in_layout, WholeWidget)
    else: 
        #For popup we're not adding WholeWidget because we dont need extra container for additional buttons or resources
        Target.insertWidget(position_in_layout, MyCardWidget) 
    
    #After card is created we're adding some space below for buttons/extre content
    #We have 4 possible places when cards can be displayed
    #1. BuyableStore - this dont require any widget which contains something below each rad. 
    # We have some space for silver/gold coins conter, but it have fixed place and isn't connected with card 
    #2. Popup - we're not displaying anything expect the card here
    #3. PlayableStore - Playable cards that player is picking needs widget which will contain resources left on the card 
    MyCardWidget.BelowCardWidget_PlayableStore = QtWidgets.QWidget()
    MyCardWidget.BelowCardWidget_PlayableStore.setObjectName('BelowCard_PlayableStore')
    MyCardWidget.BelowCardWidget_PlayableStore.setFixedHeight(40)
    MyCardWidget.BelowCardWidget_PlayableStore.setStyleSheet('*{background-color: transparent}')
    WholeVerticalLayout.addWidget(MyCardWidget.BelowCardWidget_PlayableStore)
    MyCardWidget.BelowCardWidget_PlayableStore_Label = QtWidgets.QLabel(MyCardWidget.BelowCardWidget_PlayableStore)
    MyCardWidget.BelowCardWidget_PlayableStore_Label.setFixedSize(120, 40)

    #4. PlayerHand - this cards needs some space extra action buttons (Like move card left/right)
    MyCardWidget.BelowCardWidget_PlayerHand = QtWidgets.QWidget()
    MyCardWidget.BelowCardWidget_PlayerHand.setObjectName('BelowCard_PlayerHand')
    MyCardWidget.BelowCardWidget_PlayerHand.setFixedHeight(40)
    MyCardWidget.BelowCardWidget_PlayerHand.setStyleSheet(
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
    WholeVerticalLayout.addWidget(MyCardWidget.BelowCardWidget_PlayerHand)
    #Add layout for extra buttons assigned to card
    BelowCardLayoutForButtons_PlayerHand = QtWidgets.QHBoxLayout(MyCardWidget.BelowCardWidget_PlayerHand)
    BelowCardLayoutForButtons_PlayerHand.setContentsMargins(8,0,8,0)
    #Add buttons:
    MyCardWidget.LeftMoveByButton = QtWidgets.QPushButton()
    MyCardWidget.LeftMoveByButton.setFixedHeight(25)
    MyCardWidget.LeftMoveByButton.setStyleSheet(
                            'background-image: url(images/move_by_left.png);'
                            'background-repeat: none; '
                            'background-position: center;'
                            )
    MyCardWidget.RightMoveByButton = QtWidgets.QPushButton()
    MyCardWidget.RightMoveByButton.setFixedHeight(25)
    MyCardWidget.RightMoveByButton.setStyleSheet(
                            'background-image: url(images/move_by_right.png);'
                            'background-repeat: none; '
                            'background-position: center;'
                            )
    MyCardWidget.LeftMoveToButton = QtWidgets.QPushButton()
    MyCardWidget.LeftMoveToButton.setFixedHeight(25)
    MyCardWidget.LeftMoveToButton.setStyleSheet(
                            'background-image: url(images/move_to_left.png);'
                            'background-repeat: none; '
                            'background-position: center;'
                            )
    MyCardWidget.RightMoveToButton = QtWidgets.QPushButton()
    MyCardWidget.RightMoveToButton.setFixedHeight(25)
    MyCardWidget.RightMoveToButton.setStyleSheet(
                            'background-image: url(images/move_to_right.png);'
                            'background-repeat: none; '
                            'background-position: center;'
                            )

    BelowCardLayoutForButtons_PlayerHand.addWidget(MyCardWidget.LeftMoveToButton)
    BelowCardLayoutForButtons_PlayerHand.addWidget(MyCardWidget.LeftMoveByButton)
    BelowCardLayoutForButtons_PlayerHand.addWidget(MyCardWidget.RightMoveByButton)
    BelowCardLayoutForButtons_PlayerHand.addWidget(MyCardWidget.RightMoveToButton)


    from functools import partial
    MyCardWidget.LeftMoveByButton.clicked.connect(partial(self.move_card, WholeWidget, -1, 'move_by'))
    MyCardWidget.RightMoveByButton.clicked.connect(partial(self.move_card, WholeWidget, 1, 'move_by'))
    MyCardWidget.LeftMoveToButton.clicked.connect(partial(self.move_card, WholeWidget, -1, 'move_to'))
    MyCardWidget.RightMoveToButton.clicked.connect(partial(self.move_card, WholeWidget, 1, 'move_to'))

    if Target != self.PlayableStore.HorizontalLayout: MyCardWidget.BelowCardWidget_PlayableStore.hide()
    if Target != self.PlayerHand.HorizontalLayout: MyCardWidget.BelowCardWidget_PlayerHand.hide()

    #If we are not creating this card for popup, we should return CardWidget so we can assign event to it
    return MyCardWidget



#This is part of Ui class
def fill_grid(self, Card, descriptions, CardGrid):
        if Card.card_type == 'Trade' or Card.card_type == 'Harvest':
            for row in range (0, 5):
                for column in range (0,2):
                    #Add all inputs and outputs to the grid
                    Element = QtWidgets.QLabel()
                    Element.setText = ""
                    if Card.the_list[column][row] != "":
                        Element.setStyleSheet(
                            f"background-image: url(images/{Card.the_list[column][row]}.png);"
                            "background-repeat: none; "
                            "background-position: center;"
                            )
                    CardGrid.addWidget(Element, row, column)

            #Add description
            Description = QLabel(descriptions[Card.card_type])
            #description.setTextFormat(QtCore.Qt.RichText) #In my version of python this line is no needed (it detects html automatically)
            Description.setWordWrap(True)
            Description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            Description.setObjectName("description")
            Description.setFixedHeight(55)
            Description.setStyleSheet("*{font-size:10px; padding-top: 11px;}")
            CardGrid.addWidget(Description, 7, 0, 1, 2) #row, column, how many rows, how many columns

        if Card.card_type == 'Upgrade':
            #Upgrade cards displays only number which defines amout of dies to upgrade and image of gray die
            UpgradeCardHorizotalLayout = QtWidgets.QHBoxLayout()
            CardGrid.addLayout(UpgradeCardHorizotalLayout, 0, 0, 2, 1)

            #Display the number
            Element = QtWidgets.QLabel()
            Element.setFixedSize(20, 20)
            Element.setText(f'{Card.the_list[0][0]}')
            Element.setStyleSheet(
                "font-size:12px; font-weight: bold;"
                "padding-left: 5px;"
                )
            UpgradeCardHorizotalLayout.addWidget(Element)

            #Display the image of gray die
            Element = QtWidgets.QLabel()
            Element.setText('')
            Element.setStyleSheet(
                f"background-image: url(images/k5.png);"
                "background-repeat: none; "
                "margin-top: 3px"
            )
            UpgradeCardHorizotalLayout.addWidget(Element)

            #Then we need empty label to separate first Element from description
            Element = QtWidgets.QLabel()
            Element.setFixedHeight(80)
            CardGrid.addWidget(Element)


            #And finally we'rea dding description
            Description = QLabel(descriptions[Card.card_type])
            #description.setTextFormat(QtCore.Qt.RichText) #In my version of python this line is no needed (it detects html automatically)
            Description.setWordWrap(True)
            Description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            Description.setObjectName("description")
            Description.setFixedHeight(45)
            Description.setStyleSheet("font-size:10px")
            CardGrid.addWidget(Description, 7, 0, 1, 2) #row, column, how many rows, how many columns


        if Card.card_type == 'Treasure':
            #Treasure cards displays amount of points they're giving to their owner
            Element = QtWidgets.QLabel()
            Element.setFixedWidth(35)
            Element.setText(f'{Card.points}')
            Element.setStyleSheet(
                "font-size:12px; font-weight: bold;"
                "padding-left: 8px;"
                )
            CardGrid.addWidget(Element, 0, 0)

            #Then we need empty label to separate first Element from description
            Element = QtWidgets.QLabel()
            Element.setFixedSize(105, 90)
            CardGrid.addWidget(Element, 1, 0)
            CardGrid.setHorizontalSpacing(1)
            
            for x in range(0, 6):
                Element = QtWidgets.QLabel('')
                Element.setFixedWidth(16)
                Element.setObjectName("bigger_labels")
                if Card.the_list[0][x]!='':
                    Element.setStyleSheet(
                        f"background-image: url(images/{Card.the_list[0][x]}.png);"
                        "background-repeat: none; "
                        "background-position: center;"
                    )
                CardGrid.addWidget(Element, 2, x)
