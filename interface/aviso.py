import customtkinter as ctk 
from PIL import Image, ImageTk

def show_aviso(app):
    aviso_window = ctk.CTkToplevel()
    aviso_window.title('Aviso')
    aviso_window.geometry('500x700')

    image_path = 'assets/logo.png'
    img = Image.open(image_path)
    img_tk = ImageTk.PhotoImage(img)

    img_label = ctk.CTkLabel(aviso_window, image=img_tk, text='')
    img_label.image = img_tk
    img_label.pack(pady=50)

    text = 'Este é um aviso para explicar como o programa funciona. Siga as instruções para uma melhor experiência.'
    text_label = ctk.CTkLabel(aviso_window, text=text, wraplength=350, justify='left')
    text_label.pack(pady=20)

    def close_aviso():
        aviso_window.destroy()

    button = ctk.CTkButton(aviso_window, text='Entendi', fg_color='#FF284C', width=300, height=50, command=close_aviso)
    button.pack(pady=50, side='bottom')

    aviso_window.transient(app)
    aviso_window.grab_set()
    app.wait_window(aviso_window)
