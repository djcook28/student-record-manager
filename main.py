from PyQt6.QtWidgets import QGridLayout, QLabel, QApplication, QWidget
import sys

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        file_label = QLabel("File")
        help_label = QLabel("Help")

        grid.addWidget(file_label, 0, 0)
        grid.addWidget(help_label, 0, 1)

        self.setLayout(grid)

app = QApplication(sys.argv)
main_window = MainWidget()
main_window.show()
sys.exit(app.exec())
