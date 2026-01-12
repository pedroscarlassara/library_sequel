import customtkinter
import sqlite3
import os

table_name = "Books"

textbox_width = 200
textbox_height = 10

con = sqlite3.connect("library.db")
cur = con.cursor()

def list_available_books():
    books_list = cur.execute(f"SELECT * FROM {table_name} WHERE status='available'").fetchall()
    for book in books_list:
        print(book)
        book_list_label_1 = customtkinter.CTkLabel(master=tabview.tab("Book List"), text=book)
        book_list_label_1.pack()

def count_available_books():
    rows = cur.execute(f"SELECT COUNT(*) FROM {table_name} WHERE status='available'").fetchall()
    for row in rows:
        return row[0]

def count_borrowed_books():
     rows = cur.execute(f"SELECT COUNT(*) FROM {table_name} WHERE status='borrowed'").fetchall()
     for row in rows:
        return row[0]


# cur.execute(f'''CREATE TABLE {table_name} (
#     first_name TEXT NOT NULL,
#     last_name TEXT,
#     book TEXT NOT NULL,
#     status TEXT NOT NULL
#     );''')

app = customtkinter.CTk()
app.geometry("400x300")
app.title(f"Library Sequel")

tabview = customtkinter.CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("Home")

home_label_1 = customtkinter.CTkLabel(master=tabview.tab("Home"), text=f"Welcome, {os.getlogin()}.")
home_label_1.pack()

home_available_books = customtkinter.CTkLabel(master=tabview.tab("Home"), text=f"Available Books: {count_available_books()}")
home_available_books.pack()

home_borrowed_books = customtkinter.CTkLabel(master=tabview.tab("Home"), text=f"Borrowed Books: {count_borrowed_books()}")
home_borrowed_books.pack()

tabview.add("Book List")

book_list_button_1 = customtkinter.CTkButton(master=tabview.tab("Book List"), command=list_available_books, text="List Available Books")
book_list_button_1.pack()

tabview.add("Borrow Book")

borrow_book_first_name_label = customtkinter.CTkLabel(master=tabview.tab("Borrow Book"), text="First Name")
borrow_book_first_name_label.pack()

borrow_book_first_name_textbox = customtkinter.CTkTextbox(master=tabview.tab("Borrow Book"), width=textbox_width, height=textbox_height)
borrow_book_first_name_textbox.pack()

borrow_book_last_name_label = customtkinter.CTkLabel(master=tabview.tab("Borrow Book"), text="Last Name")
borrow_book_last_name_label.pack()

borrow_book_last_name_textbox = customtkinter.CTkTextbox(master=tabview.tab("Borrow Book"), width=textbox_width, height=textbox_height)
borrow_book_last_name_textbox.pack()

borrow_book_book_name_label = customtkinter.CTkLabel(master=tabview.tab("Borrow Book"), text="Book Name")
borrow_book_book_name_label.pack()

borrow_book_book_name_textbox = customtkinter.CTkTextbox(master=tabview.tab("Borrow Book"), width=textbox_width, height=textbox_height)
borrow_book_book_name_textbox.pack()

def borrow_available_book():
    first_name = borrow_book_first_name_textbox.get("0.0", "end")
    last_name = borrow_book_last_name_textbox.get("0.0", "end")
    book_name = borrow_book_book_name_textbox.get("0.0", "end")
    cur.execute(f'''INSERT INTO {table_name} VALUES ('{first_name}', '{last_name}', '{book_name}' , 'borrowed')''')
    con.commit()

borrow_book_button = customtkinter.CTkButton(master=tabview.tab("Borrow Book"), command=borrow_available_book, text="Borrow a Book")
borrow_book_button.pack()

tabview.set("Home")

app.mainloop()

# CRIAR FUNÇÃO DE DEVOLVER

# PRO LIST BOOK FAZER UM FETCH ONE DENTRO DE UM FOR PRA FICAR EM LOOP E PULANDO LINHA
