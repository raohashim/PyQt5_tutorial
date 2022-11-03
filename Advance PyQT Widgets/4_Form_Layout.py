# In form layout we have widgets in the columns of the window
#
import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        ###################Creat an Empty Window################
        self.setWindowTitle("Form Layout")
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        #############
        #######Creat Form Layout######
        form_lay = QFormLayout()
        # It will add the title above the rows
        #form_lay.setRowWrapPolicy(form_lay.WrapAllRows)

        #######################################
        name_lab1 = QLabel("Name: ")
        lab1 = QLineEdit("Type your Name Here")
        name_lab2 = QLabel("Password: ")
        lab2 = QLineEdit("Type your Password Here")

        #
        combo = QComboBox()
        combo.addItems(["DE", "FR", "PK", "UK", "US"])
        #
        hbox = QHBoxLayout()

        #
        btn1 = QPushButton("Enter", self)
        btn2 = QPushButton("Exit", self)
        #
        hbox.addStretch()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        # Another Way of adding the Label and Combo Box or any widget.
        form_lay.addRow(QLabel("Country: "), combo)
        #

        form_lay.addRow(hbox)
        #
        #In Form Layout we can only add two wodgets in a row but we can over come it by using two hbox
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())
        # In our form layout we add the items in the Rows
        form_lay.addRow(name_lab1, hbox1)
        form_lay.addRow(name_lab2, lab2)
        # Add the form layout to the Main Window
        self.setLayout(form_lay)

        ############# Show Window ####################
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
