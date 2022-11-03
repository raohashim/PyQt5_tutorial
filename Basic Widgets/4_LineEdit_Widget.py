import sys
from PyQt5.QtWidgets import *


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        # Size of my window
        self.setGeometry(50, 30, 500, 450)  # (x, y, x size of window, y size of my window)
        # Set the windows title for our Window
        self.setWindowTitle("Using Line Edits")
        self.UI()

    def UI(self):
        # Creating Line Edits
        # Line Edits are used to ask for user input like name or password
        self.nameTextBox = QLineEdit(self)
        # Here we enter a hint for the user, about what to enter in the desired field
        self.nameTextBox.setPlaceholderText("Please Enter your Name: ")
        self.nameTextBox.move(120, 150)
        # We create another line for entering the password
        self.passTextBox = QLineEdit(self)
        # Place holder text to give user hint what to enter
        self.passTextBox.setPlaceholderText("Please Enter your Name: ")
        # A we want user to enter password so we secure password so no one can see it.
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(120, 180)
        # creating of Button
        button = QPushButton("Save", self)
        button.move(170, 220)
        # Assigning task to the button
        button.clicked.connect(self.getValues)

        # Show the window
        self.show()

    # Function define the task to be performed by the button
    def getValues(self):
        # Get the data from the name line
        name = self.nameTextBox.text()
        # Get the data from the password line
        password = self.passTextBox.text()
        # print(name, password)
        # Show the name and the password enter in the windows title.
        self.setWindowTitle("Your name is :. "+name+" your password is : "+password)


def execute_my_window():
    app = QApplication(sys.argv)
    windows = Windows()
    sys.exit(app.exec_())


if __name__ == "__main__":
    execute_my_window()
