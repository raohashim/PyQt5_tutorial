#
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QTimer
import sqlite3
# We use the pillow package for uploading the images
from PIL import Image


# Now we will create a database for out Employee
# To create a database we set a Connection and Cursor
con = sqlite3.connect("Employees.db")  # .db is our database
cor = con.cursor()
# For adding the tables to our database we will use the DB for SQLite app.

# Default Image: If our Employee dont have any Image to add
default_Image = "/home/hashim/MyQT_Tutorials/Employees App/Resources-My-Employees-App-What-we-are-Going-to-Build/icons"

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employee")
        self.setGeometry(450,150,750,600)
        self.UI()
        self.show()

    def UI(self):

        self.layouts()
        self.mainDesign()
        self.getEmployee()
        self.disply_first_record()

    def layouts(self):
        # Main Layout
        self.main_lay = QHBoxLayout()
        # Form Layout to show the Employee Data
        self.left_lay = QFormLayout()
        # Layout showing the Employee Names
        self.main_right_lay = QVBoxLayout()
        # For the employee
        self.top_right_lay = QVBoxLayout()
        # Layout for Buttons
        self.bottom_right_lay = QHBoxLayout()
        # ----------------------------------------
        # Adding Layouts to Right Layouts
        self.main_right_lay.addLayout(self.top_right_lay)
        self.main_right_lay.addLayout(self.bottom_right_lay)

        # Adding Layouts to the main layout
        self.main_lay.addLayout(self.left_lay, 40)  # Adding the aspect ratio for the layout
        self.main_lay.addLayout(self.main_right_lay, 60)  # Adding the aspect ratio for the layout
        # Show the main Layout on our Window
        self.setLayout(self.main_lay)

    def mainDesign(self):
        self.setStyleSheet("font-size:14pt;font-family:Arial bold")
        #-------------Right Layout Design------------
        # Adding List layout to Right top Layout
        self.list = QListWidget()
        # Creating a single click to display the record of the employ on the Main Window
        self.list.itemClicked.connect(self.single_clicked_event)
        # Adding Widgets to Right top Layout
        self.top_right_lay.addWidget(self.list)

        # Creating buttons for the Right bottom Layout
        self.new_btn = QPushButton("New")
        self.new_btn.clicked.connect(self.add_new_Employee)

        self.update_btn = QPushButton("Update")
        #self.update_btn.clicked.connect(self.)

        self.del_btn = QPushButton("Delete")
        self.del_btn.clicked.connect(self.del_record)

        # Adding buttons to the Right Bottom layout
        self.bottom_right_lay.addWidget(self.new_btn)
        self.bottom_right_lay.addWidget(self.update_btn)
        self.bottom_right_lay.addWidget(self.del_btn)

    def add_new_Employee(self):
        # First we create a new Instance for the New Class
        self.newEmployee = AddEmployee()

        # To close our main window
        self.close()

    def getEmployee(self):
        # Create a query to get the values from the Employee Database
        query = "SELECT Id, Name, SurName FROM Employee"
        # Execute the Query to fetch the data
        employees = cor.execute(query).fetchall()
        # Use the for loop to get all the records from the Database
        for employee in employees:
            self.list.addItem(str(employee[0]) + "- " + str(employee[1]) + " " + str(employee[2]))

    def disply_first_record(self):
        # Create a query to get the values from the Employee Database
        query = "SELECT * FROM Employee ORDER BY ROWID ASC LIMIT 1"
        #
        employee_1 = cor.execute(query).fetchone()
        img = QLabel()

        name = QLabel(employee_1[1])
        sur_name = QLabel(employee_1[2])
        phone = QLabel(employee_1[3])
        email = QLabel(employee_1[4])
        address = QLabel(employee_1[6])
        img.setPixmap(QPixmap(employee_1[5]))
        # Vertical Spacing
        self.left_lay.setVerticalSpacing(20)
        self.left_lay.addRow("", img)
        self.left_lay.addRow("Name: ", name)
        self.left_lay.addRow("Sur Name: ", sur_name)
        self.left_lay.addRow("Phone No.:", phone)
        self.left_lay.addRow("Email Id: ", email)
        self.left_lay.addRow("Address: ", address)

    # This function will show the record of the Employ on which we Single Clicked Mouse
    def single_clicked_event(self):
        # To remove the Widgets from the Layout
        for i in reversed(range(self.left_lay.count())):
            #print (i)
            widget = self.left_lay.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        #
        employee = self.list.currentItem().text()
        id = employee[0]
        print(id)
        query = "SELECT * FROM Employee WHERE id=?"
        employee_rec = cor.execute(query,(id,)).fetchall()
        #print (employee_rec)
        img = QLabel()
        print(employee_rec)
        img.setPixmap(QPixmap(employee_rec[5]))
        name = QLabel(employee_rec[1])
        sur_name = QLabel(employee_rec[2])
        phone = QLabel(employee_rec[3])
        email = QLabel(employee_rec[4])
        address = QLabel(employee_rec[6])
        img.setPixmap(QPixmap(employee_rec[5]))
        # Vertical Spacing
        self.left_lay.setVerticalSpacing(20)
        self.left_lay.addRow("", img)
        self.left_lay.addRow("Name: ", name)
        self.left_lay.addRow("Sur Name: ", sur_name)
        self.left_lay.addRow("Phone No.:", phone)
        self.left_lay.addRow("Email Id: ", email)
        self.left_lay.addRow("Address: ", address)


    def del_record(self):
        employ = self.list.currentItem().text()
        id = employ[0]
        mbox = QMessageBox.question(self, "Warning", "Are you sure to delete this employ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                query = "DELETE FROM Employee WHERE id=?"
                print(id)
                cor.execute(query, (id,))
                con.commit()
                QMessageBox.information(self, "The record is deleted")
                # To update Window
                self.close()
                self.main = Main()

            except:
                QMessageBox.information(self, "Warning", "User is not Deleted")
                self.close()
                self.main = Main()



class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employ")
        self.setGeometry(450, 150, 350, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layout()

    # the function help to switch between Windows
    def closeEvent(self, event):

        # We will add a new instance form the main class
        self.main = Main()


    def layout(self):
        # Create the layout for the main Window
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()

        # Adding Widgets to top layout
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget(self.img_add)
        self.top_layout.addStretch()
        # To set the margins for our windows
        self.top_layout.setContentsMargins(110, 20, 10, 30)  # loft,top, right, bottom

        # Adding Widgets to Bottom Layout
        self.bottom_layout.addRow(self.get_name_text, self.get_name)
        self.bottom_layout.addRow(self.get_sur_name_text, self.get_sur_name)
        self.bottom_layout.addRow(self.get_ph_no_text, self.get_ph_no)
        self.bottom_layout.addRow(self.get_email_text, self.get_email)
        self.bottom_layout.addRow(self.get_img_text, self.get_img)
        self.bottom_layout.addRow(self.get_adress_text, self.get_adress)
        self.bottom_layout.addRow("", self.get_add)  #If we want to add an emplty row
        #self.bottom_layout.addWidget(self.get_add)

        # Adding Layout to main windows
        self.main_layout.addLayout(self.top_layout, 30)
        self.main_layout.addLayout(self.bottom_layout, 70)

        # Set Layout on Main Window
        self.setLayout(self.main_layout)

    def mainDesign(self):
        # Creating top layout widgets
        #  To set the background color of our window
        self.setStyleSheet("background-color:white;font-size:14pt")
        self.title = QLabel("Add Person")
        # To Change the font size and shape we use setstylesheet
        self.title.setStyleSheet('font-size :24pt; font-family: Arial Bold')

        self.img_add = QLabel()
        self.img_add.setPixmap(QPixmap("/home/hashim/MyQT_Tutorials/Employees App/Resources-My-Employees-App-What-we-are-Going-to-Build/icons/person.png"))

        # Creating the widgets for the Bottom Layout
        self.get_name_text = QLabel("Name: ")
        self.get_name_text.setStyleSheet('font-size :10pt; font-family: Arial')
        self.get_name = QLineEdit(self)
        self.get_name.setPlaceholderText("Enter your Name Here")
        self.get_name.setStyleSheet('font-size :10pt; font-family: Arial')

        self.get_sur_name_text = QLabel("Surname: ")
        self.get_sur_name_text.setStyleSheet('font-size :10pt; font-family: Arial')
        self.get_sur_name = QLineEdit(self)
        self.get_sur_name.setPlaceholderText("Enter your Surname Here")
        self.get_sur_name.setStyleSheet('font-size :10pt; font-family: Arial')

        self.get_ph_no_text = QLabel("Phone No: ")
        self.get_ph_no_text.setStyleSheet('font-size :10pt; font-family: Arial')
        self.get_ph_no = QLineEdit(self)
        self.get_ph_no.setPlaceholderText("Enter your Phone No. Here")
        self.get_ph_no.setStyleSheet('font-size :10pt; font-family: Arial')

        self.get_email_text = QLabel("Email ID: ")
        self.get_email_text.setStyleSheet('font-size :10pt; font-family: Arial')
        self.get_email = QLineEdit(self)
        self.get_email.setPlaceholderText("Enter your email Here")
        self.get_email.setStyleSheet('font-size :10pt; font-family: Arial')

        self.get_img_text = QLabel("Select Image: ")
        self.get_img_text.setStyleSheet('font-size :10pt; font-family: Arial')
        self.get_img = QPushButton("Open Image")
        self.get_img.setStyleSheet("background-color:orange;font-size :10pt; font-family: Arial")
        self.get_img.clicked.connect(self.uploadImage)

        self.get_adress_text = QLabel("Adress: ")
        self.get_adress_text.setStyleSheet('font-size :10pt; font-family: Arial')
        self.get_adress = QTextEdit(self)
        self.get_adress.setPlaceholderText("Enter your Adress Here")
        self.get_adress.setStyleSheet('font-size :10pt; font-family: Arial')

        self.get_add = QPushButton("Add")
        self.get_add.setStyleSheet("background-color:orange;font-size :10pt; font-family: Arial")
        self.get_add.clicked.connect(self.entry_safe)

    def uploadImage(self):
        # If our user do not add their default Image
        global default_Image
        # define size for Image
        size = (128, 128)
        #
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload your Image', '', 'Image Files (*.jpg *.png)')
        if ok:
            # Only to get the File Name instead of Complete address
            default_Image = os.path.basename(str(self.fileName))
            # Open the Image
            #print(Image.open(self.fileName, "rb"))
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save("/home/hashim/MyQT_Tutorials/Employees App/Resources-My-Employees-App-What-we-are-Going-to-Build/images/{}".format(default_Image))


    def entry_safe(self):
        global default_Image
        # Get the values added to the Filed By the User
        name = self.get_name.text()
        surname = self.get_sur_name.text()
        phone = self.get_ph_no.text()
        email = self.get_email.text()
        img = default_Image
        address = self.get_adress.toPlainText()  # As we have to get value from the QTextEditor widget

        #
        if (name and surname and phone != ""):
            # If we want to make a datbase reconrd we use try and except report
            try:
                # Here we create a query which willl enter our record to our datatable
                query = "INSERT INTO Employee (Name, SurName, Phone, Email, Image, Address) VALUES(?,?,?,?,?,?)"
                # We use cources defined globaly earlier to link the Values to the Query
                cor.execute(query, (name, surname, phone, email, img, address))
                # If we want to make change in our database we use the commit function like add, delete etc.
                con.commit()
                QMessageBox.information(self, "Success", "Employ record Entered Successfully")

                # To get back to our main window after successfully entering the employ record
                self.close()
                self.closeEvent()
            except:
                QMessageBox.warning(self, "Warning", "Person has not been added")
        else:
            QMessageBox.information(self, "Warning", "Fields Cannot be Empty")


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

