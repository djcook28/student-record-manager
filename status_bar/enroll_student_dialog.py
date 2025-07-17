from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QLineEdit, QComboBox, QApplication, QPushButton
import data_manager

class EnrollStudentDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enroll Student")
        self.setFixedWidth(400)
        self.setFixedHeight(200)

        # QVBoxLayout give us a more vertical layout
        layout = QVBoxLayout()

        students = data_manager.load_students()
        # create widgets for adding student name
        name_label = QLabel("Student")
        self.student_box = QComboBox()
        for student_id, student_name in students:
            self.student_box.addItem(student_name, student_id)

        # add student name widgets to layout
        layout.addWidget(name_label)
        layout.addWidget(self.student_box)

        # load list of courses from the course database
        courses = data_manager.load_courses()

        # create widgets for course selection
        course_label = QLabel("Course Enrolled")
        # combobox creates a dropdown widget
        self.course_box = QComboBox()
        self.course_box.addItems(courses)

        # add course widgets to layout
        layout.addWidget(course_label)
        layout.addWidget(self.course_box)

        # add enrollment button to send the entry to the database
        enroll_button = QPushButton("Submit Enrollment")
        enroll_button.clicked.connect(self.enroll_student)

        # add the enrollment button to the layout
        layout.addWidget(enroll_button)

        # add layout to window
        self.setLayout(layout)

    # write new enrollment record to the database
    def enroll_student(self):
        data_manager.enroll_student(self.student_box.currentData(), self.course_box.currentText())
        self.close()