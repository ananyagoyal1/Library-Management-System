Library Management System

This Python script provides a basic library management system with functionalities for adding, removing, displaying information about books and members, and managing book issuance and return. It utilizes the mysql.connector library to interact with a MySQL database.

Features:

Add, remove, and display books in the library
Add, remove, and display members
Issue books to members (marks book as unavailable)
Return books (marks book as available and updates return date)
Display all transactions (including book, member, issue date, and return date)
Requirements:

Python 3 (tested with 3.x)
mysql.connector library (pip install mysql.connector)
MySQL database server with a library database and tables (books, members, transactions)
Setup:

Install dependencies: Run pip install mysql.connector in your terminal.
Database configuration:
Update connection details in the code (change 'Ananya-Goyal', 'root@localhost', and '' for your database server, username, and password).
Ensure you have the library database and tables (books, members, transactions) created with appropriate columns.
Usage:

Run the script: Execute python library_management.py (replace with your script filename).
Menu: The script will present a menu with options for managing books, members, and transactions.
Follow prompts: Enter the relevant information when prompted for adding or removing books/members, and book/member IDs when issuing or returning books.
Database Schema (Example):

SQL
CREATE TABLE books (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  available BOOLEAN DEFAULT TRUE
);

CREATE TABLE members (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE transactions (
  id INT PRIMARY KEY AUTO_INCREMENT,
  book_id INT NOT NULL,
  member_id INT NOT NULL,
  issue_date DATE NOT NULL,
  return_date DATE DEFAULT NULL,
  FOREIGN KEY (book_id) REFERENCES books(id),
  FOREIGN KEY (member_id) REFERENCES members(id)
);

Disclaimer:

This script is intended for educational or demonstration purposes. It may require modifications for production use to enhance security, error handling, and user interface.  Future development can include features like user authentication, search functionality, email notifications, and reporting.
