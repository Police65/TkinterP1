from tkinter import messagebox

nombre="Nieves"
messagebox.showinfo("Información","Mi nombre es "+ nombre)
messagebox.showwarning("Error", "Dato no válido")
messagebox.askquestion("Salir", "¿Desea salir?")
messagebox.askokcancel("Proceso","¿Acepta el reto?")
messagebox.askretrycancel("Juego","¿Reintentas la jugada?")