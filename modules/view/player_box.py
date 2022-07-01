from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.img import img

def create_player_box(self, Player, width=240, height=130):
    """Method used for adding area to display Player points and resources"""
    if Player.player_number == 0:
        #First (basic) player is displayed in left bottom corner
        x_pos=10
        y_pos=565
    else:
        #Rest of the players are displayed on top of UI
        x_pos=1112-(Player.player_number-1)*262
        y_pos=10

    PlayerBoxWidget = QtWidgets.QWidget(self.Screen)
    PlayerBoxWidget.setObjectName(f'player_{Player.player_number}_box')
    PlayerBoxWidget.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
    PlayerBoxWidget.setStyleSheet(
        f"#player_{Player.player_number}_box{{background-color: #b38b79; border: 1px solid black}}"
    )

    return PlayerBoxWidget

def fill_playerbox_with_content(self, PlayerBoxWidget, Player):
    """Create grid and fill it with player resources/stats"""
    def generate_player_labels():
        """Generates all labels that needs calculations"""
        total_points = f'{Player.total_points} POINTS TOTAL'
        riches = f'[{Player.riches_count:2} /{self.Game.riches_maximum:2} ] ({Player.riches_points} POINTS)'
        coins = f'[{Player.coins_gold}G, {Player.coins_silver}S] ({Player.coins_points} POINTS)'
        resources = f'[{Player.resources_count:02}/{Player.resources_count:02}] ({Player.resources_points} POINTS)'
        images = (
        f'[{Player.resources.count("k1")} {img(file_name="k1", width=14, height=16)}| '
        f'{Player.resources.count("k2")} {img(file_name="k2", width=14, height=16)}| '
        f'{Player.resources.count("k3")} {img(file_name="k3", width=14, height=16)}| '
        f'{Player.resources.count("k4")} {img(file_name="k4", width=14, height=16)} ] '
        )
        return total_points, riches, coins, resources, images

    def create_vertical_laoyt_for_all_rows_of_content():
        VerticalLayout_AllRowsWithContent = QtWidgets.QVBoxLayout(PlayerBoxWidget)
        VerticalLayout_AllRowsWithContent.setSpacing(2)
        VerticalLayout_AllRowsWithContent.setContentsMargins(0,10,0,10)
        return VerticalLayout_AllRowsWithContent

    def display_content_of_row_with_2_columns_in_player_box(row, style, left_label_content, right_label_content):
        """Displays single row of player data"""
        #Create space to display text
        HorizontalLayout_ColumnsOfSingleRow = QtWidgets.QHBoxLayout()
        VerticalLayout_AllRowsWithContent.addLayout(HorizontalLayout_ColumnsOfSingleRow)

        #left side of player box
        TempLabel = QtWidgets.QLabel(left_label_content)
        TempLabel.setStyleSheet(style)
        TempLabel.setFixedWidth(80)
        TempLabel.setObjectName(f'{row}-LEFT')
        HorizontalLayout_ColumnsOfSingleRow.addWidget(TempLabel)

        #right side of player box
        TempLabel = QtWidgets.QLabel(right_label_content)
        TempLabel.setStyleSheet(style)
        TempLabel.setObjectName(f'{row}-RIGHT')
        HorizontalLayout_ColumnsOfSingleRow.addWidget(TempLabel)

    def display_content_of_row_with_1_columns_in_player_box(row, style, content):
        """
        Method for displaying rows that contains only 1 column
        TempLabel is named RIGHT because we're updating only RIGHT side of other rows and code is seraching for that name
        """
        TempLabel = QtWidgets.QLabel(images)
        TempLabel.setObjectName(f'{row}-RIGHT') 
        TempLabel.setStyleSheet(style)
        VerticalLayout_AllRowsWithContent.addWidget(TempLabel)

    total_points, riches, coins, resources, images = generate_player_labels()
    VerticalLayout_AllRowsWithContent = create_vertical_laoyt_for_all_rows_of_content()

    #ROW1 Player_name - total_points
    #ROW2 RICHES: [amount/maximum] (riches_points)
    #ROW3 COINS: [gold, silver] (coins_points)
    #ROW4 STORAGE: [amount/maximum] (storage_points)
    #ROW5 <images with resources>
    display_content_of_row_with_2_columns_in_player_box(1, self.styles['bigger_label'], Player.name, total_points)
    display_content_of_row_with_2_columns_in_player_box(2, self.styles['smaller_label'], 'RICHES:', riches)
    display_content_of_row_with_2_columns_in_player_box(3, self.styles['smaller_label'], 'COINS:', coins)
    display_content_of_row_with_2_columns_in_player_box(4, self.styles['smaller_label'], 'STORAGE:', resources )
    display_content_of_row_with_1_columns_in_player_box(5, self.styles['bigger_label'], images)
