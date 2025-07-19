🎓 Student Management System
A desktop GUI application built with PyQt6 and SQLite for managing student enrollment, course assignments, and basic CRUD operations. Designed with modular dialogs, an integrated toolbar, and a dynamically refreshed table interface.

🚀 Features
- Add New Students via a file menu action.
- Enroll Students in courses with a separate dialog.
- Search by Name through both the toolbar and edit menu.
- Edit/Delete Records with contextual buttons that appear on cell click.
- Persistent Data Storage using mysql.
- Hidden Columns for internal IDs to maintain clean UI and robust record tracking.

🧩 UI Structure

| Component | Role |
|-----------|------|
| QMainWindow | Hosts the central table, menu bar, tool bar, and status bar | 
| QTableWidget | Displays current enrollment records (6 columns, one hidden) | 
| QToolBar | Provides quick access to search/enroll actions | 
| QStatusBar | Dynamically shows Edit/Delete buttons when a record is selected | 
| QMenuBar | File/Edit/Help actions integrated with PyQt6 QAction triggers | 


🛠 Module Overview
- MainWidget — Primary window with table and all connected UI components.
- data_manager.py — Handles loading student records from SQLite.
- status_bar/*.py — Dialogs for searching, adding, and enrolling students.
- tool_bar/*.py — Dialogs for editing and deleting student records.

🗃 Table Columns
- Enrollment ID (hidden)
- Student ID
- Name
- Course ID
- Course
- Mobile

🧠 Usage
python main.py


Make sure school_master.db is correctly located relative to your script or use an absolute path inside data_manager.py.

🧪 Dependencies
- Python 3.9+
- PyQt6
- mysql 9.0.0

Install via pip:
pip install PyQt6


📂 File Structure

student-management/
│
├── icons/                     # PNG icons used in toolbar and menu items
│   └── [your_icon_files].png
│
├── status_bar/               # Dialogs for search, enroll, and add actions
│   ├── search_student_dialog.py
│   ├── enroll_student_dialog.py
│   ├── about_dialog.py
│   └── add_student_dialog.py
│
├── tool_bar/                 # Dialogs for edit and delete actions
│   ├── edit_student_dialog.py
│   └── delete_student_dialog.py
│
├── data_manager.py           # Handles SQLite DB interactions and data retrieval
├── main.py                   # MainWindow UI and QApplication launcher
└── school_master.db          # SQLite database (pre-created with required tables)

📌 Notes
- Hidden column (Enrollment ID) is essential for correctly identifying rows during edit/delete operations.
- When a table cell is clicked, the status bar buttons adapt based on the selected row.
- Database connection errors or missing tables will raise runtime exceptions — make sure schema is initialized.

Let me know if you want to add screenshots, update installation steps, or split this into contributor and usage sections. I'm happy to turn this into a full GitHub-ready documentation suite.
