# We have always be using the fix windows size fixed widgets size till now.
# But we want our window to be adjustable as we increase or decrease its size.
# So now we will move toward layouts from fixed positioning.
##################### Vertical Box Layout #######################

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap  # For font and Images import
from PyQt5.QtCore import QTimer # Timer
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        ###################Creat an Empty Window################
        self.setWindowTitle("Horizontal Box Layout")
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        ###################Adding buttons to our Horizontal Layout#########################
        # Vertical layout box is used to add the buttons along Y-axis or horizontally
        vbox = QVBoxLayout()  # To initiate a vertical box layout
        vbox = QVBoxLayout()  # To initiate a vertical box layout
        button1 = QPushButton("Button1")  # Adding Button 1
        button2 = QPushButton("Button2")  # Adding Button 2
        button3 = QPushButton("Button3")  # Adding button 3
        # Adding add strech on top and bottom keep the button in middle
        # Add stretch is used on top adding buttons to push them to the bottom of window
        vbox.addStretch()
        # Adding of the buttons to our layout
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        # It is used at bottom to push button toward top of window
        vbox.addStretch()

        # Here we set the layout for our windows that's why we don't need to use the self earlier
        self.setLayout(vbox)



        ############# Show Window ####################
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
