# Progress Bar:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer  # WE use Qt lib to get the horizontal sliders else we have vertical sliders
from PyQt5.QtGui import QIcon

count = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        ##### Creat a Window #####
        self.setWindowTitle("Progress Bar")
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        #
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        ##### Creat a Timer  #####
        # To update the progress bar we have three ways:
        # 1- QTimer (standard process)
        # 2- Thread
        # 3- while loop or for loop (cause problem)
        # But, the recommended way  is to use the QTimer for the updation
        # Create Progress Bar
        self.prog_bar = QProgressBar()
        btn_start = QPushButton("Start")
        btn_start.clicked.connect(self.time_start)
        btn_stop = QPushButton("Stop")
        btn_stop.clicked.connect(self.time_stop)
        #
        self.timer = QTimer()
        self.timer.setInterval(100)  # Every 100ms we update our progress bar
        # Time Out Function : Process we want to do while our timer is running.
        self.timer.timeout.connect(self.runProgressbar)
        #
        vbox.addWidget(self.prog_bar)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(btn_start)
        hbox.addWidget(btn_stop)
        hbox.addStretch()
        #
        self.setLayout(vbox)

        ##### Show Window #####
        self.show()

    def runProgressbar(self):
        # We need a variable to update out progress bar in interval

        # Create a variable to Update out progress bar.
        global count
        count += 1
        print(count)
        self.prog_bar.setValue(count)
        if count == 100:
            self.time_stop()

    def time_start(self):

        self.timer.start()

    def time_stop(self):

        self.timer.stop()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
