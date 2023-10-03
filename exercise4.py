import sqlite3

# Create or connect to the database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        BookID TEXT PRIMARY KEY,
        Title TEXT,
        Author TEXT,
        ISBN TEXT,
        Status TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        UserID TEXT PRIMARY KEY,
        Name TEXT,
        Email TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Reservations (
        ReservationID TEXT PRIMARY KEY,
        BookID TEXT,
        UserID TEXT,
        ReservationDate DATE,
        FOREIGN KEY (BookID) REFERENCES Books (BookID),
        FOREIGN KEY (UserID) REFERENCES Users (UserID)
    )
''')

def add_book():
    book_id = input("Enter BookID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    isbn = input("Enter ISBN: ")
    status = input("Enter Status: ")

    cursor.execute('INSERT INTO Books VALUES (?, ?, ?, ?, ?)',
                   (book_id, title, author, isbn, status))
    conn.commit()
    print("Book added successfully.")

def find_book_details():
    book_id = input("Enter BookID: ")
    cursor.execute('''
        SELECT Books.BookID, Books.Title, Books.Status, Users.Name, Users.Email
        FROM Books
        LEFT JOIN Reservations ON Books.BookID = Reservations.BookID
        LEFT JOIN Users ON Reservations.UserID = Users.UserID
        WHERE Books.BookID = ?
    ''', (book_id,))
    result = cursor.fetchone()

    if result:
        book_id, title, status, user_name, user_email = result
        print(f"BookID: {book_id}")
        print(f"Title: {title}")
        print(f"Status: {status}")
        print(f"Reserved by: {user_name} ({user_email})")
    else:
        print("Book not found or not reserved.")

def find_book_reservation_status():
    search_text = input("Enter BookID, UserID, ReservationID, or Title: ")
    if search_text.startswith('LB'):
        # BookID
        cursor.execute('SELECT * FROM Books WHERE BookID = ?', (search_text,))
    elif search_text.startswith('LU'):
        # UserID
        cursor.execute('''
            SELECT Books.BookID, Books.Title, Books.Status
            FROM Books
            LEFT JOIN Reservations ON Books.BookID = Reservations.BookID
            WHERE Reservations.UserID = ?
        ''', (search_text,))
    elif search_text.startswith('LR'):
        # ReservationID
        cursor.execute('''
            SELECT Books.BookID, Books.Title, Books.Status
            FROM Books
            LEFT JOIN Reservations ON Books.BookID = Reservations.BookID
            WHERE Reservations.ReservationID = ?
        ''', (search_text,))
    else:
        # Title
        cursor.execute('SELECT * FROM Books WHERE Title = ?', (search_text,))

    results = cursor.fetchall()
    if results:
        for result in results:
            print(result)
    else:
        print("No matching records found.")

def find_all_books():
    cursor.execute('''
        SELECT Books.BookID, Books.Title, Books.Author, Books.ISBN, Books.Status,
               Users.UserID, Users.Name, Users.Email,
               Reservations.ReservationID, Reservations.ReservationDate
        FROM Books
        LEFT JOIN Reservations ON Books.BookID = Reservations.BookID
        LEFT JOIN Users ON Reservations.UserID = Users.UserID
    ''')
    results = cursor.fetchall()
    for result in results:
        print(result)

def update_book_details():
    book_id = input("Enter BookID to update: ")
    new_status = input("Enter new status: ")

    cursor.execute('''
        UPDATE Books
        SET Status = ?
        WHERE BookID = ?
    ''', (new_status, book_id))

    # Commit the changes to the database
    conn.commit()

    if cursor.rowcount > 0:
        print("Book details updated successfully.")
    else:
        print("Book not found. Update failed.")

def delete_book():
    book_id = input("Enter BookID to delete: ")

    cursor.execute('DELETE FROM Books WHERE BookID = ?', (book_id,))
    cursor.execute('DELETE FROM Reservations WHERE BookID = ?', (book_id,))
    conn.commit()
    print("Book deleted successfully.")

while True:
    print("\nLibrary Management System")
    print("1. Add a new book")
    print("2. Find a book's detail by BookID")
    print("3. Find book's reservation status")
    print("4. Find all books")
    print("5. Update book details")
    print("6. Delete a book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        find_book_details()
    elif choice == '3':
        find_book_reservation_status()
    elif choice == '4':
        find_all_books()
    elif choice == '5':
        update_book_details()
    elif choice == '6':
        delete_book()
    elif choice == '7':
        break

# Close the database connection
conn.close()
