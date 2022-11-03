# Toolbar Widget : Creating the toolbar for the Window and adding items to it
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt  # WE use Qt lib to get the horizontal sliders else we have vertical sliders
from PyQt5.QtGui import QIcon



# In order to Create a Menu we have to Inherit QMainWindow
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        ##### Creat a Window #####
        self.setWindowTitle("Toolbar")
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
        #---------- Creating a Click Connect Function For the Exit Button----------
        exit_item.triggered.connect(self.exit_conn)
        file.addAction(exit_item)

        ##### Toolbar  #####
        # ----------Creating a Main toolbar----------
        tb = self.addToolBar("My Toolbar")

        # ----------Creating a toolbar item with its Icon (New File)----------
        newtb = QAction(QIcon("/home/hashim/MyQT_Tutorials/Advance PyQT Widgets/Resources-Advanced-PyQt5-Widgets-Using-Menu-Widget/folder.png"), "New Folder", self)
        # If we want to also add the text along with the item of toolbar we do as:
        #tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # Adding the toolbar item to the toolbar
        tb.addAction(newtb)

        # ----------Creating a toolbar item with its Icon (Open Tab )----------
        opentb = QAction(QIcon("/home/hashim/MyQT_Tutorials/Advance PyQT Widgets/Resources-Advanced-PyQt5-Widgets-Using-Menu-Widget/empty.png"), "Open Folder", self)
        # If we want to also add the text along with the item of toolbar we do as
        #tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # Adding the toolbar item to the toolbar
        tb.addAction(opentb)

        # ----------Creating a toolbar item with its Icon (Safe Tab )----------
        safetb = QAction(QIcon("/home/hashim/MyQT_Tutorials/Advance PyQT Widgets/Resources-Advanced-PyQt5-Widgets-Using-Menu-Widget/save.png"), "Save File", self)
        # If we want to also add the text along with the item of toolbar we do as :
        #tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # Adding the toolbar item to the toolbar
        tb.addAction(safetb)

        # ----------Creating a toolbar item with its Icon (Exit Tab )----------
        exittb = QAction(QIcon("/home/hashim/MyQT_Tutorials/Advance PyQT Widgets/Resources-Advanced-PyQt5-Widgets-Using-Menu-Widget/exit.png"), "Exit", self)
        # If we want to also add the text along with the item of toolbar we do as :
        #tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # Creating a click and connect Button for the Exit Icon
        exittb.triggered.connect(self.exit_conn)
        # Adding the toolbar item to the toolbar
        tb.addAction(exittb)

        #---------- Creating a Main Function for the Buttons in the toolbar----------
        tb.actionTriggered.connect(self.btnFunc)

        # ----------Creating a combo box----------
        # Initialize a Combo Box
        self.combo = QComboBox()
        # Adding Items to the Combo Box
        self.combo.addItems(["Spider Man", "Super Man", "Bat Man", "Hashim"])
        # Adding the Combo box to the Toolbar using .addWidget
        tb.addWidget(self.combo)

        ##### Show Window #####
        self.show()

    def exit_conn(self):
        # Creating a Message Box to ask user to confirm action
        mbox = QMessageBox.information(self, "Warning", "Are you sure to exit", QMessageBox.Yes| QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()

    def btnFunc(self, btn):
        if btn.text() == "New Folder":
            print("You Clicked New Button")
        elif btn.text() == "Open Folder":
            print("You Clicked Open Button")
        else:
            print("You Clicked Safe Button")



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
