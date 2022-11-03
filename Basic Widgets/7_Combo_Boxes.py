import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combo Boxes")
        self.setGeometry(10, 10, 500, 500)
        self.GUI()

    def GUI(self):
        self.lable = QLabel("Select your Fav. Language", self)
        self.lable.move(150,70)
        # For creating a combo box
        # NOTE COMBO BOX ONLY CONTAIN STRING ITEMS NO OTHER TYPE
        self.combo = QComboBox(self) # Creating a combo Box
        self.combo.move(150, 100)
        # To add a single Item to a combo box
        self.combo.addItem("Python")
        # To add multiple Item to the combo box
        self.combo.addItems(["C", "C sharp", "PHP"])
        # Adding multiple items to Combobox using for loop
        list1 = ["Batman","Superman", "Spiderman"]
        # Adding list to combo box
        for name in list1:
            self.combo.addItem(name)
        # Adding numbers in a range to combo box
        for number in range(18, 30):
            self.combo.addItem(str(number))

        # Create a safe button
        button = QPushButton("Save",self)
        button.move(150, 130)
        button.clicked.connect(self.getvalue)
        self.show()

    # Function to get the value selected in the combo box.
    def getvalue(self):
        value = self.combo.currentText()
        print(value)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

