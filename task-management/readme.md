# Task Manager App

A simple Task Manager application built using PyQt5 and Python that allows users to create, view, edit, delete, and mark tasks as completed. This application stores the task data in a `tasks.json` file.

## Features

- **Add Task**: Allows users to add new tasks with a description, due date, and priority.
- **View Task**: View the details of a selected task.
- **Edit Task**: Edit the task description, due date, and priority.
- **Delete Task**: Remove a selected task from the list.
- **Mark Task as Completed**: Toggle the task status between completed and not completed.

## Requirements

- Python 3.x
- PyQt5

## Installation

1. Clone the repository or download the project files.

```bash
git clone <repository_url>
Install required dependencies using pip:
bash
Copy code
pip install pyqt5
Running the Application
Navigate to the directory where your project is located.
Run the task_manager.py script:
bash
Copy code
python task_manager.py
Features in Detail
Add Task
Users can add a task with a description, due date, and priority.
The task will be added to the task list and saved in the tasks.json file.
View Task
Users can view the details of a selected task, including its description, due date, priority, and completion status.
Edit Task
Users can update the description, due date, and priority of a selected task.
Delete Task
Users can delete a selected task. A confirmation dialog will appear before the task is permanently deleted.
Mark Task as Completed
Users can mark a task as completed. If a task is marked as completed, its status will be updated accordingly.
Project Structure
bash
Copy code
/task_manager
    ├── task_manager.py  # Main application script
    ├── tasks.json       # Stores the task data
    ├── README.md        # Project documentation
    └── icon.png         # Optional: Task Manager Icon
Troubleshooting
No tasks are being saved: Ensure that the tasks.json file is present in the project directory. If it's missing, the program will attempt to create one automatically when launched.
Error on launching: Ensure all required libraries (e.g., PyQt5) are installed.
License
This project is licensed under the MIT License - see the LICENSE file for details.
