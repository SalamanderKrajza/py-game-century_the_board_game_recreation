###################################################################################
#
def take_card(self, target, WholeWidget, event):
    #print('widget removed')
    #print(target)
    #print(target.itemAt(1))
    #print(target.indexOf(WholeWidget)) #Not working with self.Whole_Widget
    #WholeWidget.hide()

    self.playerHand.HorizontalLayout.addWidget(WholeWidget)
    self.playerHand.scrollAreaWidgetContents.resize(self.playerHand.scrollAreaWidgetContents.width()+130, self.playerHand.scrollAreaWidgetContents.height())

    #target.removeWidget(WholeWidget)

#
###################################################################################