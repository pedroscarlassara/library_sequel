import customtkinter
import sqlite3

app_version = "0.1"

table_name = "Books"

con = sqlite3.connect("library.db")
cur = con.cursor()

""" cur.execute(f'''CREATE TABLE {table_name} (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    book TEXT NOT NULL,
    status TEXT NOT NULL
    );''')
 """
cur.execute(f'''INSERT INTO {table_name} VALUES (1, 'pedro', 'scarlassara', 'livro_1', 'emprestado')''')
con.commit()

app = customtkinter.CTk()
app.geometry("400x400")
app.title(f"library sequel {app_version}")

label_query_output = customtkinter.CTkLabel(app, text="Query Output Label", fg_color="transparent")
label_query_output.pack()

app.mainloop()