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
        self.setGeometry(100, 100, 400, 120)
        self.converterUserInterface()

        self.show()

    def converterUserInterface(self):
        """Build the user interface for the converter."""
        # Create the widgets
        self.instructions_label = qtw.QLabel(
            "Enter a distance in yards or meters. The other value will populate dynamically.",
            self,
        )
        self.instructions_label.setWordWrap(True)
        self.instructions_label.setAlignment(qtc.Qt.AlignTop)

        self.yards_label = qtw.QLabel("Yards:", self)
        self.yards_input = qtw.QLineEdit(self)
        # self.yards_input.setPlaceholderText("Enter yards here")
        self.yards_input.setValidator(qtg.QDoubleValidator(0, 1_000_000, 2, self))

        self.meters_label = qtw.QLabel("Meters:", self)
        self.meters_input = qtw.QLineEdit(self)
        self.meters_input.setValidator(qtg.QDoubleValidator(0, 1_000_000, 2, self))
        # self.meters_input.setAlignment(qtc.Qt.AlignRight)

        self.yards_input.textEdited.connect(self.convertYardsToMeters)
        self.meters_input.textEdited.connect(self.convertMetersToYards)

        # Create the layout
        grid_layout = qtw.QGridLayout()
        grid_layout.addWidget(self.instructions_label, 0, 0, 1, 5)
        grid_layout.addWidget(self.yards_label, 1, 0)
        grid_layout.addWidget(self.yards_input, 1, 1)
        grid_layout.addWidget(qtw.QLabel("=", self), 1, 2)
        grid_layout.addWidget(self.meters_label, 1, 3)
        grid_layout.addWidget(self.meters_input, 1, 4)
        grid_layout.setAlignment(qtc.Qt.AlignCenter)
        grid_layout.setVerticalSpacing(20)
        self.setLayout(grid_layout)

    def convertYardsToMeters(self):
        """Convert the distance from yards to meters."""
        # Get the yards value from the input field and remove commas
        yards = self.yards_input.text().replace(",", "")
        # Check if the input string is empty
        if yards:
            try:
                # Cast the input to a number, then convert it to meters (assuming 1 meter = 1.09361 yards)
                meters = float(yards) * 0.9144
                # Format the result so that it doesn't have trailing zeros
                formatted_meters = f"{meters:,.4f}".rstrip("0").rstrip(".")
                # Display the result
                self.meters_input.setText(formatted_meters)
            except ValueError:
                # Handle the case where the conversion to float fails
                # TODO - add an error message to the UI
                self.meters_input.setText("")
        else:
            self.meters_input.setText("")

    def convertMetersToYards(self):
        """Convert the distance from meters to yards."""
        # Get the meters value from the input field and remove commas
        meters = self.meters_input.text().replace(",", "")
        # Check if the input string is empty
        if meters:
            try:
                # Cast the input to a number, then convert it to yards (assuming 1 meter = 1.09361 yards)
                yards = float(meters) * 1.09361
                # Format the result so that it doesn't have trailing zeros
                formatted_yards = f"{yards:,.4f}".rstrip("0").rstrip(".")
                # Display the result
                self.yards_input.setText(formatted_yards)
            except ValueError:
                # Handle the case where the conversion to float fails
                # TODO - add an error message to the UI
                self.yards_input.setText("")
        else:
            self.yards_input.setText("")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
