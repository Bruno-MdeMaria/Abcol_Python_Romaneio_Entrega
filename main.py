from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("ROMANEIO DE ENTREGA")
window.config(padx=40, pady=40)
window.geometry("1500x700")

canvas = Canvas(height=1500, width=700)
logo_abcol = PhotoImage(file="image\logo_abcol.png")
canvas.create_image(600,100, image=logo_abcol)
canvas.grid(row=0, column=1)



window.mainloop()