import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" <<list Widget>>")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        ##############LineEdit##########
        self.addrecord = QLineEdit(self)
        self.addrecord.move(100, 50)

        ###############Creating a List Widget################
        self.list = QListWidget(self)
        self.list.move(100, 80)

        #############Adding Items to the list###############
        list1 = ["Batman", "Superman", "Spider"]
        self.list.addItems(list1)  # Adding multiple Items
        self.list.addItem("Human")  # Adding single item to the list
        # Using for Loop
        '''for num in range(5):
            self.list.addItem(str(num))'''

        ############Creating Buttons###############
        add = QPushButton("Add", self)
        add.move(370, 100)
        add.clicked.connect(self.add_list)

        dele = QPushButton("Delete", self)
        dele.move(370, 130)
        dele.clicked.connect(self.dele_list)

        get = QPushButton("Get", self)
        get.move(370, 160)
        get.clicked.connect(self.get_list)

        del_all = QPushButton("Delete All", self)
        del_all.move(370, 190)
        del_all.clicked.connect(self.del_all_list)

        self.show()

    def add_list(self):
        val = self.addrecord.text()
        self.list.addItem(val)
        self.addrecord.setText("")  # To get the blank line for our Line Edit

    def dele_list(self):
        index = self.list.currentRow()
        self.list.takeItem(index)

    def get_list(self):
        val = self.list.currentItem().text()
        print(val)

    def del_all_list(self):
        self.list.clear()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
