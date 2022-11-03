# Slider
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt  # WE use Qt lib to get the horizontal sliders else we have vertical sliders
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        ###################Creat an Empty Window################
        self.setWindowTitle("Slider Widget")
        self.setGeometry(50, 50, 600, 500)
        self.UI()

    def UI(self):
        ################### Slider Widget Initialization################
        vbox = QVBoxLayout()  # Create a Vertical Box Layout
        # Initialize a Slider
        self.slider= QSlider(Qt.Horizontal)  # Use Qt lib to get a horizontal slider else it will be vertical
        # Set the minimum value for the slider
        self.slider.setMinimum(30)
        # Set the maximum value for the slider
        self.slider.setMaximum(60)
        # Set the Tick Position for the slider
        self.slider.setTickPosition(QSlider.TicksAbove)
        # Set the tick Interval for the slider
        self.slider.setTickInterval(2)
        # Get back the value from the slider
        self.slider.valueChanged.connect(self.getValue)
        ######################### Lables #################
        self.text1 = QLabel("0")
        # Use the Qt lib to set the alignment of the text i.e center, middle etc
        self.text1.setAlignment(Qt.AlignCenter)
        self.text2 = QLabel("Hello Python")
        ####################Add widgets to the layout##############
        vbox.addStretch()
        vbox.addWidget(self.text1)  # Add Label 1
        vbox.addWidget(self.text2)  # Add Label 2
        vbox.addWidget(self.slider)  # Add Slider
        vbox.addStretch()
        #############Set the Vetrical Layout to the window###########
        self.setLayout(vbox)
        ############# Show Window ####################
        self.show()

    def getValue(self):
        # To get the value back from the slider
        value = self.slider.value()
        self.text1.setText(str(value))
        # To change the font using the slider
        font_size = self.slider.value()
        font = QFont("Times", font_size)
        self.text2.setFont(font)


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
