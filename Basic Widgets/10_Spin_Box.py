# Spin Box is the box In which we select the numerical value by clicking the up and down button
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
# Font family and font size
# the font supported by the OS is only adapted here
font = QFont("Times", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Spin Box")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.lable = QLabel("select your speed", self)
        self.lable.move(150,80)

        # Initiate the spin box
        self.spinbox = QSpinBox(self)
        self.spinbox.setFont(font)
        self.spinbox.move(150, 100)
        '''# Set the minimum Value of spinbox
        self.spinbox.setMinimum(25)
        # Set the maximum value of spinbox
        self.spinbox.setMaximum(30)'''
        # Instead of using these two lines we can do this using setRange function
        self.spinbox.setRange(25, 35)

        # We can add suffix and prefix before and after the spin box using the function
        # setprefix and setSuffix. For adding symbols or units for the value
        # self.spinbox.setPrefix("$")
        # Instead of symbol if we want to use a string value we use Suffix function
        self.spinbox.setSuffix(" km/h")
        # Changing the stepsize for each click
        self.spinbox.setSingleStep(3) # every time value increase or decrease by 3

        # To get the current value of the spinbox we use this function
        # self.spinbox.valueChanged.connect(self.getValue)

        # To only get the value from the spin box when a button is pressed we create a button and do as follow
        button = QPushButton("Save", self)
        button.move(150, 140)
        button.clicked.connect(self.getValue)
        self.show()

    def getValue(self):
        value = self.spinbox.value()
        print(value)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

