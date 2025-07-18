from PyQt6.QtWidgets import QMessageBox

class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About")

        content = """
        Application for managing student enrollment in courses and adding new students.
        You can search by student name by clicking the magnifying glass or going to Edit -> Search
        You can add new students under File -> Add New Student
        You can add new course enrollment records by clicking the enroll icon or under File -> Enroll
        Note that you can only enroll existing students to a course, if the student is new you will have to add them first
        Options to modify or delete existing enrollment records will appear at the bottom upon clicking an enrollment record on the main table
        """

        self.setText(content)