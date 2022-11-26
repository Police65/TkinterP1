from  tkinter import * # Importar la librería tkinter
from tkinter import messagebox # Importar la librería messagebox
from tkinter import ttk

ventana = Tk()         # Crear una variable de la clase Tk
ventana.title("Tree view") # Establece el título de la ventana

ventana.geometry("700x400") # Establece ancho por alto de la ventana
arbol = ttk.Treeview(ventana)
arbol.place(x=20,y=20)
menu1=arbol.insert("",END, text ="Menú 1")
menu2=arbol.insert("",END, text ="Menú 2")
arbol.insert(menu1,END, text ="Opción 1")
arbol.insert(menu1,END, text ="Opción 2")
arbol.insert(menu1,END, text ="Opción 3")

arbol.insert(menu2,END, text ="Opción 1")
arbol.insert(menu2,END, text ="Opción 2")
arbol.insert(menu2,END, text ="Opción 3")
ventana.mainloop()
