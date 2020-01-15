from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.view.display_card import display_card
from modules.view.img import img
from functools import partial

class Popup:

    from modules.controller.action_confirmed import action_confirmed, check_player_resources, check_player_riches, end_of_the_turn
    def __init__(self, Ui, Game, x_pos = 480, y_pos = 200, width=480, height=310):
        self.multiplier = 1
        self.Game=Game
        self.Player = Game.CurrentPlayer
        self.resources_to_thorw_out = list()
        self.upgraded_resources = list()
        self.PopupWidget = QtWidgets.QWidget(Ui.Screen)
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
        self.PopupCardWidget = QtWidgets.QWidget()
        self.PopupCardWidget.setObjectName('CardWidgetTemplate')
        self.PopupCardWidget.setFixedSize(120, 160)
        self.PopupCardWidget.setStyleSheet(
                                    "background-color: #935b89; "
                                    "border: 1px solid black;"
                                    "border-radius: 8"
                                    )
        self.HorizontalLayout.insertWidget(0, self.PopupCardWidget)
        

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

        # self.right_side_widgets_list.append(QtWidgets.QLabel(f'this is extra test')) 
        # self.VierticalLayout2.insertWidget(11, self.right_side_widgets_list[11])
        # self.right_side_widgets_list[11].show()


        #Additional widget for choosing resources
        self.right_side_widgets_list.append(QtWidgets.QWidget(self.PopupWidget)) #This widged works weird until parent was added
        self.VierticalLayout2.insertWidget(11, self.right_side_widgets_list[11])
        #Prepare horizontal layout for buttons to manipulater resources
        HorizontalLayout_for_resource_buttons = QtWidgets.QHBoxLayout(self.right_side_widgets_list[11])
        HorizontalLayout_for_resource_buttons.setContentsMargins(5, 5, 165, 5)

        self.resources_buttons = list()
        for x in range(1, 5):
            pass
            TempButton = QtWidgets.QPushButton()
            TempButton.setFixedSize(30, 30)
            TempButton.setStyleSheet(f'background-image: url(images/add_k{x}.png) ;')
            TempButton.clicked.connect(partial(self.press_resource_button, f'k{x}') )
        

            HorizontalLayout_for_resource_buttons.addWidget(TempButton)
            self.resources_buttons.append(TempButton)


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
        self.Button3.clicked.connect(self.plus_button_action)

        self.Button4 = QtWidgets.QPushButton('-')
        self.Button4.setFixedSize(50, 50)
        self.HorizontalLayout2.addWidget(self.Button4)
        self.Button4.clicked.connect(self.minus_button_action)

    def plus_button_action(self):
        self.multiplier += 1
        self.update_popup_widgets()


    def minus_button_action(self):
        if self.multiplier <= 1: return #Player cant use card 0 times or used it reversed
        self.multiplier -= 1
        self.update_popup_widgets()

    def close_popup(self):
        self.resources_to_thorw_out = list()
        self.upgraded_resources = list()
        self.PopupWidget.hide()

    def display_popup(self):
        self.PopupWidget.show()
        self.multiplier = 1
        self.update_popup_widgets()

    def configure_popup(self, popup_type, ClickedCardWidget, Ui):
        self.ClickedCardWidget = ClickedCardWidget
        self.popup_type = popup_type

        #Check card distance to righd edge in its layout
        #Player have pay 1 die for cadt between right edge and choosen card if he is taking playable card
        #Player could get extra point for buying one of 2 closest do right edge Treasure cards
        self.distance_to_right_edge = self.ClickedCardWidget.parent().parent().layout().count() - self.ClickedCardWidget.parent().parent().layout().indexOf(self.ClickedCardWidget.parent()) - 1

        #Assing methods to buttons - 
        #We're assigning here (instead in __init__ because we're using Ui as argument which isnt aviable in Ui)
        self.Button1.disconnect()
        #Quick Note: self.Popupself.ClickedCardWidget is card inside popup, self.ClickedCardWidget is card which was clicked
        self.Button1.clicked.connect(partial(self.action_confirmed, self.ClickedCardWidget.parent(), self.ClickedCardWidget, Ui, self.Game)) 
        self.Button2.disconnect()
        self.Button2.clicked.connect(self.close_popup) 

        #We start with hidding all right side widgets (so we can display desired for given popup_type)
        for x in self.right_side_widgets_list:
            x.hide()

        #We are hidding also all buttons expect button2 (Player should always be able to cancel)
        self.Button1.hide()
        self.Button3.hide()
        self.Button4.hide()

        #We're also hidding Card on this widget because it might be not needed
        self.PopupCardWidget.hide()


        #If we have not dealing with "too_much_resources" popup, we should display the Card
        if self.popup_type != 'too_much_resources':
            #Delete old CardWidget inside PopupBox
            self.PopupCardWidget.deleteLater()

            #Quick Note:
            #This works good but i wasn't able to find way of copying widget (only moving this) so instead we generate a new one
            # self.PopupCardWidget = Card
            # self.HorizontalLayout.insertWidget(0, self.PopupCardWidget

            #Generate new card
            self.PopupCardWidget = Ui.display_card(Card=self.ClickedCardWidget.Card, Target=self.HorizontalLayout, position_in_layout=0, for_popup=True)
            #self.PopupCardWidget.setFixedSize(120, 160)

            #Looks like its not needed but i am leaving this line "just in case"
            self.PopupCardWidget.show()

        #Then we should update labels
        self.update_popup_widgets()
    


    def update_popup_widgets(self):
        #Then we're going to check self.popup_type and display desired right_side_widgets
        # ###################################################################################
        # #And finally, configuring for each popup type
        # #Buyable Card picking
        # if self.popup_type == 'BuyableStore':
        #     for x in [0,1,2,3,4,5,10]:
        #         pass
        #         self.right_side_widgets_list[x].show()

        # #Playable Card picking
        # elif self.popup_type == 'PlayableStore':
        #     #If Playable card do not require leaving dies this popup shouldn't be shown
        #     for x in [0,1,6,7,10,11]:
        #         self.right_side_widgets_list[x].show()
        #     self.Button1.hide()

        #     #Check if player have enough resources to this acction
        #     if self.distance_to_right_edge <= len(self.Player.resources):
        #         self.right_side_widgets_list[10].hide()
        #     else:
        #         self.right_side_widgets_list[11].hide()

        # #Trade Card
        # if self.popup_type == 'Trade':
        #     for x in [0,1,2,3,4,5]:
        #         self.right_side_widgets_list[x].show()

        # #Upgrade
        # elif self.popup_type == 'Upgrade':
        #     #If Playable card do not require leaving dies this popup shouldn't be shown
        #     for x in [0,1,8,9]:
        #         self.right_side_widgets_list[x].show()

        # #Harvesting card
        # #This shouldn't require any popup

        # #too_much_resources
        # elif self.popup_type == 'too_much_resources':
        #     pass

        distance_to_right_edge=self.distance_to_right_edge
        player_resources = {'k1':0, 'k2':0, 'k3':0, 'k4':0}
        for x in ['k1', 'k2', 'k3', 'k4']:
            player_resources[x] = self.Player.resources.count(x)

        #Player Resources - every kind of popup will have this one
        self.right_side_widgets_list[0].setText("You have:")
        self.right_side_widgets_list[1].setText(
            f'[ \
            {player_resources["k1"]} {img(file_name="k1", width=14, height=16)}| \
            {player_resources["k2"]} {img(file_name="k2", width=14, height=16)}| \
            {player_resources["k3"]} {img(file_name="k3", width=14, height=16)}| \
            {player_resources["k4"]} {img(file_name="k4", width=14, height=16)} \
            ]')
        
        self.right_side_widgets_list[0].show()
        self.right_side_widgets_list[1].show()
        
        #Card cost/income - This should be visible in cases when we're reading this value from card
        resources_cost = {'k1':0, 'k2':0, 'k3':0, 'k4':0}
        resources_income = {'k1':0, 'k2':0, 'k3':0, 'k4':0}
        for x in ['k1', 'k2', 'k3', 'k4']:
            if self.popup_type == 'BuyableStore':
                resources_cost[x] = self.ClickedCardWidget.Card.the_list[0].count(x)
            elif self.popup_type == 'Trade':
                resources_cost[x] = self.ClickedCardWidget.Card.the_list[0].count(x) * self.multiplier
                resources_income[x] = self.ClickedCardWidget.Card.the_list[1].count(x) * self.multiplier
        self.right_side_widgets_list[2].setText("It costs:")
        self.right_side_widgets_list[3].setText(
            f'[ \
            {resources_cost["k1"]} {img(file_name="k1", width=14, height=16)}| \
            {resources_cost["k2"]} {img(file_name="k2", width=14, height=16)}| \
            {resources_cost["k3"]} {img(file_name="k3", width=14, height=16)}| \
            {resources_cost["k4"]} {img(file_name="k4", width=14, height=16)} \
            ]')
        if self.popup_type == 'BuyableStore' or self.popup_type == 'Trade':
            self.right_side_widgets_list[2].show()
            self.right_side_widgets_list[3].show()

        #Resources after action - This should be visible in cases when we're reading this value from card
        resource_after_action = {'k1':0, 'k2':0, 'k3':0, 'k4':0}
        if self.popup_type == 'BuyableStore' or self.popup_type == 'Trade':
            self.Button1.show()
            self.right_side_widgets_list[4].show()
            self.right_side_widgets_list[5].show()
            self.right_side_widgets_list[10].hide()
            for x in ['k1', 'k2', 'k3', 'k4']:
                if self.popup_type == 'BuyableStore':
                    resource_after_action[x] = player_resources[x] - resources_cost[x] 
                elif self.popup_type == 'Trade':
                    self.Button3.show()
                    self.Button4.show()
                    resource_after_action[x] = player_resources[x] - (resources_cost[x]) + (resources_income[x])
                #We assume that even if player AFTER action will have positive amount of resource he shouldnt be able to make this trade
                if (player_resources[x] - (resources_cost[x]))<0: 
                    self.Button1.hide()
                    self.right_side_widgets_list[4].hide()
                    self.right_side_widgets_list[5].hide()
                    self.right_side_widgets_list[10].show()
            self.right_side_widgets_list[4].setText("You will have:")
            self.right_side_widgets_list[5].setText(
                f'[ \
                {resource_after_action["k1"]} {img(file_name="k1", width=14, height=16)}| \
                {resource_after_action["k2"]} {img(file_name="k2", width=14, height=16)}| \
                {resource_after_action["k3"]} {img(file_name="k3", width=14, height=16)}| \
                {resource_after_action["k4"]} {img(file_name="k4", width=14, height=16)} \
                ]')

        #Extra counter for throwing out resources - This should be visible while picking Playable card
        if self.popup_type == 'PlayableStore' or self.popup_type == 'Upgrade':
            self.right_side_widgets_list[6].show()
            self.right_side_widgets_list[7].show()
            #Resources buttons shouln't be shown if player have choosen his resources
            if (self.popup_type == 'PlayableStore' and (len(self.resources_to_thorw_out) != distance_to_right_edge)) \
            or (self.popup_type == 'Upgrade' and (len(self.resources_to_thorw_out) != int(self.ClickedCardWidget.Card.the_list[0][0]))):
                self.right_side_widgets_list[11].show()
            if self.popup_type == 'PlayableStore':
                self.resources_buttons[3].show() #this button is aviable for throwing resources but hidden for upgrade
                self.right_side_widgets_list[6].setText(
                    f"You are throwing out ({len(self.resources_to_thorw_out)}/{distance_to_right_edge})")
            if self.popup_type == 'Upgrade':
                    self.resources_buttons[3].hide() #this button is aviable for throwing resources but hidden for upgrade
                    self.right_side_widgets_list[6].setText(
                        f"You are upgrading ({len(self.resources_to_thorw_out)}/{self.ClickedCardWidget.Card.the_list[0][0]})")
            self.right_side_widgets_list[7].setText(
                f'[ \
                {self.resources_to_thorw_out.count("k1")} {img(file_name="k1", width=14, height=16)}| \
                {self.resources_to_thorw_out.count("k2")} {img(file_name="k2", width=14, height=16)}| \
                {self.resources_to_thorw_out.count("k3")} {img(file_name="k3", width=14, height=16)}| \
                {self.resources_to_thorw_out.count("k4")} {img(file_name="k4", width=14, height=16)} \
                ]')

            self.right_side_widgets_list[10].setText('You have not enough resources!')

        maintext={
                "BuyableStore":f"You are buying a Treasure Card",
                "PlayableStore":f"You are taking a Playable Card<br>Bonus resources: {self.ClickedCardWidget.BelowCardWidget_PlayableStore_Label.text()}",
                "Harvest":"You are playing Harvesting Card",
                "Upgrade":"You are playing Upgrade card",
                "Trade":f"You are playing Trade card ({self.multiplier} times)"
                }
        self.MainText.setText(maintext[self.popup_type])





    def press_resource_button(self, resource_type):
        #This settings are prepared for picking playable card
        if self.popup_type == 'PlayableStore':
            if self.Player.resources.count(resource_type) > self.resources_to_thorw_out.count(resource_type):
                self.resources_to_thorw_out.append(resource_type)
                if len(self.resources_to_thorw_out) == self.distance_to_right_edge:
                    self.Button1.show()
                    self.right_side_widgets_list[11].hide()
                
                    #self.ClickedCardWidget.BelowCardWidget_PlayerHand.show()
        if self.popup_type == 'Upgrade':
            #We have to check if player have enough resources in both, his storage and temporary storage of resources which he already upgraded
            if self.Player.resources.count(resource_type)+self.upgraded_resources.count(resource_type) > self.resources_to_thorw_out.count(resource_type):
                self.resources_to_thorw_out.append(resource_type)
                upgraded ={'k1':'k2', 'k2':'k3', 'k3':'k4'}
                self.upgraded_resources.append(upgraded[resource_type])
                
                print(self.ClickedCardWidget.Card.the_list[0][0])
                if len(self.resources_to_thorw_out) == int(self.ClickedCardWidget.Card.the_list[0][0]):
                    self.Button1.show()
                    self.right_side_widgets_list[11].hide()
        self.update_popup_widgets()