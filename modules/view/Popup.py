from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.display_card import display_card
from modules.view.img import img

class Popup:

    def __init__(self, Screen, Game, x_pos = 480, y_pos = 200, width=480, height=310):
        self.PopupWidget = QtWidgets.QWidget(Screen)
        self.PopupWidget.setGeometry(QtCore.QRect(x_pos, y_pos, width, height))
        self.PopupWidget.setObjectName('PopupWidget')
        self.PopupWidget.setStyleSheet(
                                    "#PopupWidget{"
                                    "background-color: #b38b79; "
                                    "border: 1px solid black;"
                                    "border-radius: 8"
                                    "}"
                                    "QPushButton{"
                                    "background-color: #b19686; "
                                    "border: 1px solid black;"
                                    "border-radius: 8;"
                                    "font-size: 12px;  font-weight: 500;"
                                    "}"
                                    "QPushButton:hover{"
                                    "background-color: #e5e2d7;"
                                    "}"
                                    )

        #Prepare vertical layout for popup
        self.VierticalLayout = QtWidgets.QVBoxLayout(self.PopupWidget)

        #Prepare label for maintext
        self.MainText = QtWidgets.QLabel('MainTextLabel')
        self.MainText.setStyleSheet("font-size: 18px;  font-weight: 450;")
        self.MainText.setFixedHeight(50)
        self.VierticalLayout.addWidget(self.MainText)
        self.VierticalLayout.setContentsMargins(20,10,10,10) #left, top, right, bottom

        #Prepare horizontal layout for card image (LEFT SIDE) and some text (RIGHT SIDE)
        self.HorizontalLayout = QtWidgets.QHBoxLayout()
        self.VierticalLayout.addLayout(self.HorizontalLayout)
        
        #For test we're adding some widget to simulate card image
        self.CardWidget = QtWidgets.QWidget()
        self.CardWidget.setFixedSize(120, 160)
        self.CardWidget.setStyleSheet(
                                    "background-color: #935b89; "
                                    "border: 1px solid black;"
                                    "border-radius: 8"
                                    )
        self.HorizontalLayout.insertWidget(0, self.CardWidget)
        

        #Prepare Vertical layout for extra text labels. It will be RIGHT SIDE of Horizontal Layout 
        self.VierticalLayout2 = QtWidgets.QVBoxLayout()
        self.HorizontalLayout.insertLayout(1, self.VierticalLayout2)

        #Add text labels
        self.right_side_widgets_list = list()
        for x in range(0, 11):
            self.right_side_widgets_list.append(QtWidgets.QLabel(f'right_side_widgets_list{x} label')) 
            self.right_side_widgets_list[x].setStyleSheet("font-size: 15px;  font-weight: 500;")
            self.VierticalLayout2.insertWidget(x, self.right_side_widgets_list[x])

        #As widget 10 is 1 line information we're giving it fixed height to match 2 lines labels
        self.right_side_widgets_list[10].setFixedHeight(50)

        #Additional widget for choosing resources
        self.right_side_widgets_list.append(QtWidgets.QWidget(self.PopupWidget)) #This widged works weird until parent was added

        ################################
        # 0 - Player Resources (Text)
        # 1 - Player Resources (Images)
        # 2 - Card cost (Text)
        # 3 - Card cost (Images)
        # 4 - Player Resources AFTER action (text)
        # 5 - Player Resources AFTER action (images)
        # 6 - Resources to throw out (text)
        # 7 - Resources to throw out (images)
        # 8 - Resources to upgrade (text)
        # 9 - Resources to upgrade (images)
        # 10 - You have not enough resources (text)
        # 11 - buttons to manipulate resources
        ################################

        #Prepare horizontal layout for buttons
        self.HorizontalLayout2 = QtWidgets.QHBoxLayout()
        self.VierticalLayout.addLayout(self.HorizontalLayout2)
        self.HorizontalLayout2.setContentsMargins(0,20,0,0) #left, top, right, bottom

        #Add buttons
        self.Button1 = QtWidgets.QPushButton('OK')
        self.Button1.setStyleSheet('')
        self.Button1.setFixedHeight(50)
        self.HorizontalLayout2.addWidget(self.Button1)

        self.Button2 = QtWidgets.QPushButton('CANCEL')
        self.Button2.setFixedHeight(50)
        self.HorizontalLayout2.addWidget(self.Button2)
        
        #Additional buttons in case player have to decide how many Trade card is played
        self.Button3 = QtWidgets.QPushButton('+')
        self.Button3.setStyleSheet('')
        self.Button3.setFixedSize(50, 50)
        self.HorizontalLayout2.addWidget(self.Button3)

        self.Button4 = QtWidgets.QPushButton('-')
        self.Button4.setFixedSize(50, 50)
        self.HorizontalLayout2.addWidget(self.Button4)

        #Assing methods to buttons
        self.Button1.clicked.connect(self.confirm) 
        self.Button2.clicked.connect(self.close_popup) 

    def close_popup(self):
        self.PopupWidget.hide()

    def confirm(self):
        #We assume that Button1 is invisible unless action is possible so we're not checking if player fulfill requirements here
        if self.popup_type == 'Treasure':
            pass


    def display_popup(self):
        self.PopupWidget.show()

    def configure_popup(self, popup_type, Card, Ui, Player):
        self.popup_type = popup_type
        #We start with hidding all right side widgets (so we can display desired for given popup_type)
        for x in self.right_side_widgets_list:
            x.hide()

        #We are hidding also all buttons expect button2 (Player should always be able to cancel)
        self.Button1.hide()
        self.Button3.hide()
        self.Button4.hide()

        #We're also hidding Card on this widget because it might be not needed
        self.CardWidget.hide()

        checker=True #Variable to help determine which widgets should be shown 

        #Then we're going to check popup_type and display desired right_side_widgets
        #Treasure Card picking
        if popup_type == 'Treasure':
            for x in [0,1,2,3,4,5,10]:
                pass
                self.right_side_widgets_list[x].show()
            for x in range(1,5):
            #check if player have enough resources of every color to buy this Treasure Card
                if Player.resources.count(f'k{x}') < Card.Card.the_list[0].count(f'k{x}'):
                    checker=False
            if checker:
                self.right_side_widgets_list[10].hide()
                self.Button1.show()
            else:
                self.right_side_widgets_list[4].hide()
                self.right_side_widgets_list[5].hide()
                self.Button1.hide()


        #Playable Card picking
        elif self.popup_type == 'Playable':
            #If Playable card do not require leaving dies this popup shouldn't be shown
            for x in [0,1,6,7,8,10]:
                self.right_side_widgets_list[x].show()

        #Trade Card
        if self.popup_type == 'Trade':
            for x in range [0,1,2,3,4,5,10, 11]:
                self.right_side_widgets_list[x].show()

        #Upgrade
        elif self.popup_type == 'Upgrade':
            #If Playable card do not require leaving dies this popup shouldn't be shown
            for x in [0,1,8,9]:
                self.right_side_widgets_list[x].show()

        #Production Card
        #This shouldn't require any popup

        #too_much_resources
        elif self.popup_type == 'too_much_resources':
            pass


        #If we have not dealing with "too_much_resources" popup, we should display the Card
        if self.popup_type != 'too_much_resources':
            #Delete old CardWidget inside PopupBox
            self.CardWidget.deleteLater()

            #This works good but i wasn't able to find way of copying widget (only moving this) so instead we generate a new one
            # self.CardWidget = Card
            # self.HorizontalLayout.insertWidget(0, self.CardWidget

            #Generate new card
            self.CardWidget = Ui.display_card(Card=Card.Card, Target=self.HorizontalLayout, position_in_layout=0, for_popup=True)
            self.CardWidget.setFixedSize(120, 160)

            #Looks like its not needed but i am leaving this line "just in case"
            self.CardWidget.show()

        if Card.Card.bonus > 1:
            bonus = ' +1 Gold coin'
        elif Card.Card.bonus == 1:
            bonus = ' +1 Silver coin'
        else:
            bonus = ''

        #Then we should update labels
        maintext={
                'Treasure':f'You are buying a Treasure Card{bonus}',
                'Playable':'You are taking a Playable Card'
                }
        self.MainText.setText(maintext[self.popup_type])
        
        self.update_right_side_widgets(Player=Player, Card=Card)
        

    def update_right_side_widgets(self, Player, Card):
        self.right_side_widgets_list[0].setText("You have:")
        self.right_side_widgets_list[1].setText(
            f'[ \
            {Player.resources.count("k1")} {img(file_name="k1", width=14, height=16)}| \
            {Player.resources.count("k2")} {img(file_name="k2", width=14, height=16)}| \
            {Player.resources.count("k3")} {img(file_name="k3", width=14, height=16)}| \
            {Player.resources.count("k4")} {img(file_name="k4", width=14, height=16)} \
            ]')

        self.right_side_widgets_list[2].setText("It costs:")
        self.right_side_widgets_list[3].setText(
            f'[ \
            {Card.Card.the_list[0].count("k1")} {img(file_name="k1", width=14, height=16)}| \
            {Card.Card.the_list[0].count("k2")} {img(file_name="k2", width=14, height=16)}| \
            {Card.Card.the_list[0].count("k3")} {img(file_name="k3", width=14, height=16)}| \
            {Card.Card.the_list[0].count("k4")} {img(file_name="k4", width=14, height=16)} \
            ]')

        self.right_side_widgets_list[4].setText("You will have:")
        self.right_side_widgets_list[5].setText(
            f'[ \
            {Player.resources.count("k1")-Card.Card.the_list[0].count("k1")} {img(file_name="k1", width=14, height=16)}| \
            {Player.resources.count("k1")-Card.Card.the_list[0].count("k2")} {img(file_name="k2", width=14, height=16)}| \
            {Player.resources.count("k1")-Card.Card.the_list[0].count("k3")} {img(file_name="k3", width=14, height=16)}| \
            {Player.resources.count("k1")-Card.Card.the_list[0].count("k4")} {img(file_name="k4", width=14, height=16)} \
            ]')
        self.right_side_widgets_list[10].setText('You have not enough resources!')
        