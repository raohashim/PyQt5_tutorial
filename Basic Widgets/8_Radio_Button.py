# Radio Buttons are the same as check boxes but here we have to make a choice among different options.
# For EG Gender selection
import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Button")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        # Creat two line Edits
        self.name = QLineEdit(self)
        self.name.move(150, 150)
        self.name.setPlaceholderText("Enter Your Name")
        self.surname = QLineEdit(self)
        self.surname.move(150, 180)
        self.surname.setPlaceholderText("Enter Your SurName")
        # Creation of Radio Button
        self.male = QRadioButton("male", self)
        # By default the value of this radio button is selected
        self.male.setChecked(True)
        self.male.move(150, 230)
        # Creating Second Radio button
        self.female = QRadioButton("female", self)
        self.female.move(230, 230)
        # Creation of a Push Button To get the value from radio button and line Edit
        button = QPushButton("Submit", self)
        button.move(250, 250)
        button.clicked.connect(self.getvalue)
        self.show()

    # Function get the value from Radio Button and the Line Edits
    def getvalue(self):
        name = self.name.text()
        surname = self.surname.text()
        # Action Based on the selection of the Radio Button
        if self.male.isChecked():
            print(name, " ", surname, "You are Male")
        else:
            print(name, " ", surname, "You are Female")


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

