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
    from modules.view.player_box import create_player_box, fill_playerbox_with_content
    from modules.controller.cards_actions import move_card
    from modules.controller.game_record import game_record
    """Class responsible for management of graphic interface of Game"""
    def __init__(self, Game):
        self.Game = Game

        self.define_css_rules_to_style_elements()
        self.display_game_window()

        for Player in Game.players_list:
            PlayerBoxWidget = self.create_player_box(Player=Player)
            self.fill_playerbox_with_content(PlayerBoxWidget=PlayerBoxWidget, Player=Player)

        #Prepare space to display cards
        self.BuyableStore = ScrollBox(parentWidget=self.Screen, cards_cnt=5, \
            x_pos=700, y_pos=145, height=164, prefix='BuyableStore')
        self.PlayableStore = ScrollBox(parentWidget=self.Screen, cards_cnt=6, \
            x_pos=570, y_pos=350, height=200, prefix='PlayableStore')
        self.PlayerHand = ScrollBox(parentWidget=self.Screen, cards_cnt=8, \
            x_pos=308, y_pos=565, height=210, prefix='PlayerHand', scrollbox_type='PlayerHand')

        #Display cards in desired areas        
        for Card in Game.playable_store_cards_list:
            self.display_card(Card=Card, Target=self.PlayableStore.HorizontalLayout)
        for Card in Game.buyable_store_cards_list:
            self.display_card(Card=Card, Target=self.BuyableStore.HorizontalLayout)
        for Card in Game.players_list[0].player_hand:
            self.display_card(Card=Card, Target=self.PlayerHand.HorizontalLayout)


        self.PlayerHand.resize_player_hand_scroll_area(cards_cnt=Game.players_list[0].player_hand)
        self.display_current_player_name()
        self.display_history_box()
        self.display_coins_info()
        self.display_buttons_for_player_actions()


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


    def define_css_rules_to_style_elements(self):
        self.styles = {"bigger_label":"font-size:17px; font-weight: bold; color: black", \
                "smaller_label":"font-size:13px; font-weight: bold; color: black"}

    def display_current_player_name(self):
        """
        It is displayed in top left corner of game window
        """
        self.add_text_label(content='Current turn:', x_pos=10, y_pos=5)
        self.add_text_label(content=f'{self.Game.players_list[self.Game.current_player_no].name}', x_pos=10, y_pos=20)

    def display_history_box(self):
        self.add_text_label(content='History:', x_pos=10, y_pos=125)
        self.history = ScrollBox(parentWidget=self.Screen, cards_cnt=4, \
            x_pos=10, y_pos=145, height=405, scrollbox_type='history', prefix='history')
        self.history.ScrollAreaWidgetContents.resize(self.history.ScrollAreaWidgetContents.width(), 20)

    def display_coins_info(self):
        """
        Displays information about extra coins \n
        Coins are added riches cards closest to right edge and gives extra points
        """
        self.GoldCoinsLabel = self.add_text_label(
            content=f'<center>+ GOLD COIN  <br>({self.Game.gold_coins_counter} left)</center>',
            x_pos=1240, y_pos=311, font_size=12, font_weight=600, 
            custom_style_sheet='background-color:#b38b79; border: 1px solid black;  border-radius:8; padding:3px 8px 3px 6px'
            )

        self.SilverCoinsLabel = self.add_text_label(
            content=f'<center>+ SILVER COIN<br>({self.Game.silver_coins_counter} left)</center>', 
            x_pos=1105, y_pos=311, font_size=12, font_weight=600, 
            custom_style_sheet='background-color:#b38b79; border: 1px solid black; border-radius:8; padding:3px 4px 3px 3px')

    def display_buttons_for_player_actions(self):
        self.add_text_label(content='Player actions:', x_pos=10, y_pos=720)
        Rest_Button = QtWidgets.QPushButton(
            text='Rest', 
            parent=self.Screen, 
            toolTip='Change state of all player cards to "unused"'
        )
        Rest_Button.move(10, 750)
        Rest_Button.resize(140, 40)
        Rest_Button.clicked.connect(partial(rest, self.Game, self))