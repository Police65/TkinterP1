from  tkinter import * # Importar la librería tkinter
from tkinter import messagebox # Importar la librería messagebox
from tkinter import ttk

ventana = Tk()         # Crear una variable de la clase Tk
ventana.title("Tree view") # Establece el título de la ventana

ventana.geometry("700x400") # Establece ancho por alto de la ventana
tabla = ttk.Treeview(ventana, columns =("Cantidad","Precio"))
tabla.heading("#0", text="Producto")
tabla.heading("Cantidad", text="Cantidad")
tabla.heading("Precio", text="Precio")
tabla.place(x=20,y=20)
tabla.insert("",END,text="Cambur",values=(5,10))
tabla.insert("",END,text="Papas",values=(3,15))


ventana.mainloop()
