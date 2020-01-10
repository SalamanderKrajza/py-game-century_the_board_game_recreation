from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.img import img

def player_box(self, player, x_pos, y_pos, width=240, height=130):
    """Method used for adding area which displays player points and resources"""
    PlayerBoxWidget = QtWidgets.QWidget(self.Screen)
    PlayerBoxWidget.setObjectName(f'player_{player.no}_box')
    PlayerBoxWidget.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
    PlayerBoxWidget.setStyleSheet(
        f"#player_{player.no}_box{{background-color: #b38b79; border: 1px solid black}}"
    )

    style = {"bigger_label":"font-size:17px; font-weight: bold; color: black", \
            "smaller_label":"font-size:13px; font-weight: bold; color: black"}

    VerticalLayout = QtWidgets.QVBoxLayout(PlayerBoxWidget)
    VerticalLayout.setSpacing(2)
    VerticalLayout.setContentsMargins(0,10,0,10)


    def SingleLine(row, style, left_label_content, right_label_content):
        #left side
        HorizontalLayout = QtWidgets.QHBoxLayout()
        VerticalLayout.addLayout(HorizontalLayout)
        TempLabel = QtWidgets.QLabel(left_label_content)
        TempLabel.setStyleSheet(style)
        TempLabel.setFixedWidth(80)
        TempLabel.setObjectName(f'{row}-LEFT')
        HorizontalLayout.addWidget(TempLabel)

        #right side
        TempLabel = QtWidgets.QLabel(right_label_content)
        TempLabel.setStyleSheet(style)
        TempLabel.setObjectName(f'{row}-RIGHT')
        HorizontalLayout.addWidget(TempLabel)

    points = 5

    #ROW1 player_name - total_points
    SingleLine(row=1, style=style['bigger_label'], \
        left_label_content=f'{player.name}', \
        right_label_content=f'{player.total_points} POINTS TOTAL')

    #ROW2 RICHES: [amount/maximum] (riches_points)
    SingleLine(row=2, style=style['smaller_label'], \
        left_label_content='RICHES:', \
        right_label_content=f'[{player.riches_count:2} /{self.Game.riches_maximum:2} ] ({player.riches_points} POINTS)')

    #ROW3 COINS: [gold, silver] (coins_points)
    SingleLine(row=3, style=style['smaller_label'], \
        left_label_content='COINS:', \
        right_label_content=f'[{player.coins_gold}G, {player.coins_silver}S] ({player.coins_points} POINTS)')

    #ROW4 STORAGE: [amount/maximum] (storage_points)
    SingleLine(row=4, style=style['smaller_label'], \
        left_label_content='STORAGE:', \
        right_label_content=f'[{player.resources_count:02}/10] ({player.resources_points} POINTS)')

    #ROW5 images of resources
    TempWidget = QtWidgets.QWidget() #We created widget to easier reference
    TempWidget.setObjectName('ResourcesRow')
    VerticalLayout.addWidget(TempWidget)

    TempLabel = QtWidgets.QLabel(f'[ \
        {player.resources.count("k1")} {img(file_name="k1", width=14, height=16)}| \
        {player.resources.count("k2")} {img(file_name="k2", width=14, height=16)}| \
        {player.resources.count("k3")} {img(file_name="k3", width=14, height=16)}| \
        {player.resources.count("k4")} {img(file_name="k4", width=14, height=16)} ]')
    TempLabel.setStyleSheet(style['bigger_label'])
    TempLabel.setParent(TempWidget)

