# Spin Box is the box In which we select the numerical value by clicking the up and down button
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

# Font family and font size
# the font supported by the OS is only adapted here
font = QFont("Times", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" <<Text Editor>>")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        # Create a label
        self.lable = QLabel("Enter your address here", self)
        self.lable.move(150, 80)

        # We create a text editor
        # They are used when we have long text to enter such as addresses, emails etc.
        self.editor = QTextEdit(self)
        self.editor.resize(100, 100)
        self.editor.move(150, 100)  # To set the size of the text box
        
        # If we don't want our editor to accept the rich text
        self.editor.setAcceptRichText(False)  # If we don't want our Editor to accept the rich text

        # Create a button to get the value from the text editor
        button = QPushButton("Send", self)
        button.move(326, 300)
        button.clicked.connect(self.getValue)

        self.show()

    def getValue(self):
        # To fetch the text from the editor
        text = self.editor.toPlainText()  # Rich Text like bold, italic etc.
        print(text)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
