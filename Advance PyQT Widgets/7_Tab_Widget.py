# Tabs :
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt  # WE use Qt lib to get the horizontal sliders else we have vertical sliders
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        ##### Creat a Window #####
        self.setWindowTitle("Tab Widget")
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        ##### Creat a Layout and Creat a Tab #####
        main_layout = QHBoxLayout()
        # Constructor Method for Tabs
        self.tabs = QTabWidget()

        ##### Creating Tabs #####
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        ##### Adding Tabs to Tab Widget #####
        # All the tabs are them self a main window
        self.tabs.addTab(self.tab1, "Tab 1")  # addTab(self.tab, "Name of Tab")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")

        ##### Creating Widgets to the Tabs #####
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        # Creating Widgets for the Vertical and Horizontal Layouts
        self.text = QLabel("hello")
        self.btn1 = QPushButton("Tab 1")
        self.btn1.clicked.connect(self.btnfun)
        self.btn2 = QPushButton("Tab 2")
        # Adding Widgets to horizontal and vertical Layouts
        vbox.addWidget(self.text)
        vbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        ##### Adding Widget to Tabs #####
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)

        ##### Adding Tab Widgets To Main Layout #####
        main_layout.addWidget(self.tabs)

        ##### Addind Main Layout on the Window  #####
        self.setLayout(main_layout)
        ##### Show Window #####
        self.show()

    def btnfun(self):
        self.text.setText("Meine Liebe")

        
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
