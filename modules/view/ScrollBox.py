from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

class ScrollBox:
    """Class which helps creating new ScrollBoxes on the gamescreen. It also keeps all related properties"""
    def __init__(self, parentWidget, cards_cnt, x_pos, y_pos, height, prefix, scrollbox_type='standard'):
        #Create outer area
        self.ScrollArea = QtWidgets.QScrollArea(parentWidget)
        self.ScrollArea.setGeometry(QtCore.QRect(x_pos, y_pos, 130*cards_cnt+2, height))
        self.ScrollArea.setObjectName(f"{prefix}-ScrollArea")

        self.ScrollArea.setStyleSheet(
            f"#{prefix}-ScrollArea{{background-color: #b38b79; border: 1px solid black}}"
            "#ScrollAreaWidgetContents{background-color: #b38b79; }"
            )
        #Create inner area
        self.ScrollAreaWidgetContents = QtWidgets.QWidget()
        self.ScrollAreaWidgetContents.setObjectName("ScrollAreaWidgetContents")
        self.ScrollArea.setWidget(self.ScrollAreaWidgetContents)

        if scrollbox_type == 'history':
            #Create vertical layout (prepard for history) so we can add cards later
            self.VerticalLayout = QtWidgets.QVBoxLayout(self.ScrollAreaWidgetContents)
            self.VerticalLayout.setSpacing(2)
            self.VerticalLayout.setContentsMargins(0,0,0,0)
            self.ScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.ScrollAreaWidgetContents.setObjectName("historyAreaWidgetContents")
            self.ScrollArea.setObjectName("historyArea")
        else:
            #Create layout so we can add cards later
            self.HorizontalLayout = QtWidgets.QHBoxLayout(self.ScrollAreaWidgetContents)
            self.HorizontalLayout.setSpacing(10)
            self.HorizontalLayout.setContentsMargins(0,0,0,0)
            self.ScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        

        #Resize innerContent
        self.ScrollAreaWidgetContents.resize(130*cards_cnt-2, height)