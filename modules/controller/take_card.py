from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.img import img
from modules.view.Popup import Popup

def press_the_card():
    pass


def take_playable_card(WholeWidget, Card_Widget, Ui, Game, event):
    Player = Game.CurrentPlayer

    print('heh')
    print(WholeWidget.parent().parent().parent().objectName())

    #Show popup
    Ui.MyPopup.display_popup()
    Ui.MyPopup.configure_popup(popup_type='Playable', Card=Card_Widget, Ui=Ui, Player=Player)

    #Move card to PlayerHand and resize playerhand
    Ui.PlayerHand.HorizontalLayout.addWidget(WholeWidget)
    Ui.PlayerHand.ScrollAreaWidgetContents.resize(Ui.PlayerHand.ScrollAreaWidgetContents.width()+130, \
                                                    Ui.PlayerHand.ScrollAreaWidgetContents.height())

    #Remove card-picking event after card is picked. At final version it should be replaced with new function
    Card_Widget.mouseReleaseEvent=""

def buy_card(WholeWidget, Card_Widget, Ui, Game, event):
    #First check which player is buying card
    Player = Game.CurrentPlayer

    #Show popup
    Ui.MyPopup.display_popup()
    Ui.MyPopup.configure_popup(popup_type='Treasure', Card=Card_Widget, Ui=Ui, Player=Player)


    Player.riches_points += Card_Widget.Card.points
    Player.riches_count += 1

    if Card_Widget.Card.bonus == 3:
        Player.coins_gold += 1 
    if Card_Widget.Card.bonus == 1:
        Player.coins_silver += 1

    Card_Widget.Card.bonus = 0
    Player.coins_points = 3 * Player.coins_gold + 1 * Player.coins_silver

    # for x in Card_Widget.Card.the_list[0]:
    #     if x != '':
    #         Player.resources.remove(x)


    Player.resources_count = len(Player.resources)
    Player.resources_points = Player.resources_count - Player.resources.count('k1') #every  die other than k1 gives 1 point

    Player.total_points = Player.resources_points + Player.riches_points + Player.coins_points

    update_player_box(Game=Game, Ui=Ui, Player=Player)

    #We are not keeping BuyableCards in player hand. We need to get information about this card and remove it.
    WholeWidget.deleteLater()


def update_player_box(Game, Ui, Player):
    right_label_content = {1:f'{Player.total_points} POINTS TOTAL', \
        2:f'[{Player.riches_count:2} /{Game.riches_maximum:2} ] ({Player.riches_points} POINTS)', \
        3:f'[{Player.coins_gold}G, {Player.coins_silver}S] ({Player.coins_points} POINTS)', \
        4:f'[{Player.resources_count:02}/10] ({Player.resources_points} POINTS)', \
        5:f'[ \
        {Player.resources.count("k1")} {img(file_name="k1", width=14, height=16)}| \
        {Player.resources.count("k2")} {img(file_name="k2", width=14, height=16)}| \
        {Player.resources.count("k3")} {img(file_name="k3", width=14, height=16)}| \
        {Player.resources.count("k4")} {img(file_name="k4", width=14, height=16)} ]'}                    

    #As all players have the objects with the same name inside playerbox, we have to find their box first
    CurrentPlayerBox = Ui.Screen.findChild(QtWidgets.QWidget, f'player_{Player.no}_box')

    for x in range(1,6):
        #as we know CurrentPlayerBox, we now can search for specified row
        RightSideLabel = CurrentPlayerBox.findChild(QtWidgets.QWidget, f'{x}-RIGHT')
        RightSideLabel.setText(right_label_content[x])
