# Open File : How we can use Open file and other file dialogs
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt  # WE use Qt lib to get the horizontal sliders else we have vertical sliders
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        ##### Creat a Window #####
        self.setWindowTitle("Open File Dialog")
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        ##### Create Layout  #####
        #----- Creat Horizontal and Vertical Layouts
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        # Create A Text Editor
        self.editor = QTextEdit()

        # Create a Button
        fileButton = QPushButton("Open File")
        fileButton.clicked.connect(self.openFile)

        # Add editor widget to the Vertical layout
        vbox.addWidget(self.editor)
        # Add Horizontal Layout to the Vertical layout
        vbox.addLayout(hbox)

        # Add File Button to the Horizontal layout
        hbox.addStretch()
        hbox.addWidget(fileButton)
        hbox.addStretch()


        # Set the Vertical Layout on the main Window
        self.setLayout(vbox)

        ##### Show Window #####
        self.show()

    def openFile(self):
        # In order to open a file we need its url. We can create its url as follow:
        # QFileDialog.getOpenFileName(self, "Window title", "If you want to open at some specific URL else none",
        # "Extension of the file (name* ;; *extension)")
        url = QFileDialog.getOpenFileName(self, "Open A File", "", "All Files(*);;*txt")
        # Here we will get the path of the file which Will be at index 0
        print(url)
        # As the URL of our file is at Index 0 we will get that from url variable
        filepath = url[0]
        print("Url Path ", filepath)
        # We need to Open and read the file and display it in our text editor
        # First we open the file in the read only mode from its URL
        file = open(filepath, 'r')
        # We read the content from the file and save it in a string
        content = file.read()
        # We add the text extracted from the file to our text editor
        self.editor.setText(content)



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
