import customtkinter
import sqlite3
import os

app_version = "0.1"

table_name = "Books"

con = sqlite3.connect("library.db")
cur = con.cursor()

def list_available_books():
    cur.execute(f'''SELECT * FROM {table_name} WHERE status='available' ''')
    book_list_label_1 = customtkinter.CTkLabel(master=tabview.tab("Book List"), text=cur.fetchall())
    book_list_label_1.pack()
    # talvez seja necessário trocar para fetchall

def borrow_book_function():
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
tabview.set("Home")

app.mainloop()

# CRIAR  FUNÇÃO DE EMPRESTAR LIVRO

# CRIAR FUNÇÃO DE DEVOLVER

