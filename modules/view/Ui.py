from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets


import datetime

from modules.view.ScrollBox import ScrollBox
from modules.view.img import img
from modules.controller.add_to_history import add_to_history



class Ui:
    from modules.view.display_game_window import display_game_window
    from modules.view.display_card import display_card
    from modules.view.display_card import fill_grid
    from modules.view.add_text_label import add_text_label
    from modules.view.player_box import player_box
    from modules.controller.cards_actions import move_card
    """Class responsible for management of graphic interface of Game"""
    def __init__(self, Game):
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
            x_pos=700, y_pos=145, height=164, prefix='BuyableStore')
        #buyable
        self.PlayableStore = ScrollBox(parentWidget=self.Screen, cards_cnt=6, \
            x_pos=570, y_pos=350, height=200, prefix='PlayableStore')
        #player hand
        self.PlayerHand = ScrollBox(parentWidget=self.Screen, cards_cnt=8, \
            x_pos=308, y_pos=565, height=210, prefix='PlayerHand', scrollbox_type='PlayerHand')

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

        #Display information about extra coins
        self.GoldCoinsLabel = self.add_text_label(content=f'<center>+ GOLD COIN  <br>({Game.gold_coins_counter} left)</center>', x_pos=1240, y_pos=311, font_size=12, font_weight=600 ,custom_style_sheet='background-color:#b38b79; border: 1px solid black;  border-radius:8; padding:3px 8px 3px 6px')
        self.SilverCoinsLabel = self.add_text_label(content=f'<center>+ SILVER COIN<br>({Game.silver_coins_counter} left)</center>', x_pos=1105, y_pos=311, font_size=12, font_weight=600 ,custom_style_sheet='background-color:#b38b79; border: 1px solid black; border-radius:8; padding:3px 4px 3px 3px')

        #Filling the history with something for tests
        HTMLtext = (f'has played [Trade] card [1 times].<br> \
                Player traded [1{img("k1")}, 1{img("k2")}, 1{img("k3")}, 1{img("k4")}] for [3{img("k1")}, 3{img("k4")}]')
        for x in range(1, 22):
            add_to_history(history=self.history, HTMLtext=HTMLtext)

        #show screen
        self.Screen.show()



