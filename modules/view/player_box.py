from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.img import img

#This is part of Ui class
def player_box(self, Player, x_pos, y_pos, width=240, height=130):
    """Method used for adding area which displays Player points and resources"""
    PlayerBoxWidget = QtWidgets.QWidget(self.Screen)
    PlayerBoxWidget.setObjectName(f'player_{Player.no}_box')
    PlayerBoxWidget.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
    PlayerBoxWidget.setStyleSheet(
        f"#player_{Player.no}_box{{background-color: #b38b79; border: 1px solid black}}"
    )

    styles = {"bigger_label":"font-size:17px; font-weight: bold; color: black", \
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

    #ROW1 Player_name - total_points
    SingleLine(row=1, style=styles['bigger_label'], \
        left_label_content=f'{Player.name}', \
        right_label_content=f'{Player.total_points} POINTS TOTAL')

    #ROW2 RICHES: [amount/maximum] (riches_points)
    SingleLine(row=2, style=styles['smaller_label'], \
        left_label_content='RICHES:', \
        right_label_content=f'[{Player.riches_count:2} /{self.Game.riches_maximum:2} ] ({Player.riches_points} POINTS)')

    #ROW3 COINS: [gold, silver] (coins_points)
    SingleLine(row=3, style=styles['smaller_label'], \
        left_label_content='COINS:', \
        right_label_content=f'[{Player.coins_gold}G, {Player.coins_silver}S] ({Player.coins_points} POINTS)')

    #ROW4 STORAGE: [amount/maximum] (storage_points)
    SingleLine(row=4, style=styles['smaller_label'], \
        left_label_content='STORAGE:', \
        right_label_content=f'[{Player.resources_count:02}/10] ({Player.resources_points} POINTS)')

    #ROW5 images of resources
    TempLabel = QtWidgets.QLabel(f'[ \
        {Player.resources.count("k1")} {img(file_name="k1", width=14, height=16)}| \
        {Player.resources.count("k2")} {img(file_name="k2", width=14, height=16)}| \
        {Player.resources.count("k3")} {img(file_name="k3", width=14, height=16)}| \
        {Player.resources.count("k4")} {img(file_name="k4", width=14, height=16)} ]')
    #Its not really RIGHT as this row have only 1 widget, but for making references easier we will keep it this way
    TempLabel.setObjectName(f'5-RIGHT') 
    TempLabel.setStyleSheet(styles['bigger_label'])
    VerticalLayout.addWidget(TempLabel)

