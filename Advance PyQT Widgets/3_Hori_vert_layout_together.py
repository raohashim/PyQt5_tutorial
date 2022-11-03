#Main layout.
# Main layout is needed to be vertical
# Top layout----->
# Bottom Layout------->
# inside layouts we have widgests in both top and bottom layout.
#
import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        ###################Creat an Empty Window################
        self.setWindowTitle("Horizontal and Vertical Box Layout")
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        ########################Main Layout#################
        # Create A Main Layout i.e. Vertical layout
        main_layout = QVBoxLayout()
        # Create a top layout
        top_layout = QHBoxLayout()
        # Create a bottom layout
        bottom_layout = QVBoxLayout()
        # Adding Top and bottom Layouts to the main layout.
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)
        #########Widgets#################
        cbox = QCheckBox("Male", self)
        rbtn = QRadioButton("Sex", self)
        list1 = ["1", "2", "3", "4", "5", "6", "7"]
        combo = QComboBox()
        combo.addItems(list1)
        btn1 = QPushButton("Save", self)
        btn2 = QPushButton("Exit", self)
        ################### Assigning the Windgets##############
        # Using Margin for Layouts
        top_layout.setContentsMargins(150, 20, 150, 10)  # Left side, top side, right side, top
        # Adding Widgets To top layer
        top_layout.addWidget(cbox)
        top_layout.addWidget(rbtn)
        top_layout.addWidget(combo)
        # Using Margin for Layouts
        bottom_layout.setContentsMargins(150 , 10, 150, 10)
        # Assigning Widgets to bottom Layer
        bottom_layout.addWidget(btn1)
        bottom_layout.addWidget(btn2)
        ################Set the Main Layout in the main Windows#########
        self.setLayout(main_layout)
        ############# Show Window ####################
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
