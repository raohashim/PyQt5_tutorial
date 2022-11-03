import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap # Library for showing the images

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Images")
        self.setGeometry(50, 50, 1500, 1000)
        self.UI()

    def UI(self):
        # We initially define opr image as a Liable
        self.image = QLabel(self)
        # Than we use .setPixmap(QPixmap("path to image")) to get our image to display
        self.image.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Images/2021-bmw-m5-cs.jpg"))
        self.image.move(50, 50)
        # Now we create two buttons one will remove the picture and the other will show it again
        button1 = QPushButton("Remove", self)
        button1.move(10,900)
        button1.clicked.connect(self.remove)
        # Button 2
        button2 = QPushButton("Show",self)
        button2.move(1300,900)
        button2.clicked.connect(self.showb)
        self.show()

    def remove(self):
        # To remove the picture from display ,close is used in PyQT
        self.image.close()

    def showb(self):
        # To reshow the picture from display ,show is used in PyQT
        self.image.show()


def main():
    app = QApplication(sys.argv)
    window = Windows()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
