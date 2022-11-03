# Message Box is the pop up message we get when we hit some other button.
# There are different type of message boxes such as QUESTION and INFORMATION message boxes
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
# Font family and font size
# the font supported by the OS is only adapted here
font = QFont("Times", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Message Box Widget")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        # Create a Button
        button = QPushButton("Click Me", self)
        # We set the font for the text in the button
        button.setFont(font)
        button.move(200, 150)
        button.clicked.connect(self.messagebox)

        self.show()

    def messagebox(self):
        # Question message box
        # It ask the used a question and give them some options to select from.
        # QMessageBox.question(self, Title, Message text, selection Buttons, default Selection Button)
        qmbox = QMessageBox.question(self, "Warning!!!!! ", "are you sure to exit", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #
        if qmbox==QMessageBox.Yes:
            sys.exit()
        elif qmbox==QMessageBox.No:
            print("You clicked no Button")

        '''
        # Information message box
        # It is only used to give user some information when they clicked some button
        # QMessageBox.information(self, Title, Information text)
        imbox = QMessageBox.information(self, "Information!!", "You Logged out")'''


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

