import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check Boxes")
        self.setGeometry(10,10,500,500)
        self.GUI()

    def GUI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Enter your name")
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Enter your Surname")
        self.name.move(150, 50)
        self.surname.move(150, 80)
        # We use the QCheckBox To creat a checkbox
        self.remember= QCheckBox("Remember Me", self)
        self.remember.move(150,110)

        button1 = QPushButton("Submit",self)
        button1.move(200,140)
        button1.clicked.connect(self.submit)
        self.show()

    def submit(self):
        if self.remember.isChecked():
            print("Name: " + self.name.text()+" Surname: "+self.surname.text()+ "Remember me checked")
        else:
            print("Name: " + self.name.text() + " Surname: " + self.surname.text() + "Remember me not checked")



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

