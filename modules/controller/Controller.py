import sys
from functools import partial
from modules.controller.add_to_history import add_to_history
from modules.controller.take_card import check_if_popup_needed, press_the_card
from modules.view.Popup import *

class Controller:
    def __init__(self, Game, Ui, Popup):
        self.Game = Game
        self.Ui = Ui
        self.Popup = Popup

        #######################Game start:
        #Make initial note in game history
        for x in range(0, 5):
            add_to_history(history=Ui.history, HTMLtext='The game has been started')

        #Add onclick event to cards in player hand  
        for Layout in [Ui.BuyableStore.HorizontalLayout, Ui.PlayableStore.HorizontalLayout, Ui.PlayerHand.HorizontalLayout]:
            for x in range(0, Layout.count()):
                self.assign_onclick_event_to_card(card_number=x, which_layout=Layout)

    def assign_onclick_event_to_card(self, card_number, which_layout):
        #Find widgets for card with specific number on Playablestore layout
        WholeWidget = which_layout.itemAt(card_number).widget()
        CardWidget = which_layout.itemAt(card_number).widget().children()[1]

        #check if references are correct
        self._check_refferences(WholeWidget=WholeWidget, CardWidget=CardWidget)

        #Replacing mouseRelaseEvent with my function. ATM it isn't triggering while click on description part
        CardWidget.mouseReleaseEvent=partial(press_the_card, WholeWidget, CardWidget, self.Ui,  self.Game, self.Popup)

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
