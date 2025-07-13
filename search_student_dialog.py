from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel


class SearchStudentDialog(QDialog):
    def __init__(self, main_widget):
        super().__init__()
        self.setWindowTitle("Search by Student Name")
        self.main_widget = main_widget

        self.setFixedHeight(100)
        self.setFixedWidth(150)

        layout = QVBoxLayout()

        self.search_name = QLineEdit()
        self.search_name.setPlaceholderText("First Last")

        self.error_label = QLabel()

        layout.addWidget(self.search_name)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search)

        layout.addWidget(search_button)
        layout.addWidget(self.error_label)

        self.setLayout(layout)

    def search(self):
        result = self.main_widget.load_name_filtered_data(self.search_name.text())
        if(result == None):
            self.error_label.setText("No student found")
        else:
            self.close()