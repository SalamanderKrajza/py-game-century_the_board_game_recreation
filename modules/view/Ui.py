from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets


import datetime

from modules.view.ScrollBox import ScrollBox

class Ui:
    """Class responsible for management of graphic interface of Game"""
    from modules.view.display_game_window import display_game_window
    from modules.view.display_card import display_card
    from modules.view.display_card import fill_grid
    from modules.view.add_text_label import add_text_label
    from modules.view.player_box import player_box
    from modules.view.img import img
    from modules.controller.take_card import take_card
    from modules.controller.add_to_history import add_to_history
    def __init__(self, Game):
        pass
        self.Game = Game

        #Game window
        self.display_game_window()

        #Show players boxes
        self.player_box(player=self.Game.players[0] ,left_margin=10, top_margin=600)
        self.player_box(player=self.Game.players[1] ,left_margin=10, top_margin=10)
        self.player_box(player=self.Game.players[2] ,left_margin=280, top_margin=10)
        self.player_box(player=self.Game.players[3] ,left_margin=560, top_margin=10)
        
        #Prepare space to contain cards
        #playable
        self.buyableStore = ScrollBox(parentWidget=self.Screen, cards_cnt=5, \
            left_margin=700, top_margin=100, height=170)
        #buyable
        self.playableStore = ScrollBox(parentWidget=self.Screen, cards_cnt=6, \
            left_margin=570, top_margin=280, height=170)
        #player hand
        self.playerHand = ScrollBox(parentWidget=self.Screen, cards_cnt=8, \
            left_margin=300, top_margin=550, height=220)

        #Display cards in storages        
        for card in Game.playable_store_cards:
            self.display_card(card=card, target=self.playableStore.HorizontalLayout)

        for card in Game.buyable_store_cards:
            self.display_card(card=card, target=self.buyableStore.HorizontalLayout)

        #Display cards in player hand
        for card in Game.players[0].playerHand:
            self.display_card(card=card, target=self.playerHand.HorizontalLayout)
        #Resize playerhand scrollbox (this have not fixed size)
        self.playerHand.scrollAreaWidgetContents.resize(130*len(Game.players[0].playerHand), self.playerHand.scrollAreaWidgetContents.height())

        #Display "Current Player"
        self.add_text_label(content='Current turn:', x_pos=10, y_pos=5)
        self.add_text_label(content=f'{self.Game.players[self.Game.current_player_no].name}', x_pos=10, y_pos=20)

        #self.history.scrollAreaWidgetContents.resize(self.history.scrollAreaWidgetContents.width(), self.history.scrollAreaWidgetContents.height()+30)
        
        
        #Display history
        self.add_text_label(content='History:', x_pos=10, y_pos=125)
        self.history = ScrollBox(parentWidget=self.Screen, cards_cnt=4, \
            left_margin=10, top_margin=150, height=370, scrollbox_type='history')
        self.history.scrollAreaWidgetContents.resize(self.history.scrollAreaWidgetContents.width(), 20)

        #Filling the history with something for tests
        for x in range(1, 22):
            self.add_to_history()

        #show screen
        self.Screen.show()

        #Scroll history to the last line (need to be called AFTER shwoing Gamewindow)
        last_widget = self.history.VerticalLayout.itemAt(self.history.VerticalLayout.count()-1).widget() 
        self.history.scrollArea.ensureWidgetVisible(last_widget)


        
