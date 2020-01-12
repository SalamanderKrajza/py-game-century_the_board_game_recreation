from modules.view.img import img
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets


#This is part of controller class
def action_confirmed(self, WholeWidget, CardWidget, Ui, Game):
    Player = Game.CurrentPlayer

    #print(f'{self}\n{WholeWidget.objectName()}\n{CardWidget.objectName()}')
    print(self.popup_type)


    if self.popup_type == 'Buyable':
        #Increase player Treasure points and Treasure counter
        Player.riches_points += CardWidget.Card.points
        Player.riches_count += 1

        #Check if card have any extra cions and add increase player coins if there was some
        if CardWidget.Card.bonus == 3:
            Player.coins_gold += 1 
        if CardWidget.Card.bonus == 1:
            Player.coins_silver += 1

        CardWidget.Card.bonus = 0
        Player.coins_points = 3 * Player.coins_gold + 1 * Player.coins_silver

        #Remove Card cost from player resources after buying
        for x in CardWidget.Card.the_list[0]:
            if x != '':
                Player.resources.remove(x)

        #Recalculate points and resources in playerBox
        Player.resources_count = len(Player.resources)
        Player.resources_points = Player.resources_count - Player.resources.count('k1') #every  die other than k1 gives 1 point

        #Recalculate total player points
        Player.total_points = Player.resources_points + Player.riches_points + Player.coins_points

        #Update displayed data
        update_player_box(Game=Game, Ui=Ui, Player=Player)

        #We are not keeping BuyableCards in player hand. We need to get information about this card and remove it.
        WholeWidget.deleteLater()

        #We need to hide Popup after action is finished
        self.close_popup()


    if self.popup_type == 'Playable':
        #Increase player Treasure points and Treasure counter
       
        Ui.PlayerHand.HorizontalLayout.insertWidget(999, WholeWidget) 

        #Pick new from the deck to PlayableStore
        Ui.display_card(Card=Game.DeckPlayable.pickOneCard(), Target=Ui.PlayableStore.HorizontalLayout)
        #Assign onclick event to this new card


        Ui.PlayerHand.HorizontalLayout.addWidget(WholeWidget)
        Ui.PlayerHand.ScrollAreaWidgetContents.resize(Ui.PlayerHand.ScrollAreaWidgetContents.width()+130, \
                                                    Ui.PlayerHand.ScrollAreaWidgetContents.height())
       

        #We need to hide Popup after action is finished
        self.close_popup()



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