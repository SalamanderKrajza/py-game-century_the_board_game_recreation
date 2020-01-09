from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
def player_box(self, player, left_margin, top_margin, width=240, height=130):
    """Method used for adding area which displays player points and resources"""
    player_box_widget = QtWidgets.QWidget(self.Screen)
    player_box_widget.setObjectName(f'player_{player.no}_box')
    player_box_widget.setGeometry(QtCore.QRect(left_margin, top_margin, width, height))
    player_box_widget.setStyleSheet(
        f"#player_{player.no}_box{{background-color: #b38b79; border: 1px solid black}}"
        "#bigger_labels{font-size:17px; font-weight: bold; color: black}"
        "#smaller_labels{font-size:13px; font-weight: bold; color: black}"
    )

    VerticalLayout = QtWidgets.QVBoxLayout(player_box_widget)
    VerticalLayout.setSpacing(2)
    VerticalLayout.setContentsMargins(0,10,0,10)


    def SingleLine(row_type, left_label_content, right_label_content):
        #left side
        HorizontalLayout = QtWidgets.QHBoxLayout()
        VerticalLayout.addLayout(HorizontalLayout)
        qtemp = QtWidgets.QLabel(left_label_content)
        qtemp.setObjectName(row_type)
        qtemp.setFixedWidth(80)
        HorizontalLayout.addWidget(qtemp)

        #right side
        qtemp = QtWidgets.QLabel(right_label_content)
        qtemp.setObjectName(row_type)
        HorizontalLayout.addWidget(qtemp)

    points = 5

    #ROW1 player_name - total_points
    SingleLine(row_type="bigger_labels", \
        left_label_content=f'{player.name}', \
        right_label_content=f'{player.total_points} POINTS TOTAL')

    #ROW2 RICHES: [amount/maximum] (riches_points)
    SingleLine(row_type="smaller_labels", \
        left_label_content='RICHES:', \
        right_label_content=f'[{player.riches_count:2} /{self.Game.riches_maximum:2} ] ({player.riches_points} POINTS)')

    #ROW3 COINS: [gold, silver] (coins_points)
    SingleLine(row_type="smaller_labels", \
        left_label_content='COINS:', \
        right_label_content=f'[{player.coins_gold}G, {player.coins_silver}S] ({player.coins_points} POINTS)')

    #ROW4 STORAGE: [amount/maximum] (storage_points)
    SingleLine(row_type="smaller_labels", \
        left_label_content='STORAGE:', \
        right_label_content=f'[{player.resources_count:02}/10] ({player.resources_points} POINTS)')

    #ROW5 images of resources
    qtemp = QtWidgets.QLabel(f'[ \
        {player.resources.count("k1")} {self.img(file_name="k1", width=14, height=16)}| \
        {player.resources.count("k2")} {self.img(file_name="k2", width=14, height=16)}| \
        {player.resources.count("k3")} {self.img(file_name="k3", width=14, height=16)}| \
        {player.resources.count("k4")} {self.img(file_name="k4", width=14, height=16)} ]')
    qtemp.setObjectName("bigger_labels")
    VerticalLayout.addWidget(qtemp)

