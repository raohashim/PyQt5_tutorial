import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
# Import the QTimer fro QTCore to use the timer
from PyQt5.QtCore import QTimer

# Font family and font size
# the font supported by the OS is only adapted here
font = QFont("Times", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" <<Timer Editor>>")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        # Create an Empty liable to
        self.lable = QLabel(self)
        self.lable.resize(250,  250)
        self.lable.move(80, 20)
        # Set the Back Ground of Lable
        self.lable.setStyleSheet("background-color:green")
        #################Buttons##################
        start = QPushButton("Start", self)
        start.move(80, 280)
        start.clicked.connect(self.start)
        stop = QPushButton("Stop", self)
        stop.move(250, 280)
        stop.clicked.connect(self.stop)

        #################Timer####################
        self.timer = QTimer()
        # set the interval of timer in ms
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.changeColor)
        self.value = 0

        self.show()

    def changeColor(self):
        # Change the color of thr label as the timer will start
        if self.value == 0:
            self.lable.setStyleSheet("background-color:red")
            self.value = 1
        else:
            self.lable.setStyleSheet("background-color:blue")
            self.value = 0

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()







def main():
    app = QApplication(sys.argv)
    window = Window()
    # In order to start timer at the start of Program
    window.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
