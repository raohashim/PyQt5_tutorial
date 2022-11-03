# Menu Widget : Creating the menu for the Window
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt  # WE use Qt lib to get the horizontal sliders else we have vertical sliders
from PyQt5.QtGui import QIcon


# In order to Create a Menu we have to Inherit QMainWindow
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        ##### Creat a Window #####
        self.setWindowTitle("Menu Widget")
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        ##### Main Menu  #####
        menu_bar = self.menuBar()

        # Creating the Menu Items
        file = menu_bar.addMenu("&File")
        edit = menu_bar.addMenu("&Edit")
        code = menu_bar.addMenu("&Code")
        help_menu = menu_bar.addMenu("&Help")

        ##### Sub Menu Items #####

        #------ Create a sub Menu------#
        new = QAction("New Project", self)
        # Adding a shortcut Hint to the sub Item
        new.setShortcut("ctrl+N")
        # Adding sub menu to the Menu
        file.addAction(new)

        #------ Open Sub Menu Item ------#
        open = QAction("Open Project", self)
        open.setShortcut("ctrl+O")
        file.addAction(open)

        #----------Adding a New Menues to Sub Menus-----------
        history = file.addMenu("History")
        shw_hist = history.addMenu("Show History")
        rcnt_hist = shw_hist.addMenu("Recent History")
        open_history = shw_hist.addAction("All History")
        history.addAction("Recently Closed")


        #------ Exit Sub Menu Item ------#
        exit_item = QAction("Exit", self)
        exit_item.setShortcut("ctrl+X")
        exit_item.setIcon((QIcon("/home/hashim/MyQT_Tutorials/Advance PyQT Widgets/Resources-Advanced-PyQt5-Widgets-Using-Menu-Widget/exit.png")))
        ## Creating a Click Connect Function For the Exit Button
        exit_item.triggered.connect(self.exit_conn)
        file.addAction(exit_item)

        ##### Show Window #####
        self.show()

    def exit_conn(self):
        # Creating a Message Box to ask user to confirm action
        mbox = QMessageBox.information(self, "Warning", "Are you sure to exit", QMessageBox.Yes| QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
