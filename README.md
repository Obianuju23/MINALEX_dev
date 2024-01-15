WEBSTACK PORTFOLIO PROJECT for ALX SE Africa


# MINALEX Todo Flask App

![Task Manager App Logo](https://github.com/Obianuju23/MINALEX/blob/main/shots/landingpage.PNG?raw=true)

## Overview new

The Todo Flask App is a powerful task management tool designed to streamline your daily activities and enhance productivity. It provides a convenient, one-stop solution for users to organize tasks, discuss concerns, prioritize tasks, find quick resolutions to their pending to-do items and achieve their goals before due dates. Whether you're looking to organize your daily activities or keep track of project-related tasks, this app has you covered.

From this project, users can get a feel of what the web application is all about by having a "Logged Out Experience" and the routes that can be assessed by the user or customer includes:

- The landing page
- The Add new task tab
- The Review and edit task tab

## Key Features

- Efficient Task Management:** Seamlessly organize and prioritize your tasks for enhanced productivity.
- Collaborative Environment:** Foster collaboration by discussing tasks and sharing updates with team members.
- Swift Resolutions:** Quickly resolve pending issues and tasks to stay on top of your commitments.
- User-Friendly Interface:** Intuitive design for a seamless and enjoyable task management experience.
- Performs CRUD Operations:** Add new tasks,Read/list all tasks, update task details, and mark tasks as complete and can delete tasks.
- Prioritization:** Prioritize tasks by choosing between high, medium and low in that section.
- Persistence:** Your tasks are stored persistently, so you can access them across sessions and ensure to meet up with the due dates.


## How It Works

1. **Task Creation:**
   Easily create and manage tasks with just a few clicks.

2. **Discussion Forum:**
   Engage in discussions with team members to get insights and updates on tasks.

3. **Prioritization:**
   Prioritize tasks based on urgency and importance.

4. **Task Relegation:**
   Assigning task to individual or teams. 

5. **Task Completion:**
   Mark tasks as complete when they are done.

## DEVELOPMENT TOOLS

Some of the tools used for software development of this app are:

 
- Flask: A web framework for Python that simplifies the development of web applications.

- SQLite3 Module: A built-in Python module providing an interface to SQLite databases.

- HTML: HyperText Markup Language, used for structuring and presenting content on the web.

- CSS: Cascading Style Sheets, used for styling and layout of web pages.

- Jinja: Jinja2, a template engine for Python, commonly used with Flask to generate dynamic content.

- SQLite Team Viewer: A tool for viewing and managing SQLite databases.

- DataGrip App: An integrated development environment (IDE) for working with databases, including SQLite.


## Getting Started

1. **Installation:**
   Clone the repository and install dependencies.

   ```bash
   git clone https://github.com/your-username/MINALEX.git
   
## Install virtual Environment
sudo apt update
sudo apt upgrade -y
sudo apt install virtualenv -y

## Creating a Virtual Environment
python3 -m venv portfolio

## Activating the virtual Environment

### on a unix based operating system
source portfolio/bin/activate
(portfolio) /home/nerd $

### on a windows based operating system
portfolio\Scripts\activate.bat
(portfolio) C:\Users\nerd>

## Deactivating a Virtual Environment
(portfolio) /home/nerd $ deactivate
   
## INSTALLING DEPENDENCIES
We have saved the dependencies in a file named requirement.txt

(portfolio) /home/nerd $ pip freeze > requirements.txt
- blinker==1.7.0
- click==8.1.7
- flask==3.0.0
- greenlet==3.0.2
- importlib-metadata==7.0.0
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.3
- typing-extensions==4.9.0
- werkzeug==3.0.1
- zipp==3.17.0

## INSTALL DEPENDENCIES
(portfolio) /home/nerd $ pip install -r requirements.txt

## RUNNING THE APPLICATION
To run MINALEX Task Manager application using command line, do the following:

### Step One
(portfolio) /home/nerd $ python app.py

OR

### Step Two
(portfolio) /home/nerd $ FLASK_APP=app.py
(portfolio) /home/nerd $ FLASK_DEBUG=1
(portfolio) /home/nerd $ flask run

Both will give you the output:

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.28.87.20:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 659-121-357

**AUTHOR**

Christiana Aghara - [GitHub](https://github.com/Obianuju23) / [Gmail](mailto:obianujunmoh@gmail.com)

License
Public Domain. No copy write protection

