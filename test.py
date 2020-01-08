import sys
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv) 

#Mainwindow
Screen = QtWidgets.QWidget() 

#label1
label1 = QtWidgets.QLabel('label1')
label1.move(100, 100)
label1.setParent(Screen)

#showwindow
Screen.show()

#Screen.close()

#label2
label2 = QtWidgets.QLabel('label2')
label2.move(200, 100)
label2.setParent(Screen)

label2.show()

# Screen.repaint()
# Screen.update()
# Screen.hide()
# Screen.show()
# Screen.close()
#Screen.show()

sys.exit(app.exec_())