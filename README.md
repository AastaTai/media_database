# Sharing for All
This repository contains a Python application built using wxPython for the GUI and MySQLdb for database interactions. The application allows users to insert, find, modify, and recommend various items such as books, albums, movies, and series.

## Features
- Insert Items: Users can insert new items into the database.
- Find and Modify Items: Users can search for items and modify their details.
- Recommendations: The application provides recommendations based on user ratings.
- User Management: Users can log in or create new accounts.

## Prerequisites
- Python 3.x
- wxPython
- MySQLdb
- MySQL Server

## Usage
1. Run the application:
    ```python code.py```
2. Login or Create User:
    - On the login screen, choose to either log in or create a new user.
    - Enter the required details and click "Enter".
3. Insert Items:
    - Navigate to the "Insert" tab.
    - Fill in the details and click "Insert".
4. Find and Modify Items:
    - Navigate to the "Find + Modify" tab.
    - Select a category and click "Search".
    - Modify the details as needed and click "Modify".
5. Recommendations:
    - Navigate to the "Recommendation" tab.
    - Click "Update" to get recommendations.
6. Code Structure
    - code.py: Main application file containing all the logic and GUI components.

## Acknowledgements
- [wxPython](https://www.wxpython.org/) for the GUI framework.
- [MySQLdb](https://mysqlclient.readthedocs.io/) for database interactions.