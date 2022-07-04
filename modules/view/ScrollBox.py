from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

class ScrollBox:
    """Class which helps creating new ScrollBoxes on the gamescreen. It also keeps all related properties"""
    def __init__(self, parentWidget, cards_cnt, x_pos, y_pos, height, prefix, scrollbox_type='standard'):
        self.geometry_dict = {
            'standard':{
                'width': 130 * cards_cnt + 2,
                'height': height + 2,
            },
            'PlayerHand':{
                'width': 130 * cards_cnt + 2,
                'height': height + 2 + 15,
            },
            'history':{
                'width': 130 * cards_cnt + 2 + 15, 
                'height': height + 2,
            }
        }
        self.create_outer_scrollbox_area(parentWidget, cards_cnt, x_pos, y_pos, height, prefix, scrollbox_type)
        self.create_inner_scrollbox_area(cards_cnt, height, scrollbox_type)

    def create_outer_scrollbox_area(self, parentWidget, cards_cnt, x_pos, y_pos, height, prefix, scrollbox_type):
        self.ScrollArea = QtWidgets.QScrollArea(parentWidget)
        self.ScrollArea.setGeometry(QtCore.QRect(
            x_pos, y_pos, self.geometry_dict[scrollbox_type]['width'], self.geometry_dict[scrollbox_type]['height']))
        self.ScrollArea.setObjectName(f"{prefix}-ScrollArea")
        from modules.view.styles import scrollbox_styles
        self.ScrollArea.setStyleSheet(f"#{prefix}-{scrollbox_styles}")

    def create_inner_scrollbox_area(self, cards_cnt, height, scrollbox_type):
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
        else:
            #Create layout so we can add cards later
            self.HorizontalLayout = QtWidgets.QHBoxLayout(self.ScrollAreaWidgetContents)
            self.HorizontalLayout.setSpacing(10)
            self.HorizontalLayout.setContentsMargins(0,0,0,0)
            self.ScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        #Resize innerContent
        self.ScrollAreaWidgetContents.resize(130 * cards_cnt -4, height-4)

    def resize_player_hand_scroll_area(self, cards_cnt):
        """Resize playerhand scrollbox (this have not fixed size but changes with amount of cards that player has)"""
        self.ScrollAreaWidgetContents.resize(130*len(cards_cnt), self.ScrollAreaWidgetContents.height())