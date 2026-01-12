import customtkinter

app_version = "0.1"

app = customtkinter.CTk()
app.geometry("400x400")
app.title(f"library sequel {app_version}")

label_query_output = customtkinter.CTkLabel(app, text="Query Output Label", fg_color="transparent")
label_query_output.pack()

app.mainloop()