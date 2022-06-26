from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

from functools import partial

from modules.view.ScrollBox import ScrollBox
from modules.view.img import img
from modules.controller.add_to_history import add_to_history
from modules.controller.rest import rest



class Ui:
    from modules.view.display_game_window import display_game_window
    from modules.view.display_card import display_card
    from modules.view.display_card import fill_grid
    from modules.view.add_text_label import add_text_label
    from modules.view.player_box import player_box
    from modules.controller.cards_actions import move_card
    from modules.controller.game_record import game_record
    """Class responsible for management of graphic interface of Game"""
    def __init__(self, Game):
        self.Game = Game

        #Game window
        self.display_game_window()

        #Show players boxes
        self.player_box(Player=self.Game.players_list[0] ,x_pos=10, y_pos=565)

        for x in Game.players_list:
            try:
                if x.player_number == 0: continue
                self.player_box(x ,x_pos=1112-(x.player_number-1)*262, y_pos=10)

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
        for Card in Game.playable_store_cards_list:
            self.display_card(Card=Card, Target=self.PlayableStore.HorizontalLayout)

        for Card in Game.buyable_store_cards_list:
            self.display_card(Card=Card, Target=self.BuyableStore.HorizontalLayout)

        #Display cards in player hand
        for Card in Game.players_list[0].player_hand:
            self.display_card(Card=Card, Target=self.PlayerHand.HorizontalLayout)
        #Resize playerhand scrollbox (this have not fixed size)
        self.PlayerHand.ScrollAreaWidgetContents.resize(130*len(Game.players_list[0].player_hand), self.PlayerHand.ScrollAreaWidgetContents.height())

        #Display "Current Player"
        self.add_text_label(content='Current turn:', x_pos=10, y_pos=5)
        self.add_text_label(content=f'{self.Game.players_list[self.Game.current_player_no].name}', x_pos=10, y_pos=20)
        
        #Display history box
        self.add_text_label(content='History:', x_pos=10, y_pos=125)
        self.history = ScrollBox(parentWidget=self.Screen, cards_cnt=4, \
            x_pos=10, y_pos=145, height=405, scrollbox_type='history', prefix='history')
        self.history.ScrollAreaWidgetContents.resize(self.history.ScrollAreaWidgetContents.width(), 20)

        #Display information about extra coins
        self.GoldCoinsLabel = self.add_text_label(content=f'<center>+ GOLD COIN  <br>({Game.gold_coins_counter} left)</center>', x_pos=1240, y_pos=311, font_size=12, font_weight=600 ,custom_style_sheet='background-color:#b38b79; border: 1px solid black;  border-radius:8; padding:3px 8px 3px 6px')
        self.SilverCoinsLabel = self.add_text_label(content=f'<center>+ SILVER COIN<br>({Game.silver_coins_counter} left)</center>', x_pos=1105, y_pos=311, font_size=12, font_weight=600 ,custom_style_sheet='background-color:#b38b79; border: 1px solid black; border-radius:8; padding:3px 4px 3px 3px')

        #show player action buttons
        self.add_text_label(content='Player actions:', x_pos=10, y_pos=720)
        Rest_Button = QtWidgets.QPushButton(text='Rest', parent=self.Screen, toolTip='Change state of all player cards to "unused"')
        Rest_Button.move(10, 750)
        Rest_Button.resize(140, 40)
        Rest_Button.clicked.connect(partial(rest, Game, self))

        #We're crating transparet poup fo player will be unable to press outsite dhe popup when to close it (when he have too much resources)
        self.Blocker_Widget = QtWidgets.QWidget(self.Screen)
        self.Blocker_Widget.setStyleSheet('background-color: transparent')
        self.Blocker_Widget.setFixedSize(1400, 800)
        self.Blocker_Widget.hide()

        #show screen
        self.Screen.show()

        #Make note about initialization
        add_to_history(Ui=self, HTMLtext='Ui has been created')

        #Read current game record and print it to history
        Game.record = self.game_record(update=False)

        #Display current record
        self.Game.turn_no += 1


