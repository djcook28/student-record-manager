from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, \
    QToolBar, QStatusBar, QPushButton, QMessageBox
from PyQt6.QtGui import QAction, QIcon
from status_bar.search_student_dialog import SearchStudentDialog
from status_bar.enroll_student_dialog import EnrollStudentDialog
from status_bar.add_student_dialog import AddStudentDialog
from tool_bar.delete_student_dialog import DeleteStudentDialog
import data_manager
import sys
import sqlite3

from tool_bar.edit_student_dialog import EditStudentDialog


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
        add_student_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        enroll_student_action = QAction(QIcon("icons/enroll.png"), "Enroll Student", self)
        file_menu_item.addAction(add_student_action)
        file_menu_item.addAction(enroll_student_action)

        # when add student is clicked, will call the add function to open the add student popup widget
        add_student_action.triggered.connect(self.add_student)
        enroll_student_action.triggered.connect(self.enroll_student)

        # add an option under edit for searching by student name
        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        edit_menu_item.addAction(search_action)

        # connect a function to trigger when search is clicked
        search_action.triggered.connect(self.search)

        # adds an about menu option under help
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        # creates a table with 4 columns
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(("Enrollment ID", "Student Id", "Name", "Course ID", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        # enrollment ID is needed later to ensure correct database row is modified but is not needed by the user
        self.table.setColumnHidden(0, True)

        # Adds the table to the main window under the menu bar and above the status bar
        self.setCentralWidget(self.table)

        # call cell_clicked when a cell in the table is clicked
        self.table.cellClicked.connect(self.cell_clicked)

        # Create tool bar
        tool_bar = QToolBar()
        tool_bar.setMovable(True)
        self.addToolBar(tool_bar)

        # Add actions to tool bar
        tool_bar.addAction(search_action)
        tool_bar.addAction(enroll_student_action)

        # create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def create_table(self, row_list):
        # resets table to 0 on each refresh so records don't keep getting appended repeatedly
        self.table.setRowCount(0)

        # iterates over the results which is a list of tuples to get each tuple
        for row_number, row_data in enumerate(row_list):
            self.table.insertRow(row_number)
            # iterates over each tuple and inserts the tuple values into the table
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.table.resizeColumnsToContents()

    def load_data(self):
        # loads current student enrollment records from the database
        results = data_manager.load_main_table()
        if results:
            self.create_table(results)

    def load_name_filtered_data(self, student_name):
        # loads current student enrollment records from the database
        results = data_manager.load_main_table(student_name)
        if results:
            self.create_table(results)

    # creates the enroll student popup window
    def enroll_student(self):
        dialog = EnrollStudentDialog()
        dialog.exec()
        self.load_data()

    # creates the enroll student popup window
    def add_student(self):
        dialog = AddStudentDialog()
        dialog.exec()
        self.load_data()

    def search(self):
        dialog = SearchStudentDialog(self)
        dialog.exec()

    def cell_clicked(self):
        # create edit and delete button
        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(self.edit_student_enrollment)
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_student_enrollment)

        for child in self.status_bar.findChildren(QPushButton):
            self.status_bar.removeWidget(child)
        self.status_bar.addWidget(edit_button)
        self.status_bar.addWidget(delete_button)

    def edit_student_enrollment(self):
        edit_student = EditStudentDialog(self)
        edit_student.exec()
        self.load_data()

    def delete_student_enrollment(self):
        delete_student = DeleteStudentDialog(self)
        delete_student.exec()
        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Deletion Confirmation")
        confirmation_widget.setText("Record Deleted")
        confirmation_widget.exec()
        self.load_data()

app = QApplication(sys.argv)
main_window = MainWidget()
main_window.load_data()
main_window.show()
sys.exit(app.exec())
