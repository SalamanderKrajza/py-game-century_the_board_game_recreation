from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
def add_to_history(self, note_type='custom'):
        if note_type=='custom':
            now = datetime.datetime.now()
            qtemp = QtWidgets.QLabel( \
                f'<font color=\"blue\">[{now.hour:02d}:{now.minute:02d}:{now.second:02d}]</font> \
                [Player1] has played [Trade] card [1 times].<br> \
                Player traded [1{self.img("k1")}, 1{self.img("k2")}, 1{self.img("k3")}, 1{self.img("k4")}] for [3{self.img("k1")}, 3{self.img("k4")}]')
            self.history.VerticalLayout.addWidget(qtemp)
            self.history.scrollAreaWidgetContents.resize(self.history.scrollAreaWidgetContents.width(), self.history.scrollAreaWidgetContents.height()+30)
