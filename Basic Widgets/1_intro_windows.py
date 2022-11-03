import sys
from PyQt5.QtWidgets import *


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        # Size of my window
        self.setGeometry(50,30,500,450)  # (x, y, x size of window, y size of my window)
        self.setWindowTitle("This is our Windows")
        self.show()


def execute_my_window():
    app = QApplication(sys.argv)
    windows = Windows()
    sys.exit(app.exec_())


if __name__ == "__main__":
    execute_my_window()
