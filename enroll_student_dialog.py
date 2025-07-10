from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QLineEdit, QComboBox, QApplication, QPushButton
import sqlite3
import sys

class EnrollStudentDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enroll Student")
        self.setFixedWidth(300)
        self.setFixedHeight(200)

        # QVBoxLayout give us a more vertical layout
        layout = QVBoxLayout()

        # create widgets for adding student name
        name_label = QLabel("Student Name")
        self.student_name = QLineEdit()
        self.student_name.setText("First Last")

        # add student name widgets to layout
        layout.addWidget(name_label)
        layout.addWidget(self.student_name)

        # load list of courses from the course database
        courses = self.load_courses()

        # create widgets for course selection
        course_label = QLabel("Course Enrolled")
        # combobox creates a dropdown widget
        self.course_box = QComboBox()
        self.course_box.addItems(courses)

        # add course widgets to layout
        layout.addWidget(course_label)
        layout.addWidget(self.course_box)

        # add mobile number widget
        mobile_label = QLabel("Student's Mobile Phone Number")
        self.mobile_number = QLineEdit()
        self.mobile_number.setText("###-###-####")

        # add mobile number widgets to layout
        layout.addWidget(mobile_label)
        layout.addWidget(self.mobile_number)

        # add enrollment button to send the entry to the database
        enroll_button = QPushButton("Submit Enrollment")
        enroll_button.clicked.connect(self.enroll_student)

        # add the enrollment button to the layout
        layout.addWidget(enroll_button)

        # add layout to window
        self.setLayout(layout)

    # loads master list of courses from database
    def load_courses(self):
        connection = sqlite3.connect("course_record.db")
        results = connection.execute("SELECT course_title FROM courses")
        # results is a database object that consists of a list of tuples
        results = list(results)
        connection.close()

        # loop through the list of tuples to create just a list
        courses = []
        for tuple in results:
            for item in tuple:
                courses.append(item)
        return courses

    # write new enrollment record to the database
    def enroll_student(self):
        connection = sqlite3.connect("student_record.db")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO student_records (name, course, mobile_phone) values (?, ?, ?)",
                       (self.student_name.text(), self.course_box.currentText(), self.mobile_number.text()))
        # commit the draft change to the database
        connection.commit()
        cursor.close()
        connection.close()
        self.close()