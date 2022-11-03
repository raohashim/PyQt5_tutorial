# Grid layout : For creating a calculator we need several buttons and a text area. We need to create
# several horizontal and vertical layout. Which will be very confusing.
# So, to overcome that problem we use the grid layout

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt  # WE use Qt lib to get the horizontal sliders else we have vertical sliders
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        ##### Creat a Window #####
        self.setWindowTitle("Grid Layout")
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        ##### Create Grid Layout  #####
        self.grid = QGridLayout()

        # Creat Buttons
        btn1 = QPushButton("Button1")
        btn2 = QPushButton("Button2")
        btn3 = QPushButton("Button3")
        btn4 = QPushButton("Button4")
        '''
        # Adding Buttons to our Grid Layout
        # in order to add buttons to our grid we also have to mention the row and the col. no. along the name of button.
        # grid.addWiget("Name of item" , row--, col||)
        self.grid.addWidget(btn1, 0, 0)
        self.grid.addWidget(btn2, 0, 1)
        self.grid.addWidget(btn3, 1, 0)
        self.grid.addWidget(btn4, 1, 1)
        '''
        # Using the nested for loop for adding the widgets to the grid

        for i in range(0,3): # for Rows
            for j in range(0,3): # For Columns
                btn = QPushButton("Button {}{}".format(i, j))
                self.grid.addWidget(btn,i ,j)
                # To know which button we clicked we create a clicked and connect button for it
                btn.clicked.connect(self.clicked)




        # Set Layout for the Main Window
        self.setLayout(self.grid)

        ##### Show Window #####
        self.show()

    def clicked(self):
        # This fucntion will return the text value (name) of the button clicked
        butn_ID = self.sender().text()
        print (self.sender().text())

        if butn_ID == "Button 00":
            print("You Clicked Button 1")
        elif butn_ID == "Button 01":
            print("You Clicked Button 2")
        elif butn_ID == "Button 02":
            print("You Clicked Button 3")
        elif butn_ID == "Button 10":
            print("You Clicked Button 4")
        elif butn_ID == "Button 11":
            print("You Clicked Button 5")


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
