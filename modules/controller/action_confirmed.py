from modules.view.img import img
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.dictionaries import bg_images


#This is part of popup class
def action_confirmed(self, ClickedWholeWidget, ClickedCardWidget, Ui, Game):
    from modules.controller.take_card import press_the_card
    from functools import partial
    Player = Game.CurrentPlayer

    if self.popup_type == 'BuyableStore':
        #If card is taken from one of two closest to right edge spots, it could contain extra coins.
        self.distance_to_right_edge = ClickedWholeWidget.parent().layout().count() - ClickedWholeWidget.parent().layout().indexOf(ClickedWholeWidget) - 1
        if self.distance_to_right_edge == 0:
            #This card could have gold coin on it!
            if Game.gold_coins_counter > 0:
                Game.gold_coins_counter -= 1
                ClickedCardWidget.Card.bonus = 3

        elif self.distance_to_right_edge == 1:
            #This card could have silver coin on it!
            if Game.silver_coins_counter > 0:
                Game.silver_coins_counter -= 1
                ClickedCardWidget.Card.bonus = 1

        #Display information about extra coins
        Ui.GoldCoinsLabel.setText(f'<center>+ GOLD COIN  <br>({Game.gold_coins_counter} left)</center>')
        Ui.SilverCoinsLabel.setText(f'<center>+ SILVER COIN<br>({Game.silver_coins_counter} left)</center>')

        #Increase player Treasure points and Treasure counter
        Player.riches_points += ClickedCardWidget.Card.points
        Player.riches_count += 1

        #Check if card have any extra cions and add increase player coins if there was some
        if ClickedCardWidget.Card.bonus == 3:
            Player.coins_gold += 1 
        if ClickedCardWidget.Card.bonus == 1:
            Player.coins_silver += 1
        ClickedCardWidget.Card.bonus = 0
        Player.coins_points = 3 * Player.coins_gold + 1 * Player.coins_silver

        #Remove Card cost from player resources after buying
        for x in ClickedCardWidget.Card.the_list[0]:
            if x != '':
                Player.resources.remove(x)

        #Recalculate points and resources in playerBox
        Player.resources_count = len(Player.resources)
        Player.resources_points = Player.resources_count - Player.resources.count('k1') #every  die other than k1 gives 1 point

        #Recalculate total player points
        Player.total_points = Player.resources_points + Player.riches_points + Player.coins_points

        #Pick new from the deck to PlayableStore
        NewCardWidget = Ui.display_card(Card=Game.DeckBuyable.pickOneCard(), Target=Ui.BuyableStore.HorizontalLayout)

        #Assign onclick event to this new card        
        NewCardWidget.mouseReleaseEvent=partial(press_the_card, NewCardWidget.parent(), NewCardWidget, Ui,  Game, self)

        #We are not keeping BuyableCards in player hand. We need to get information about this card and remove it.
        ClickedWholeWidget.deleteLater()



    TempCardPosition = len(Ui.PlayableStore.HorizontalLayout)-1
    if self.popup_type == 'PlayableStore':
        for x in self.resources_to_thorw_out:
            #TempCardWidget represents each card which is gaining resources
            TempCardWidget=Ui.PlayableStore.HorizontalLayout.itemAt(TempCardPosition).widget().children()[1]
            TempCardPosition -= 1

            #We're removing one of dies choosen by player
            Player.resources.remove(x)

            #We're adding this die to specific Card
            TempCardWidget.BelowCardWidget_PlayableStore_Label.setText('')
            TempCardWidget.Card.resources.append(x)
            for x in ['k1', 'k2', 'k3', 'k4']:
                counter = TempCardWidget.Card.resources.count(x)
                if counter:
                    TempCardWidget.BelowCardWidget_PlayableStore_Label.setText(
                        f'{TempCardWidget.BelowCardWidget_PlayableStore_Label.text()}'
                        f'{counter} {img(file_name=x, width=14, height=16)}'
                        '|'
                        )

        #Add clicked card to PlayerHand scrollbox
        Ui.PlayerHand.HorizontalLayout.insertWidget(999, ClickedWholeWidget) 

        #Add its resources to player 
        for die_to_pickup in ClickedCardWidget.Card.resources:
            Player.resources.append(die_to_pickup)
        
        #Hide BelowCard area prepared for PlayableStore and show the one created for PlayerHand
        ClickedCardWidget.BelowCardWidget_PlayableStore.hide()
        ClickedCardWidget.BelowCardWidget_PlayerHand.show()

        #Pick new from the deck to PlayableStore
        NewCardWidget = Ui.display_card(Card=Game.DeckPlayable.pickOneCard(), Target=Ui.PlayableStore.HorizontalLayout)

        #Assign onclick event to this new card        
        NewCardWidget.mouseReleaseEvent=partial(press_the_card, NewCardWidget.parent(), NewCardWidget, Ui,  Game, self)

        #Add picked card to PlayerHand
        Ui.PlayerHand.HorizontalLayout.addWidget(ClickedWholeWidget)
        Ui.PlayerHand.ScrollAreaWidgetContents.resize(Ui.PlayerHand.ScrollAreaWidgetContents.width()+130, \
                                                    Ui.PlayerHand.ScrollAreaWidgetContents.height())
    if self.popup_type == 'Harvest':
        for x in ClickedCardWidget.Card.the_list[0]:
            if x != '':
                Player.resources.append(x)

    if self.popup_type == 'Trade':
        #Repeat Y times (Y is based on multiplier choosen by player)
        for y in range(0, self.multiplier):
            #Remove card cost from player resources
            for x in ClickedCardWidget.Card.the_list[0]:
                if x != '':
                    Player.resources.remove(x)
            for x in ClickedCardWidget.Card.the_list[1]:
                #Add card income to player resources
                if x != '':
                    Player.resources.append(x)

    if self.popup_type == 'Upgrade':
        #Remove card cost from player resources
        for x in self.resources_to_thorw_out:
            if x != '':
                Player.resources.remove(x)
        for x in self.upgraded_resources:
            #Add card income to player resources
            if x != '':
                Player.resources.append(x)

    #turn card into gray after its take effect
    if self.popup_type in ['Harvest', 'Upgrade', 'Trade']:
        ClickedCardWidget.Card.used = True
        ClickedCardWidget.setStyleSheet(
        f"#CardWidget{{background-image: url(images/{ClickedCardWidget.Card.used*'BW'}{bg_images[ClickedCardWidget.Card.card_type]}.png); background-repeat: none;}}"
        )
    
    #We need to hide Popup after action is finished
    self.close_popup()

    #Update displayed data
    update_player_box(Game=Game, Ui=Ui, Player=Player)

    #Before end of the turn we should check if player have not maximum amount of dies
    self.check_player_resources()

    #Before end of the turn we should check if player hasn't surpass maximum amount of riches
    self.check_player_riches()

    #Trigger end of the turn
    self.end_of_the_turn()

def check_player_resources(self):
    """Before end of the turn we have to check if player have not surpass maximum resource limit"""
    pass

def check_player_riches(self):
    """Before end of the turn we have to check if player have not surpass maximum riches limit"""
    pass

def end_of_the_turn(self):
    pass
    # for Player in self.Game.players:
    #     print(f'Current player is: {Player.no}')
    #     print(f'next player is: {next(Player).no}')



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