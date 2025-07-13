from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit

class add_student(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        # add mobile number widget
        mobile_label = QLabel("Student's Mobile Phone Number")
        self.mobile_number = QLineEdit()
        self.mobile_number.setPlaceholderText("###-###-####")

        # add mobile number widgets to layout
        layout.addWidget(mobile_label)
        layout.addWidget(self.mobile_number)
