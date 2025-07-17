from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QDialog, QPushButton
import data_manager

class AddStudentDialog(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # create student name widgets
        name_label = QLabel("Student's Name")
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("First Last")

        # add student name to layout
        layout.addWidget(name_label)
        layout.addWidget(self.name_edit)

        # create mobile number widgets
        mobile_label = QLabel("Student's Mobile Phone Number")
        self.mobile_number = QLineEdit()
        self.mobile_number.setPlaceholderText("###-###-####")

        # add mobile number widgets to layout
        layout.addWidget(mobile_label)
        layout.addWidget(self.mobile_number)

        # create add student button to send the entry to the database
        add_student = QPushButton("Add Student")
        add_student.clicked.connect(self.add_student)

        # add the enrollment button to the layout
        layout.addWidget(add_student)

        # add layout to window
        self.setLayout(layout)

    def add_student(self):
        data_manager.add_student(self.name_edit.text(), self.mobile_number.text())
        self.close()