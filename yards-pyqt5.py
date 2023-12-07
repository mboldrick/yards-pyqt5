import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """Initialize the window and display its contents to the screen."""
        self.setWindowTitle("Swim Distance Conversion")
        self.setGeometry(100, 100, 400, 230)
        self.converterUserInterface()

        self.show()

    def converterUserInterface(self):
        """Build the user interface for the converter."""
        # Create the widgets
        self.yards_label = qtw.QLabel("Yards:", self)
        self.yards_input = qtw.QLineEdit(self)
        self.yards_input.setPlaceholderText("Enter yards here")
        self.yards_input.setValidator(qtg.QIntValidator(0, 1000000, self))

        self.meters_label = qtw.QLabel("Meters:", self)
        self.meters_display = qtw.QLineEdit(self)
        # self.meters_display.setAlignment(qtc.Qt.AlignRight)

        self.convert_btn = qtw.QPushButton("Convert", self)
        self.convert_btn.clicked.connect(self.convertDistance)

        # Create the layout
        grid_layout = qtw.QGridLayout()
        grid_layout.addWidget(self.yards_label, 0, 0)
        grid_layout.addWidget(self.yards_input, 0, 1)
        grid_layout.addWidget(self.convert_btn, 0, 2)
        grid_layout.addWidget(self.meters_label, 0, 3)
        grid_layout.addWidget(self.meters_display, 0, 4)
        self.setLayout(grid_layout)

    def convertDistance(self):
        """Convert the distance from yards to meters."""
        # Get the yards value from the input field
        yards = self.yards_input.text()

        # Convert yards to meters
        meters = int(yards) * 0.9144

        # Display the result
        self.meters_display.setText(str(meters))


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
