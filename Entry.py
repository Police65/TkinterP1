from  tkinter import * # Importar la librería tkinter
from tkinter import messagebox
"""
ventana=Tk()
ventana.geometry("600x200")
cedula = StringVar()
EntryCedula = Entry (ventana, textvariable = cedula)
EntryCedula.place(x=20,y=20)
cedula.set(4120022)
messagebox.showinfo("Valor cedula", cedula.get())
"""

def validate_entry(text):
    return text.isdecimal()

root = Tk()
root.config(width=300, height=200)
root.title("Mi aplicación")
entry = Entry(root,validate="key",validatecommand=(root.register(validate_entry), "%S"))
entry.place(x=50, y=50, width=150)

root.mainloop()