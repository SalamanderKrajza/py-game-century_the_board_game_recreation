from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets


import datetime

from modules.view.ScrollBox import ScrollBox
from modules.view.img import img
from modules.controller.add_to_history import add_to_history



class Ui:
    """Class responsible for management of graphic interface of Game"""
    from modules.view.display_game_window import display_game_window
    from modules.view.display_card import display_card
    from modules.view.display_card import fill_grid
    from modules.view.add_text_label import add_text_label
    from modules.view.player_box import player_box


    def __init__(self, Game):
        pass
        self.Game = Game

        #Game window
        self.display_game_window()

        #Show players boxes
        self.player_box(Player=self.Game.players[0] ,x_pos=10, y_pos=600)

        for x in Game.players:
            try:
                if x.no == 0: continue
                self.player_box(x ,x_pos=1112-(x.no-1)*262, y_pos=10)

            except:
                print ('There was fail with displaying player box. Probably one of players was not created.')
        
        #Prepare space to contain cards
        #playable
        self.BuyableStore = ScrollBox(parentWidget=self.Screen, cards_cnt=5, \
            x_pos=700, y_pos=150, height=200, prefix='BuyableStore')
        #buyable
        self.PlayableStore = ScrollBox(parentWidget=self.Screen, cards_cnt=6, \
            x_pos=570, y_pos=355, height=200, prefix='PlayableStore')
        #player hand
        self.PlayerHand = ScrollBox(parentWidget=self.Screen, cards_cnt=8, \
            x_pos=300, y_pos=570, height=220, prefix='playerHand')

        #Display cards in storages        
        for Card in Game.playable_store_cards:
            self.display_card(Card=Card, Target=self.PlayableStore.HorizontalLayout)

        for Card in Game.buyable_store_cards:
            self.display_card(Card=Card, Target=self.BuyableStore.HorizontalLayout)

        #Display cards in player hand
        for Card in Game.players[0].player_hand:
            self.display_card(Card=Card, Target=self.PlayerHand.HorizontalLayout)
        #Resize playerhand scrollbox (this have not fixed size)
        self.PlayerHand.ScrollAreaWidgetContents.resize(130*len(Game.players[0].player_hand), self.PlayerHand.ScrollAreaWidgetContents.height())

        #Display "Current Player"
        self.add_text_label(content='Current turn:', x_pos=10, y_pos=5)
        self.add_text_label(content=f'{self.Game.players[self.Game.current_player_no].name}', x_pos=10, y_pos=20)
        
        #Display history box
        self.add_text_label(content='History:', x_pos=10, y_pos=125)
        self.history = ScrollBox(parentWidget=self.Screen, cards_cnt=4, \
            x_pos=10, y_pos=150, height=370, scrollbox_type='history', prefix='history')
        self.history.ScrollAreaWidgetContents.resize(self.history.ScrollAreaWidgetContents.width(), 20)

        #Filling the history with something for tests
        HTMLtext = (f'has played [Trade] card [1 times].<br> \
                Player traded [1{img("k1")}, 1{img("k2")}, 1{img("k3")}, 1{img("k4")}] for [3{img("k1")}, 3{img("k4")}]')
        for x in range(1, 22):
            add_to_history(history=self.history, HTMLtext=HTMLtext)

        #show screen
        self.Screen.show()



