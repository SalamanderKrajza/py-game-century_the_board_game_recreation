from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.img import img
import datetime
def add_to_history(history, who='Game', HTMLtext='', note_type='custom'):
    #get current time
    now = datetime.datetime.now()

    #create label
    Temp = QtWidgets.QLabel( \
        f'<font color=\"blue\">[{now.hour:02d}:{now.minute:02d}:{now.second:02d}]</font> \
        [{who}] {HTMLtext}')

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


        
