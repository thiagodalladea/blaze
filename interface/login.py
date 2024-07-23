import customtkinter as ctk
import tkinter as tk
import globals

def interface_login(app):
    login_window = ctk.CTkToplevel(app)
    login_window.title("Login")
    login_window.geometry("400x300")

    user_var = tk.StringVar()
    pass_var = tk.StringVar()

    user_label = ctk.CTkLabel(login_window, text="Usuário/CPF:")
    user_label.pack(pady=5)
    user_entry = ctk.CTkEntry(login_window, textvariable=user_var, width=200)
    user_entry.pack(pady=5)

    pass_label = ctk.CTkLabel(login_window, text="Senha:")
    pass_label.pack(pady=5)
    pass_entry = ctk.CTkEntry(login_window, textvariable=pass_var, show="*", width=200)
    pass_entry.pack(pady=5)

    def submit():
        global username, password
        login_window.destroy()

    submit_button = ctk.CTkButton(login_window, text="Submit", fg_color="#FF284C", width=200, height=100, command=submit)
    submit_button.pack(pady=50)

    login_window.transient(app)
    login_window.grab_set()
    app.wait_window(login_window)