from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.img import img
from modules.view.Popup import Popup


def check_if_popup_needed(popup_type, WholeWidget):
    if popup_type == 'Harvest':
        #Harvest cards don't have not any requirements to play
        return True
    if popup_type == 'Playable':
        #QuickNote: 
        # WholeWidget.layout())          <- returns layout INSIDE this widget; 
        # WholeWidget.parent().layout()) <- returns layout CONTAINS this widget

        #If we're buying Playable card we need to check how close it is to end of the list
        distance_to_rigth_edge = WholeWidget.parent().layout().count() - WholeWidget.parent().layout().indexOf(WholeWidget) - 1
        if not distance_to_rigth_edge:
            return False

    return True

def press_the_card(WholeWidget, CardWidget, Ui, Game, Popup, event):
    #The parents of Whole Widget are CardWidget->WholeWidget->V/HBoxLayout->ScrollAreaWidgetContents->ScrollArea
    SourceScrollBox = WholeWidget.parent().parent().parent().objectName()
    if SourceScrollBox == 'PlayableStore-ScrollArea':
        popup_type = 'Playable'
    elif SourceScrollBox == 'BuyableStore-ScrollArea': 
        popup_type = 'Buyable'
    elif SourceScrollBox == 'PlayerHand-ScrollArea': 
        popup_type = CardWidget.Card.card_type
    else:
        popup_type = 'unknown'

    CardWidget.Card.popup_type = popup_type

    Player = Game.CurrentPlayer
    
    #In case Player press another card while popup is visible
    Popup.close_popup()

    #
    Popup.configure_popup(popup_type=popup_type, CardWidget=CardWidget, Ui=Ui, Player=Player)

    if check_if_popup_needed(popup_type=popup_type, WholeWidget=WholeWidget):
        #Show popup
        Popup.display_popup()
    else:
        Popup.action_confirmed(WholeWidget, CardWidget, Ui, Game)
        pass

    #Next steps should depends on what happened on popup



