from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
def take_playable_card(WholeWidget, card_widget, Ui, Game, event):
    Player = Game.current_player
    #print('widget removed')
    #print(Target)
    #print(Target.itemAt(1))
    #print(Target.indexOf(WholeWidget)) #Not working with self.WholeWidget
    #WholeWidget.hide()

    #Return position of clicked widget on HorizontalLayout - needs to be called before moving card (or it will return -1)
    print(Ui.playableStore.HorizontalLayout.indexOf(WholeWidget))

    #Move card to PlayerHand and resize playerhand
    Ui.PlayerHand.HorizontalLayout.addWidget(WholeWidget)
    Ui.PlayerHand.ScrollAreaWidgetContents.resize(Ui.PlayerHand.ScrollAreaWidgetContents.width()+130, \
                                                    Ui.PlayerHand.ScrollAreaWidgetContents.height())

    #Remove card-picking event after card is picked. At final version it should be replaced with new function
    card_widget.mouseReleaseEvent=""

def buy_card(WholeWidget, Card_Widget, Ui, Game, event):
    #First check which player is buying card
    Player = Game.current_player

    #Then check if he have enough resources
    #print(Card_Widget.Card.the_list[0])
    #print(player.resources)

    Player.riches_points += Card_Widget.card.points
    Player.riches_count += 1

    #Looks like findChild searching also inside childs of childs etc. Due to this we don't need going inside step by step.
    # CurrentPlayerBox = Ui.Screen.findChild(QtWidgets.QWidget, f'player_{player.no}_box')
    # row3_right_side = CurrentPlayerBox.findChild(QtWidgets.QWidget, f'3-RIGHT')
    # row3_right_side.setText ('test')


    row2_right_side = Ui.Screen.findChild(QtWidgets.QWidget, f'2-RIGHT')
    row2_right_side.setText(f'[{Player.riches_count:2} /{Game.riches_maximum:2} ] ({Player.riches_points} POINTS)')

    print(type(row2_right_side))
    #We are not keeping BuyableCards in player hand. We need to get information about this card and remove it.
    WholeWidget.deleteLater()