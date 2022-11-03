import sys
from PyQt5.QtWidgets import *


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        # Size of my window
        self.setGeometry(50, 30, 500, 450)  # (x, y, x size of window, y size of my window)
        # Set the windows title for our Window
        self.setWindowTitle("Using Labels")
        self.UI()

    def UI(self):
        # Creating Labels
        # If we only enter the label without using self it will not display the label in that window.
        text1 = QLabel("Hello Python", self)
        text2 = QLabel("Hello World", self)
        # The labels will overlap each other is we do not define their geometry.
        # So we use the label.move command to specify the x and y axis of label.
        text1.move(10, 50)
        text2.move(10, 100)
        self.show()


def execute_my_window():
    app = QApplication(sys.argv)
    windows = Windows()
    sys.exit(app.exec_())


if __name__ == "__main__":
    execute_my_window()
