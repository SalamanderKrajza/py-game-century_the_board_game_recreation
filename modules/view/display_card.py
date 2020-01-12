
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.img import img

from PyQt5.QtWidgets import QStyleOption, QStyle
from PyQt5.QtGui import QPainter



class CardWidget(QtWidgets.QWidget):
    """We want to let card widget hold some additional variables about itself"""
    def __init__(self, Card, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.Card = Card

    def paintEvent(self, event):
        #Subclasses from QWidget loses their ability to use StyleSheets
        #In order to use the StyleSheets you need to provide a paintEvent to the custom widget.
        #This part of code is based on https://stackoverflow.com/questions/2565963/pyqt4-qwidget-subclass-not-responding-to-new-setstylesheet-background-colour
        opt = QStyleOption()
        #opt.init(self)
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)


def display_card(self, Card, Target, position_in_layout=0, for_popup=False):
    """Defines how and where given card should be displayed"""
    used = Card.used
    card_type = Card.card_type
    the_list = Card.the_list

    #CB is space for card and area below reserved for buttons/additional dies/additional money
    WholeWidget = QtWidgets.QWidget()
    WholeWidget.setObjectName("WholeWidget") #Needed to configure styleSheet
    WholeWidget.resize(120, 200) #This dimenshion describe both, card and buttons below it

    #Inside this container we have WholeLayout which separates card and stuff from below into 2 Elements
    WholeVerticalLayout = QtWidgets.QVBoxLayout(WholeWidget)
    WholeVerticalLayout.setSpacing(0)
    WholeVerticalLayout.setContentsMargins(0,0,0,0)

    #CardWidgetPart
    #define bacground based on card card_type
    bg_images = {
        "Trade":"tradecard", 
        "Upgrade":"upgradecard", 
        "Harvest":"harvestcard", 
        "Treasure":"treasurecard"}
    tooltips = {
        "Trade":"<u><b>Card description</b></u><br>\
        Replaces dies from left side of the card by dies from the right side<br><br> \
        Can be used multiple time (if player have enough dies)",
        "Upgrade":"<u><b>Card description</b></u><br>\
        Upgrades specific amount of dies according to rules displayed on the card)",
        "Harvest":"<u><b>Card description</b></u><br>\
        Produces dies when played",
        "Treasure":"<u><b>Card description</b></u><br>\
        You can buy it to get the score",
    }
    descriptions = {
        "Trade":"<u><b>Card description</b></u><br>\
        Replaces left dies with right dies",
        "Upgrade":"<u><b>Card description</b></u><br>\
        Upgrades specific amount of dies",
        "Harvest":"<u><b>Card description</b></u><br>\
        Produces dies when played",
        "Treasure":""
    }

    #Create CardWidget
    #MyCardWidget = QtWidgets.QWidget()
    MyCardWidget = CardWidget(Card)
    MyCardWidget.setFixedSize(120, 160)
    MyCardWidget.setObjectName("CardWidget")
    MyCardWidget.setStyleSheet(
        f"#CardWidget{{background-image: url(images/{used*'BW'}{bg_images[card_type]}.png); background-repeat: none;}}"
        )

    #Add Tooltip
    MyCardWidget.setToolTip(tooltips[card_type])

    #Add grid which will contains all inputs/outputs
    CardGrid = QtWidgets.QGridLayout(MyCardWidget) #Create grid inside CardWidget
    CardGrid.setHorizontalSpacing(20)
    CardGrid.setVerticalSpacing(2)

    #Fill the card grid basing on card_type
    self.fill_grid(the_list, descriptions, card_type, Card.points, CardGrid)

    #Add CardWidget to Whole_Vertical layout
    WholeVerticalLayout.addWidget(MyCardWidget)


    #Add WholeWidget to Target layout in the Game window
    Target.insertWidget(position_in_layout, WholeWidget) #inwsert widget replaces addWidget due to its position argument

    #After card is created we're adding some space below for buttons/extre content
    #However, in case we're creating this card for popup, we dont need this!
    if for_popup==True:
        return WholeWidget

    #add anything below cards. It will be replaced later
    BelowCardWidget = QtWidgets.QWidget()
    BelowCardWidget.setFixedHeight(40)
    BelowCardWidget.setStyleSheet('*{background-color: pink}')
    WholeVerticalLayout.addWidget(BelowCardWidget)


    
def fill_grid(self, the_list, descriptions, card_type, points, CardGrid):
        if card_type == 'Trade' or card_type == 'Harvest':
            for row in range (0, 5):
                for column in range (0,2):
                    #Add all inputs and outputs to the grid
                    Element = QtWidgets.QLabel()
                    Element.setText = ""
                    if the_list[column][row] != "":
                        Element.setStyleSheet(
                            f"background-image: url(images/{the_list[column][row]}.png);"
                            "background-repeat: none; "
                            "background-position: center;"
                            )
                    CardGrid.addWidget(Element, row, column)

            #Add description
            Description = QLabel(descriptions[card_type])
            #description.setTextFormat(QtCore.Qt.RichText) #In my version of python this line is no needed (it detects html automatically)
            Description.setWordWrap(True)
            Description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            Description.setObjectName("description")
            Description.setFixedHeight(60)
            Description.setStyleSheet("*{font-size:10px; padding-top: 11px;}")
            CardGrid.addWidget(Description, 7, 0, 1, 2) #row, column, how many rows, how many columns

        if card_type == 'Upgrade':
            #Upgrade cards displays only number which defines amout of dies to upgrade and image of gray die
            UpgradeCardHorizotalLayout = QtWidgets.QHBoxLayout()
            CardGrid.addLayout(UpgradeCardHorizotalLayout, 0, 0, 2, 1)

            #Display the number
            Element = QtWidgets.QLabel()
            Element.setFixedSize(20, 20)
            Element.setText(f'{the_list[0][0]}')
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
            Description = QLabel(descriptions[card_type])
            #description.setTextFormat(QtCore.Qt.RichText) #In my version of python this line is no needed (it detects html automatically)
            Description.setWordWrap(True)
            Description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            Description.setObjectName("description")
            Description.setFixedHeight(45)
            Description.setStyleSheet("font-size:10px")
            CardGrid.addWidget(Description, 7, 0, 1, 2) #row, column, how many rows, how many columns


        if card_type == 'Treasure':
            #Treasure cards displays amount of points they're giving to their owner
            Element = QtWidgets.QLabel()
            Element.setFixedWidth(35)
            Element.setText(f'{points}')
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
                if the_list[0][x]!='':
                    Element.setStyleSheet(
                        f"background-image: url(images/{the_list[0][x]}.png);"
                        "background-repeat: none; "
                        "background-position: center;"
                    )
                CardGrid.addWidget(Element, 2, x)
