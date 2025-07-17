from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel


class DeleteStudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        student_name_label = QLabel(parent)