import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, 
    QLineEdit, QPushButton, QMessageBox, QComboBox, QDateEdit, QListWidget,QInputDialog
)
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont, QIcon

# Initialize tasks.json if it doesn't exist
def init_data_file():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump({'tasks': []}, file)

# Load data from tasks.json
def load_data():
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            if "tasks" not in data:
                return {"tasks": []}
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return {"tasks": []}

# Save data to tasks.json
def save_data(data):
    with open('tasks.json', 'w') as file:
        json.dump(data, file, indent=4)

# PyQt Class for Task Manager
class TaskManagerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        self.setGeometry(200, 100, 500, 500)
        
        # Set a default icon if file not found
        icon_path = "icon.png" if os.path.exists("icon.png") else ""
        self.setWindowIcon(QIcon(icon_path))
        
        init_data_file()
        self.data = load_data()

        # Layout Setup
        self.main_layout = QVBoxLayout()
        self.form_layout = QGridLayout()
        
        # Title
        title_label = QLabel("Task Manager", self)
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setStyleSheet("color: #2c3e50;")
        self.main_layout.addWidget(title_label)
        
        # Task Description Input
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter task description")
        self.form_layout.addWidget(QLabel("Task Description:"), 0, 0)
        self.form_layout.addWidget(self.task_input, 0, 1)

        # Due Date Input
        self.date_input = QDateEdit(self)
        self.date_input.setDate(QDate.currentDate())
        self.form_layout.addWidget(QLabel("Due Date:"), 1, 0)
        self.form_layout.addWidget(self.date_input, 1, 1)

        # Priority Dropdown
        self.priority_input = QComboBox(self)
        self.priority_input.addItems(["Low", "Medium", "High"])
        self.form_layout.addWidget(QLabel("Priority:"), 2, 0)
        self.form_layout.addWidget(self.priority_input, 2, 1)

        # Add Task Button
        self.add_button = QPushButton("Add Task", self)
        self.add_button.setStyleSheet("background-color: #3498db; color: white;")
        self.add_button.clicked.connect(self.add_task)
        self.form_layout.addWidget(self.add_button, 3, 0, 1, 2)

        # Task List Display
        self.task_list = QListWidget(self)
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(QLabel("Tasks:"))
        self.main_layout.addWidget(self.task_list)

        # Load existing tasks into the list
        self.load_task_list()

        self.setLayout(self.main_layout)

        # Buttons for CRUD operations
        self.view_button = QPushButton("View Task", self)
        self.edit_button = QPushButton("Edit Task", self)
        self.delete_button = QPushButton("Delete Task", self)
        self.mark_complete_button = QPushButton("Mark as Completed", self)

        # Button Styling
        self.view_button.setStyleSheet("background-color: #1abc9c; color: white;")
        self.edit_button.setStyleSheet("background-color: #f39c12; color: white;")
        self.delete_button.setStyleSheet("background-color: #e74c3c; color: white;")
        self.mark_complete_button.setStyleSheet("background-color: #2ecc71; color: white;")

        # Connecting buttons to functions
        self.view_button.clicked.connect(self.view_task)
        self.edit_button.clicked.connect(self.edit_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.mark_complete_button.clicked.connect(self.mark_task_completed)

        # Add buttons to layout
        self.main_layout.addWidget(self.view_button)
        self.main_layout.addWidget(self.edit_button)
        self.main_layout.addWidget(self.delete_button)
        self.main_layout.addWidget(self.mark_complete_button)

    def add_task(self):
        description = self.task_input.text().strip()
        due_date = self.date_input.date().toString("yyyy-MM-dd")
        priority = self.priority_input.currentText()

        if not description:
            QMessageBox.warning(self, "Input Error", "Please enter a task description.")
            return

        task = {
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "completed": False
        }

        self.data['tasks'].append(task)
        save_data(self.data)
        self.load_task_list()

        self.task_input.clear()
        self.date_input.setDate(QDate.currentDate())

    def load_task_list(self):
        self.task_list.clear()
        for task in self.data['tasks']:
            status = "✔" if task['completed'] else "✖"
            self.task_list.addItem(f"{status} {task['description']} | Due: {task['due_date']} | Priority: {task['priority']}")

    def view_task(self):
        index = self.task_list.currentRow()
        if index < 0:
            QMessageBox.warning(self, "No Task Selected", "Select a task first.")
            return
        task = self.data['tasks'][index]
        QMessageBox.information(self, "Task Details", f"{task}")

    def edit_task(self):
        index = self.task_list.currentRow()
        if index < 0:
            QMessageBox.warning(self, "No Task Selected", "Select a task first.")
            return
        task = self.data['tasks'][index]
        new_desc, ok = QInputDialog.getText(self, "Edit Task", "Update Description:", text=task['description'])
        if ok and new_desc:
            task['description'] = new_desc
            save_data(self.data)
            self.load_task_list()

    def delete_task(self):
        index = self.task_list.currentRow()
        if index >= 0:
            self.data['tasks'].pop(index)
            save_data(self.data)
            self.load_task_list()

    def mark_task_completed(self):
        index = self.task_list.currentRow()
        if index >= 0:
            self.data['tasks'][index]['completed'] = not self.data['tasks'][index]['completed']
            save_data(self.data)
            self.load_task_list()

# Run App
def main():
    app = QApplication(sys.argv)
    window = TaskManagerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
