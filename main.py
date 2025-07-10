from PyQt6.QtWidgets import QGridLayout, QLabel, QApplication, QWidget, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction
from search_student_dialog import SearchStudentDialog
from enroll_student_dialog import EnrollStudentDialog
import sys
import sqlite3

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        # creates top menu bar in the main window and adds File and Help menu selections
        file_menu_item = self.menuBar().addMenu("&File")
        edit_menu_item = self.menuBar().addMenu("&Edit")
        help_menu_item = self.menuBar().addMenu("&Help")

        # add a menu option for adding student under the file menu
        enroll_student_action = QAction("Enroll Student", self)
        file_menu_item.addAction(enroll_student_action)

        # when add student is clicked, will call the add function to open the add student popup widget
        enroll_student_action.triggered.connect(self.enroll_student)

        # add an option under edit for searching by student name
        search_action = QAction("Search", self)
        edit_menu_item.addAction(search_action)

        # connect a function to trigger when search is clicked
        search_action.triggered.connect(self.search)

        # adds an about menu option under help
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        # creates a table with 4 columns
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)

        # Adds the table to the main window under the menu bar and above the status bar
        self.setCentralWidget(self.table)

    def load_data(self):
        # loads current student enrollment records from the database
        connection = sqlite3.connect("student_record.db")
        results = connection.execute("SELECT * FROM student_records")

        # resets table to 0 on each refresh so records don't keep getting appended repeatedly
        self.table.setRowCount(0)

        # iterates over the results which is a list of tuples to get each tuple
        for row_number, row_data in enumerate(results):
            self.table.insertRow(row_number)
            # iterates over each tuple and inserts the tuple values into the table
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def load_name_filtered_data(self, student_name):
        # loads current student enrollment records from the database
        connection = sqlite3.connect("student_record.db")
        student_name = (student_name,)
        results = connection.execute("SELECT * FROM student_records WHERE name = (?)", student_name)

        # resets table to 0 on each refresh so records don't keep getting appended repeatedly
        self.table.setRowCount(0)

        # iterates over the results which is a list of tuples to get each tuple
        for row_number, row_data in enumerate(results):
            self.table.insertRow(row_number)
            # iterates over each tuple and inserts the tuple values into the table
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    # creates the enroll student popup window
    def enroll_student(self):
        dialog = EnrollStudentDialog()
        dialog.exec()
        self.load_data()

    def search(self):
        dialog = SearchStudentDialog(self)
        dialog.exec()

app = QApplication(sys.argv)
main_window = MainWidget()
main_window.load_data()
main_window.show()
sys.exit(app.exec())
