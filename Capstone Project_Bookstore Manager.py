import sqlite3


# Connect to SQLite database
conn = sqlite3.connect("ebookstore.db")
cursor = conn.cursor()


# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    qty INTEGER
)
""")


# Insert initial books
cursor.executemany("""
INSERT OR IGNORE INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)
""", [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12)
])
conn.commit()


# Function to add a new book
def enter_book():
    id_ = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter quantity: "))
    cursor.execute(
        "INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)",
        (id_, title, author, qty)
    )
    conn.commit()
    print("Book added successfully.")


# Function to update book information
def update_book():
    id_ = int(input("Enter book ID to update: "))
    column = input("Enter column to update (title, author, qty): ")
    new_value = input("Enter new value: ")
    if column == "qty":
        new_value = int(new_value)
    cursor.execute(
        f"UPDATE book SET {column} = ? WHERE id = ?",
        (new_value, id_)
    )
    conn.commit()
    print("Book updated successfully.")


# Function to delete a book
def delete_book():
    id_ = int(input("Enter book ID to delete: "))
    cursor.execute("DELETE FROM book WHERE id = ?", (id_,))
    conn.commit()
    print("Book deleted successfully.")


# Function to search for a book
def search_books():
    keyword = input("Enter book title or author to search: ")
    cursor.execute(
        "SELECT * FROM book WHERE title LIKE ? OR author LIKE ?",
        (f"%{keyword}%", f"%{keyword}%")
    )
    results = cursor.fetchall()
    if results:
        for book in results:
            print(book)
    else:
        print("No books found.")


# Menu-driven program
while True:
    print("\nBookstore Manager Menu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        enter_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        search_books()
    elif choice == "0":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")

conn.close()