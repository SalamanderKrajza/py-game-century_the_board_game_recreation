from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

class ScrollBox:
    """Class which helps creating new ScrollBoxes on the gamescreen. It also keeps all related properties"""
    def __init__(self, parentWidget, cards_cnt, left_margin, top_margin, height, scrollbox_type='standard'):
        #Create outer area
        self.scrollArea = QtWidgets.QScrollArea(parentWidget)
        self.scrollArea.setGeometry(QtCore.QRect(left_margin, top_margin, 130*cards_cnt+2, height))
        self.scrollArea.setObjectName("scrollArea")

        #Create inner area
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        if scrollbox_type == 'history':
            #Create vertical layout (prepard for history) so we can add cards later
            self.VerticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
            self.VerticalLayout.setSpacing(2)
            self.VerticalLayout.setContentsMargins(0,0,0,0)
            self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.scrollAreaWidgetContents.setObjectName("historyAreaWidgetContents")
            self.scrollArea.setObjectName("historyArea")
        else:
            #Create layout so we can add cards later
            self.HorizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
            self.HorizontalLayout.setSpacing(10)
            self.HorizontalLayout.setContentsMargins(0,0,0,0)
            self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        

        #Resize innerContent
        self.scrollAreaWidgetContents.resize(130*cards_cnt-2, height)