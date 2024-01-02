# 0x15. API
## Learning Objectives
What should Bash scripting not be used for?
What is an API?
What is a REST API?
What are microservices?
What is the CSV format?
What is the JSON format?
Pythonic package and module name style
Pythonic Class name style
Pythonic Variable name style
Pythonic Function name style
Pythonic Constant name style
Significance of CapWords or CamelCase in Python


## Requirements
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3
All your files should end with a new line
The first line of all your files should be exactly “#!/usr/bin/python3”
Libraries imported in your Python files must be organised in alphabetical order.
A README.md file, at the root of the folder of the project, is mandatory.
Your code should use the pycodestyle (version 2.8.)
All your files must be executable
The length of your files will be tested using wc
All your modules should have documentation
You must use get to access a dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
Your code should not be executed when imported

## Tasks
0. Gather data from an API
Write a Python script “0-gather_data_from_an_API.py” that using this <link: REST API>, for a given employee ID, returns information about his/her TODO list progress.
Requirements
You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list progress in this format:
First line: “Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):”
Second and N next lines display the title of completed tasks in this format:
“TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)”

1. Export to CSV
Using what you did in the task #0, Write a script “1-export_to_CSV.py” that would extend your Python script to export data in CSV format.
Requirements
Records all tasks that are owned by this employee
Format must be:
“USER_ID”, “USERNAME”, “TASK_COMPLETED_STATUS”, “TASK_TITLE”
File name must be:
“USER_ID.csv”

2. Export to JSON
Using what you did in task 0, write a Python script “2-export_to_JSON.py” that extends your script to export data in the JSON format.

Requirements:
Records all tasks that are owned by this employee
Format must be: “{“USER_ID”: [{“task”: “TASK_TITLE”, “completed”: TASK_COMPLETED_STATUS, “username”: “USERNAME”}, {“task”: “TASK_TITLE”, “completed”: TASK_COMPLETED_STATUS, “username”: “USERNAME”}, …]}”
File name must be: “USER_ID.json”

3. Dictionary of list of dictionaries
Using what you did in the task 0, write a python script “” that extends your python script to export data  in the JSON format.
Requirements
Records all tasks from all employees
Format must be: “{ “USER_ID”: [ { “username”: “USERNAME”, “task”: “TASK_TITLE”, “completed”: TASK_COMPLETED_STATUS}, {“username”: “USERNAME”, “task”: “TASK_TITLE”, “completed”: TASK_COMPLETED_STATUS}, … ], “USER_ID”: [ {“username”: “USERNAME”, “task”: “TASK_TITLE”, “completed”: TASK_COMPLETED_STATUS}, {“username”: “USERNAME”, “task”: “TASK_TITLE”, “completed”: TASK_COMPLETED_STATUS}, …]}
File name must be: “todo_all_employees.json”

