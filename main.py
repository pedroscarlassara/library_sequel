import customtkinter
import sqlite3
import os

app_version = "0.1"

table_name = "Books"


textbox_width = 200
textbox_height = 10

con = sqlite3.connect("library.db")
cur = con.cursor()

def list_available_books():
    cur.execute(f'''SELECT * FROM {table_name} WHERE status='available' ''')
    book_list_label_1 = customtkinter.CTkLabel(master=tabview.tab("Book List"), text=cur.fetchall())
    book_list_label_1.pack()

def borrow_available_book():
    print("button pressed")


# """ cur.execute(f'''CREATE TABLE {table_name} (
#     customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first_name TEXT NOT NULL,
#     last_name TEXT,
#     book TEXT NOT NULL,
#     status TEXT NOT NULL
#     );''')
#  """
# cur.execute(f'''INSERT INTO {table_name} VALUES (3, 'pedro', 'pereira', 'livro_3', 'available')''')
# con.commit()

app = customtkinter.CTk()
app.geometry("400x300")
app.title(f"Library Sequel")

tabview = customtkinter.CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("Home")

home_label_1 = customtkinter.CTkLabel(master=tabview.tab("Home"), text=f"Welcome, {os.getlogin()}.")
home_label_1.pack()


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

borrow_book_button = customtkinter.CTkButton(master=tabview.tab("Borrow Book"), command=borrow_available_book, text="Borrow a Book")
borrow_book_button.pack()

tabview.set("Home")

app.mainloop()

# CRIAR  FUNÇÃO DE EMPRESTAR LIVRO

# CRIAR FUNÇÃO DE DEVOLVER

