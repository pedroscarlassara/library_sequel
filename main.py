import customtkinter
import sqlite3
import os
import datetime

customer_table_name = "customers"
book_table_name = "books"
textbox_width = 200
textbox_height = 10

con = sqlite3.connect("database.db")
cur = con.cursor()

def list_available_books():
    books_list = cur.execute(f"SELECT b.book_name FROM books b JOIN customers c ON c.book_id = b.book_id WHERE c.status=0").fetchall()
    book_list_label_1 = customtkinter.CTkLabel(master=tabview.tab("Book List"), text="")
    book_list_label_1.pack()

    for book in books_list:
        print(book)
        book_list_label_1.configure(text=book[0])

def count_available_books():
    rows = cur.execute(f"SELECT COUNT(*) FROM {customer_table_name} WHERE status=0").fetchall()
    for row in rows:
        return row[0]

def count_borrowed_books():
     rows = cur.execute(f"SELECT COUNT(*) FROM {customer_table_name} WHERE status=1").fetchall()
     for row in rows:
        return row[0]

app = customtkinter.CTk()
app.geometry("400x500")
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

borrow_book_customer_id_label = customtkinter.CTkLabel(master=tabview.tab("Borrow Book"), text="Customer ID")
borrow_book_customer_id_label.pack()

borrow_book_id_label_textbox = customtkinter.CTkTextbox(master=tabview.tab("Borrow Book"), width=textbox_width, height=textbox_height)
borrow_book_id_label_textbox.pack()

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
    cur.execute(f'''INSERT INTO {customer_table_name} VALUES ('{first_name}', '{last_name}', '{book_name}' , 'borrowed', '{datetime.date.today()}')''')
    con.commit()

borrow_book_button = customtkinter.CTkButton(master=tabview.tab("Borrow Book"), command=borrow_available_book, text="Borrow a Book")
borrow_book_button.pack()

tabview.add("Return Book")

return_book_customer_id_label = customtkinter.CTkLabel(master=tabview.tab("Return Book"), text="Customer ID")
return_book_customer_id_label.pack()

return_book_customer_id_textbox = customtkinter.CTkTextbox(master=tabview.tab("Return Book"), width=textbox_width, height=textbox_height)
return_book_customer_id_textbox.pack()

return_book_first_name_label = customtkinter.CTkLabel(master=tabview.tab("Return Book"), text="First Name")
return_book_first_name_label.pack()

return_book_first_name_textbox = customtkinter.CTkTextbox(master=tabview.tab("Return Book"), width=textbox_width, height=textbox_height)
return_book_first_name_textbox.pack()

return_book_last_name_label = customtkinter.CTkLabel(master=tabview.tab("Return Book"), text="Last Name")
return_book_last_name_label.pack()

return_book_last_name_textbox = customtkinter.CTkTextbox(master=tabview.tab("Return Book"), width=textbox_width, height=textbox_height)
return_book_last_name_textbox.pack()

return_book_book_name_label = customtkinter.CTkLabel(master=tabview.tab("Return Book"), text="Book Name")
return_book_book_name_label.pack()

return_book_book_name_textbox = customtkinter.CTkTextbox(master=tabview.tab("Return Book"), width=textbox_width, height=textbox_height)
return_book_book_name_textbox.pack()

def return_borrowed_book():
    first_name = return_book_first_name_textbox.get("0.0", "end").strip()
    last_name = return_book_last_name_textbox.get("0.0", "end").strip()
    book_name = return_book_book_name_textbox.get("0.0", "end").strip()
    customer_id = return_book_customer_id_textbox.get("0.0", "end").strip()
    query = cur.execute(f'''SELECT book_id FROM books WHERE book_name='{book_name}' ''').fetchone()
    cur.execute(f'''DELETE FROM {customer_table_name} WHERE book_id='{query[0]}' AND status=1''')
    con.commit()

    # for column in query:
    #     print(column)
    #     cur.execute(f'''DELETE FROM customers WHERE book_id='{column}' AND status=1''')
    #     con.commit()

return_book_button = customtkinter.CTkButton(master=tabview.tab("Return Book"), text="Return a Book", command=return_borrowed_book)
return_book_button.pack()


tabview.set("Home")

app.mainloop()
