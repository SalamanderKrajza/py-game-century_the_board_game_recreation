from modules.controller.add_to_history import add_to_history

def rest(Game, Ui):
    for card_number in range(0, Ui.PlayerHand.HorizontalLayout.count()):
        CardWidget = Ui.PlayerHand.HorizontalLayout.itemAt(card_number).widget().children()[1]
        #Each card have 2 versions of images differ by "BW" prefix (Black and wight is BWname.png, normal is name.png)
        #We are removing 'BW' from stylesheet without changing anything else to change its color to normal again
        CardWidget.setStyleSheet(CardWidget.styleSheet().replace('BW',''))
        CardWidget.Card.used = False
    add_to_history(Ui=Ui, who=Game.CurrentPlayer.name, HTMLtext='has rest<br>All cards has been restored')
    Game.turn_no += 1