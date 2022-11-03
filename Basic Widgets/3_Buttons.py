import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Windows title
        self.text1 = QLabel("My first Button", self)
        self.setWindowTitle("Buttons ")
        # Windows Geometry
        self.setGeometry(50, 50, 500, 500)
        self.UI()

    def UI(self):
        # Label1
        # Label geometry
        self.text1.move(150, 200)
        # Creation of Button But not signing them any operation
        enterbutton = QPushButton("Enter", self)
        exitbutton = QPushButton("Exit", self)
        # Set the geometry of the buttons
        enterbutton.move(100, 250)
        exitbutton.move(200, 250)
        # Now we assign the task to each button
        enterbutton.clicked.connect(self.enterFunc)
        exitbutton.clicked.connect(self.exitFunc)
        # Show Window
        self.show()

    def enterFunc(self):
        self.text1.setText("You have clicked Enter")
        # In order to get our text displayed we also has to resize Label
        # As if we don't do this it will only remain of the same size as initially defined.
        # And may result in not the results if its length is greater that previously defined.
        self.text1.resize(150, 20)

    def exitFunc(self):
        self.text1.setText("You have clicked Exit")
        self.text1.resize(150, 20)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

