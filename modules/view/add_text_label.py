from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

def add_text_label(self, content, x_pos=0, y_pos=0, font_color='black', font_size='15', font_weight='bold', custom_style_sheet=''):
    """Method used for adding textlabel on Game screen. Needs to be called before main screen is showed"""
    qtemp = QtWidgets.QLabel(f'{content}')
    qtemp.setStyleSheet(f"*{{font-size:{font_size}px; font-weight: {font_weight}; color: {font_color}; {custom_style_sheet}}}")
    qtemp.move(x_pos, y_pos)
    qtemp.setParent(self.Screen)