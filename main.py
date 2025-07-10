from PyQt6.QtWidgets import QGridLayout, QLabel, QApplication, QWidget, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction
from insert_dialog import InsertDialog
import sys
import sqlite3

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)

        self.setCentralWidget(self.table)

    def load_data(self):
        db = sqlite3.connect("student_record.db")
        results = db.execute("SELECT * FROM student_records")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        db.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

app = QApplication(sys.argv)
main_window = MainWidget()
main_window.load_data()
main_window.show()
sys.exit(app.exec())
