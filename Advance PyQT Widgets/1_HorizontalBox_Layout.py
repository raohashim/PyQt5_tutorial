# We are using the geometry function to fix position our buttons.
# So to get rid of them we use horizontal and vertical box layout on top of our window.
# This will helps us to alogn our boxes in horizontal and vertical position.
# Horizontal and vertical layout also helps to maintain the position of the button when we zoom in or out our windows.

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
        # Horizontal box layout is used to add buttons or items in along the x-axis (horizonta.)
        # For positioning of the button on windows
        # If we only use add stretch at the top it will move our buttons to the right side of window
        # So If we want the size of the buttons to remain same and center oriented we will also use the
        # addstretch after adding buttons to the layout as per example
        hbox = QHBoxLayout()  # To initiate a horizontal box layout
        button1 = QPushButton("Button1")  # Adding Button 1
        button2 = QPushButton("Button2")  # Adding Button 2
        button3 = QPushButton("Button3")  # Adding button 3
        # Adding of the buttons to our layout
        hbox.addStretch()  # It is used to keep the geometry of the buttons and keep them right oriented
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        hbox.addStretch()   # To keep the button center oriented and preserve their geometry we use another addStrech function at the end of layout

        # Here we set the layout for our windows that's why we don't need to use the self earlier
        self.setLayout(hbox)



        ############# Show Window ####################
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
