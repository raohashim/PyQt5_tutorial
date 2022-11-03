# Q Tables
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt  # WE use Qt lib to get the horizontal sliders else we have vertical sliders
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        ##### Creat a Window #####
        self.setWindowTitle("Table Widget")
        self.setGeometry(50, 50, 600, 500)
        self.UI()

    def UI(self):
        ##### Creat a Table Widget in a Vrtical Box #####
        vbox = QVBoxLayout()
        # Create a table
        self.table1= QTableWidget()
        # Create a Push Button
        btn1 = QPushButton("Get")

        ##### Add Widgets to the Layout #####
        vbox.addWidget(self.table1)
        vbox.addWidget(btn1)

        ##### Set the Rows of the table #####
        self.table1.setRowCount(5)

        ##### Set the Columns of table #####
        self.table1.setColumnCount(3)

        ##### Change the Header or Heading of the table Columns #####
        self.table1.setHorizontalHeaderItem(0, QTableWidgetItem("First Name"))  # setHorizontalHeaderItem(Column Number, QTableWidgetItem("New Heading")
        self.table1.setHorizontalHeaderItem(1, QTableWidgetItem("Sur Name"))
        self.table1.setHorizontalHeaderItem(2, QTableWidgetItem("Address"))

        ##### To Hide the heading of Rows or Columns #####
        #self.table1.horizontalHeader().hide()

        ##### Adding Values to the Table #####
        self.table1.setItem(0, 0, QTableWidgetItem("M. Hashim"))  # setItem(row number, column number, QTableWidgetItem("Text To Add")
        self.table1.setItem(0, 1, QTableWidgetItem("Rao"))  # Row and col no.
        self.table1.setItem(0, 2, QTableWidgetItem("Gojra"))  # Row and col no.
        self.table1.setItem(2, 0, QTableWidgetItem("Fatima"))  # Row and col no.
        self.table1.setItem(3, 1, QTableWidgetItem("Rao"))  # Row and col no.
        self.table1.setItem(1, 2, QTableWidgetItem("Heilbronn"))  # Row and col no.

        ##### Limiting Editing of Table by Double Click #####
        self.table1.setEditTriggers(QAbstractItemView.NoEditTriggers)

        ##### Get the value from Table using Double Click #####
        self.table1.doubleClicked.connect(self.double)

        ##### Get the values from Table Using Get button #####
        btn1.clicked.connect(self.getValue)

        ##### Set the Layout to the Window #####
        self.setLayout(vbox)

        ##### Show Window #####
        self.show()

    ##### Function to get the Values from Table using Button #####
    def getValue(self):
        for item in self.table1.selectedItems():
            print(item.text(), item.row(), item.column())

    ##### get Values from Table Using Double Click #####
    def double(self):
        for item in self.table1.selectedItems():
            print(item.text(), item.row(), item.column())


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
