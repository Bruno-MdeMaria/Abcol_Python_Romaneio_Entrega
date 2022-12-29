from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("ROMANEIO DE ENTREGA")
window.config(padx=40, pady=40)
window.geometry("1500x700")

canvas = Canvas(height=100, width=600)
logo_abcol = PhotoImage(file="image\logo_abcol.png")
canvas.create_image(600,100, image=logo_abcol)
canvas.grid(row=0, column=1)

#ETIQUETAS
titulo_label = Label(text="CONTROLE DE VEÍCULO:")
titulo_label.grid(row=0, column=0)
placa_label = Label(text="Placa:")
placa_label.grid(row=1, column=0)
motorista_label = Label(text="Motorista:")
motorista_label.grid(row=1, column=1)
kmsaida_label = Label(text="Km Saída:")
kmsaida_label.grid(row=1, column=2)




window.mainloop()