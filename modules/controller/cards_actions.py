#this is part of Ui class
def move_card(self, WholeWidget, direction, move_type):
        #Get positionin of given card inside Ui.PlayerHand.HorizontalLayout
        C_id = self.PlayerHand.HorizontalLayout.indexOf(WholeWidget)
        
        if move_type == 'move_to':
            if direction == -1:
                new_position = 0
            else:
                new_position = len(self.PlayerHand.HorizontalLayout)
        elif move_type == 'move_by':
            new_position = C_id+(direction)

        #We need to check if new position isn't number below 0 because if in other case the card will move to end of the list
        if new_position >= 0:
            self.PlayerHand.HorizontalLayout.insertWidget(new_position, WholeWidget)
