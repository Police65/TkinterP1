from  tkinter import * # Importar la librería tkinter

ventana = Tk()         # Crear una variable de la clase Tk

ventana.title("Ventana principal") # Establece el título de la ventana
ventana.resizable(False,False) # Evita que se cambie el tamaño de la ventana
ventana.iconbitmap("python.ico") # Establece el ícono de la ventana
ventana.geometry("600x300") # Establece ancho por alto de la ventana
ventana.config(bg = "pink")  # Establece el color de fondo de la ventana

ventana.mainloop()     #Llamar al método mainlooop() que visualiza la ventana

