from PyQt6.QtWidgets import QDialog, QLabel, QGridLayout, QComboBox, QPushButton
import data_manager

class EditStudentDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        # get values from main window to preload widgets later
        main_window = self.parent()
        table_index = main_window.table.currentRow()
        self.enrollment_id = int(main_window.table.item(table_index, 0).text())
        original_name = main_window.table.item(table_index, 2).text()
        original_course = main_window.table.item(table_index, 3).text()

        self.setWindowTitle("Update Student Enrollment")
        self.setFixedWidth(400)
        self.setFixedHeight(200)

        # QVBoxLayout give us a more vertical layout
        layout = QGridLayout()

        students = data_manager.load_students()
        # create widgets for adding student name
        name_label = QLabel("Current Student")
        original_name_label = QLabel(original_name)
        new_name_label = QLabel("Change student, if applicable")
        self.student_box = QComboBox()
        for student_id, student_name in students:
            self.student_box.addItem(student_name, student_id)

        # set initial value based on main table row selected
        index = self.student_box.findText(original_name)
        self.student_box.setCurrentIndex(index)

        # add student name widgets to layout
        layout.addWidget(name_label, 0, 0)
        layout.addWidget(original_name_label, 0, 1)
        layout.addWidget(new_name_label, 1, 0)
        layout.addWidget(self.student_box, 1, 1)

        # load list of courses from the course database
        courses = data_manager.load_courses()

        # create widgets for course selection
        course_label = QLabel("Current Course Enrolled")
        original_course_label = QLabel(original_course)
        new_course_label = QLabel("Change course, if applicable")
        # combobox creates a dropdown widget
        self.course_box = QComboBox()
        self.course_box.addItems(courses)
        index = self.course_box.findText(original_course)
        self.course_box.setCurrentIndex(index)

        # add course widgets to layout
        layout.addWidget(course_label, 2, 0)
        layout.addWidget(original_course_label, 2, 1)
        layout.addWidget(new_course_label, 3, 0)
        layout.addWidget(self.course_box, 3, 1)

        # add enrollment button to send the entry to the database
        enroll_button = QPushButton("Update Enrollment")
        enroll_button.clicked.connect(self.update_student)

        # add the enrollment button to the layout
        layout.addWidget(enroll_button, 4, 0, 1, 2)

        # add layout to window
        self.setLayout(layout)

    def update_student(self):
        data_manager.update_enrollment(enrollment_id=self.enrollment_id, student_name=self.student_box.currentText(), course_id=self.course_box.currentText())
        self.close()