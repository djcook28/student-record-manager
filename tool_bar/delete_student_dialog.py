from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
import data_manager

class DeleteStudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # get values from main window to load widgets
        main_window = self.parent()
        table_index = main_window.table.currentRow()
        self.enrollment_id = int(main_window.table.item(table_index, 0).text())
        name = main_window.table.item(table_index, 2).text()
        course = main_window.table.item(table_index, 3).text()

        self.setWindowTitle("Delete Student Enrollment Record")
        self.setFixedWidth(400)
        self.setFixedHeight(100)

        layout = QVBoxLayout()

        student_name_label = QLabel(f"Student Name: {name}")
        course_label = QLabel(f"Enrolled Course: {course}")

        layout.addWidget(student_name_label)
        layout.addWidget(course_label)

        disenroll_button = QPushButton("Delete Record")
        disenroll_button.clicked.connect(self.disenroll)

        layout.addWidget(disenroll_button)

        self.setLayout(layout)

    def disenroll(self):
        data_manager.disenroll_student(self.enrollment_id)
        self.close()