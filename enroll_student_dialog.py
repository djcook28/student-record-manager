from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QLineEdit, QComboBox, QApplication, QPushButton
import sqlite3
import sys

class EnrollStudentDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enroll Student")
        self.setFixedWidth(400)
        self.setFixedHeight(200)

        # QVBoxLayout give us a more vertical layout
        layout = QVBoxLayout()

        students = self.load_students()
        # create widgets for adding student name
        name_label = QLabel("Student")
        self.student_box = QComboBox()
        for student_id, student_name in students:
            self.student_box.addItem(student_name, student_id)

        # add student name widgets to layout
        layout.addWidget(name_label)
        layout.addWidget(self.student_box)

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

        # add enrollment button to send the entry to the database
        enroll_button = QPushButton("Submit Enrollment")
        enroll_button.clicked.connect(self.enroll_student)

        # add the enrollment button to the layout
        layout.addWidget(enroll_button)

        # add layout to window
        self.setLayout(layout)

    # loads master list of courses from database
    def load_courses(self):
        connection = sqlite3.connect("school_master.db")
        results = connection.execute("SELECT course_id FROM courses")
        # results is a database object that consists of a list of tuples
        results = list(results)
        connection.close()

        # loop through the list of tuples to create just a list
        courses = []
        for tuple in results:
            for item in tuple:
                courses.append(item)
        return courses

    # loads master list of student from database
    def load_students(self):
        connection = sqlite3.connect("school_master.db")
        results = connection.execute("SELECT student_id, student_name FROM students")
        # results is a database object that consists of a list of tuples
        results = list(results)
        connection.close()

        # loop through the list of tuples to create just a list
        return results

    # write new enrollment record to the database
    def enroll_student(self):
        connection = sqlite3.connect("school_master.db")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO student_enrollment (student_id, course_id) values (?, ?)",
                       (self.student_box.currentData(), self.course_box.currentText()))
        # commit the draft change to the database
        connection.commit()
        cursor.close()
        connection.close()
        self.close()