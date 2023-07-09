import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    host='Ananya-Goyal',
    user='root@localhost',
    password='1706',
    database='library'
)

cursor = cnx.cursor()

# Function to add a book to the library
def add_book(title, author):
    query = "INSERT INTO books (title, author) VALUES (%s, %s)"
    values = (title, author)
    cursor.execute(query, values)
    cnx.commit()
    print("Book added successfully!")

# Function to remove a book from the library
def remove_book(book_id):
    query = "DELETE FROM books WHERE id = %s"
    value = (book_id,)
    cursor.execute(query, value)
    cnx.commit()
    print("Book removed successfully!")

# Function to display all books in the library
def display_books():
    query = "SELECT * FROM books"
    cursor.execute(query)
    books = cursor.fetchall()
    print("Books in the library:")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Available: {book[3]}")

# Function to add a member
def add_member(name, email):
    query = "INSERT INTO members (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(query, values)
    cnx.commit()
    print("Member added successfully!")

# Function to remove a member
def remove_member(member_id):
    query = "DELETE FROM members WHERE id = %s"
    value = (member_id,)
    cursor.execute(query, value)
    cnx.commit()
    print("Member removed successfully!")

# Function to display all members
def display_members():
    query = "SELECT * FROM members"
    cursor.execute(query)
    members = cursor.fetchall()
    print("Members:")
    for member in members:
        print(f"ID: {member[0]}, Name: {member[1]}, Email: {member[2]}")

# Function to issue a book to a member
def issue_book(book_id, member_id):
    query = "UPDATE books SET available = FALSE WHERE id = %s"
    value = (book_id,)
    cursor.execute(query, value)
    query = "INSERT INTO transactions (book_id, member_id, issue_date) VALUES (%s, %s, CURDATE())"
    values = (book_id, member_id)
    cursor.execute(query, values)
    cnx.commit()
    print("Book issued successfully!")

# Function to return a book
def return_book(book_id):
    query = "UPDATE books SET available = TRUE WHERE id = %s"
    value = (book_id,)
    cursor.execute(query, value)
    query = "UPDATE transactions SET return_date = CURDATE() WHERE book_id = %s AND return_date IS NULL"
    value = (book_id,)
    cursor.execute(query, value)
    cnx.commit()
    print("Book returned successfully!")

# Function to display all transactions
def display_transactions():
    query = "SELECT t.id, b.title, m.name, t.issue_date, t.return_date FROM transactions t JOIN books b ON t.book_id = b.id JOIN members m ON t.member_id = m.id"
    cursor.execute(query)
    transactions = cursor.fetchall()
    print("Transactions:")
    for transaction in transactions:
        print(f"Transaction ID: {transaction[0]}, Book: {transaction[1]}, Member: {transaction[2]}, Issue Date: {transaction[3]}, Return Date: {transaction[4] if transaction[4] else 'Not returned'}")

# Close the database connection
def close_connection():
    cursor.close()
    cnx.close()
    print("Connection closed.")

# Main program loop
while True:
    print()
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Add Member")
    print("5. Remove Member")
    print("6. Display Members")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Display Transactions")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        add_book(title, author)
    elif choice == "2":
        book_id = input("Enter the book ID: ")
        remove_book(book_id)
    elif choice == "3":
        display_books()
    elif choice == "4":
        name = input("Enter the member name: ")
        email = input("Enter the member email: ")
        add_member(name, email)
    elif choice == "5":
        member_id = input("Enter the member ID: ")
        remove_member(member_id)
    elif choice == "6":
        display_members()
    elif choice == "7":
        book_id = input("Enter the book ID: ")
        member_id = input("Enter the member ID: ")
        issue_book(book_id, member_id)
    elif choice == "8":
        book_id = input("Enter the book ID: ")
        return_book(book_id)
    elif choice == "9":
        display_transactions()
    elif choice == "0":
        close_connection()
        break
    else:
        print("Invalid choice. Please try again.")
