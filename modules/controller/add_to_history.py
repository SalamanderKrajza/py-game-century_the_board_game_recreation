from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.img import img
import datetime

def add_to_history(Ui, who='Game', HTMLtext=''):
    """method which adding new note in history box."""
    history = Ui.history
    Game = Ui.Game 
    #get current time
    now = datetime.datetime.now()

    #create label
    Temp = QtWidgets.QLabel( \
            f'<font color=\"#600\">[{now.hour:02d}:{now.minute:02d}:{now.second:02d}]'
            f'[Turn {Game.turn_no}]'
            f'[{who}] </font>'
            f'{HTMLtext}'
            )

    #add label to history
    history.VerticalLayout.addWidget(Temp)

    #Resize history widget so we can scroll to this label
    lines = HTMLtext.count('<br>')+1
    history.ScrollAreaWidgetContents.resize(history.ScrollAreaWidgetContents.width(), \
                                            history.ScrollAreaWidgetContents.height()+lines*14+2)

    #Scroll history to show your new note
    Temp.show() #Even if qlabel is displayed right after added to layout, without "showing it" scrolling dont work
    history.ScrollArea.ensureWidgetVisible(Temp)

    # Orevious version of scrolling which let us scroll to widget by its number
    # last_widget = self.history.VerticalLayout.itemAt(self.history.VerticalLayout.count()-1).widget() 
    # self.history.ScrollArea.ensureWidgetVisible(last_widget)


        
