import sys
from functools import partial
from modules.controller.add_to_history import add_to_history
from modules.controller.take_card import *


class Controller:
    def __init__(self, Game, Ui):
        self.Game = Game
        self.Ui = Ui

        #######################Game start:
        #Make initial note in game history
        for x in range(0, 5):
            add_to_history(history=Ui.history, HTMLtext='The game has been started')

        #Add onclick event to playable cards in stole  
        for x in range(0, Ui.playableStore.HorizontalLayout.count()):
            self.playable_controller(card_number=x)

        # #Add onclick event to buyable cards in stole  
        for x in range(0, Ui.buyableStore.HorizontalLayout.count()):
            self.buyable_controller(card_number=x)

    def _check_refferences(self, WholeWidget, CardWidget):
        #Check if refferences are correct
        if WholeWidget.objectName()!='WholeWidget':
            print(f'\nREFERENCE ERROR!\nWe expected to refer widget with objectName="WholeWidget"\n' \
                    f'Widget with objectName="{WholeWidget.objectName()}" was reffered instead')
            sys.exit()
        
        if CardWidget.objectName()!='CardWidget':
            print(f'\nREFERENCE ERROR!\nWe expected to refer widget with objectName="CardWidget"\n' \
                    f'Widget with objectName="{CardWidget.objectName()}" was reffered instead')
            sys.exit()

    def playable_controller(self, card_number):
        #Find widgets for card with specific number on playablestore layout
        WholeWidget = self.Ui.playableStore.HorizontalLayout.itemAt(card_number).widget()
        CardWidget = self.Ui.playableStore.HorizontalLayout.itemAt(card_number).widget().children()[1]

        #check if references are correct
        self._check_refferences(WholeWidget=WholeWidget, CardWidget=CardWidget)

        #Replacing mouseRelaseEvent with my function. ATM it isn't triggering while click on description part
        CardWidget.mouseReleaseEvent=partial(take_playable_card, WholeWidget, CardWidget, self.Ui,  self.Game)


    def buyable_controller(self, card_number):
        #Find widgets for card with specific number on buyable layout
        WholeWidget = self.Ui.buyableStore.HorizontalLayout.itemAt(card_number).widget()
        CardWidget = self.Ui.buyableStore.HorizontalLayout.itemAt(card_number).widget().children()[1]

        #check if references are correct
        self._check_refferences(WholeWidget=WholeWidget, CardWidget=CardWidget)

        #Replacing mouseRelaseEvent with my function. ATM it isn't triggering while click on description part
        CardWidget.mouseReleaseEvent=partial(buy_card, WholeWidget, CardWidget, self.Ui, self.Game)

