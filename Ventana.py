from  tkinter import * # Importar la librería tkinter
from tkinter import messagebox # Importar la librería messagebox
from tkinter import ttk
"""Crear la ventana inicial"""
ventana = Tk()         # Crear una variable de la clase Tk
ventana.title("Ventana principal") # Establece el título de la ventana
#ventana.resizable(False,False) # Evita que el ususrio el tamaño de la ventana
ventana.iconbitmap("python.ico") # Establece el ícono de la ventana
ventana.geometry("700x400") # Establece ancho por alto de la ventana
ventana.config(bg = "pink")  # Establece el color de fondo de la ventana

"""Crear un Frame"""
frame=Frame()  # Crear una variable de la clase Frame
frame.pack(fill = "both", expand = "True")   #Posiciona el frame con relación a la ventana
frame.config(bg = "purple") #Establece el color de fondo del frame
frame.config(width = "650", height = "350") #Establecer ancho y alto del frame
frame.config(relief = "groove") #Establece el tipo de borde
frame.config(bd = 10) #Establecer el espesor del borde
frame.config(cursor = "hand2") #Establece la forma del cursor del mouse

"""Mostrar una imagen"""
"""Crear una variable de la clase PhotoImage indicando el archivo.png"""
imagen = PhotoImage(file = "Flores.png")
"""Crear una etiqueta indicando el contenedor y a la propiedad image se le asigna la variable de la clase PhotoImage """
labelImagen = Label (frame, image = imagen )
labelImagen.pack(fill = "both", expand = "True") #La etiqueta ocupa el frame

"""Uso de label para mostrar texto (Identificar otros objetos)"""
"""Crea una variable de la clase Label indicando el contenedor"""
labelCedula = Label(frame) #Crea una variable de la clase Label indicando el Frame contenedor
labelCedula.config (text = "Cédula") #Texto de la etiqueta
"""Ubicación desde el borde izquierdo (x) y desde el borde superior (y)"""
labelCedula.place(x = 20, y = 20)
labelCedula.config(bg = "pink")  #Color del fondo
labelCedula.config(fg = "blue") #Color del texto
labelCedula.config(font=("Comic Sans MS",12)) # Estilo y tamaño de la fuente

"""Uso de Entry"""
"""Crear una variable para mostrar/leer texto del Entry"""
cedula = StringVar()
"""Crea una variable de la clase Entry indicando el contenedor y la variable asociada"""
cuadroCedula = Entry(frame, textvariable = cedula)
"""Ubicación desde el borde izquierdo (x) y desde el borde superior (y)"""
cuadroCedula.place(x = 100, y = 20)
cuadroCedula.config(bg = "yellow")  #Color del fondo
cuadroCedula.config(fg = "blue") #Color del texto
cuadroCedula.config(font=("Comic Sans MS",12)) # Estilo y tamaño de la fuente
#cuadroCedula.config(show = "*") #Ocultar el texto escrito
"""Mostrar un dato en el Entry"""
cedula.set(4120022)
"""Tomar el dato del Entry"""
#messagebox.showinfo("Valor cedula", cedula.get())

"""Uso de radiobutton"""
"""Crear una etiqueta para identificar las opciones"""
labelSexo = Label(frame, text = "Sexo")
labelSexo.place(x=20,y=70)
"""Crear una variable para guardar la opción seleccionada"""
sexo = IntVar()
"""Crear la función asociada a las opciones"""
def funcionSexo():
    if sexo.get()==1:
        messagebox.showinfo("Sexo", "Mujer")
    else:
        messagebox.showinfo("Sexo", "Hombre")
"""Crear los botones"""
radiomujer=Radiobutton(frame, text = "Mujer", variable = sexo, value = 1, command=funcionSexo)
radiomujer.place(x=20,y=100)
radiohombre= Radiobutton(frame, text = "Hombre", variable = sexo, value = 2, command=funcionSexo)
radiohombre.place(x=20,y=130)

"""Uso de Buttom"""
"""Definir la función asociada al evento click"""
def salir():
    respuesta = messagebox.askquestion("Salir", "¿Desea salir?")
    if respuesta == "yes":
        ventana.destroy()
"""Crear el botón indicando contenedor, texto y función asociada"""
botonSalir = Button(frame, text = "Salir", command = salir)
botonSalir.place(x=150, y = 250)
botonSalir.config(bg = "yellow")  #Color del fondo
botonSalir.config(fg = "blue") #Color del texto
botonSalir.config(font=("Comic Sans MS",12)) #Estilo y tamaño de la fuente

"""Uso de combobox"""
"""Crear la función para procesar el dato seleccionado en el combo"""
def procesar():
    EdoCiv = comboEdoCiv.get()
    messagebox.showinfo("Edo. Civil",EdoCiv)
"""Crear una etiqueta para identificar el valor a seleccionar en el combo"""
labelEdoCiv =Label(frame, text = "Edo. civil")
labelEdoCiv.place(x = 130, y = 70)
"""Crear un combo sólo lectura"""
comboEdoCiv =ttk.Combobox(frame, state = "readonly")
comboEdoCiv.place(x = 130, y = 100)
"""Llenar el combo"""
comboEdoCiv["values"] = ("Soltero(a)","Casado(a)","Divorciado(a)","Viudo(a)")
comboEdoCiv.current(0)
"""Crear un botón para procesar el dato seleccionado en el combo """
botonProcesar = Button(frame, text = "Procesar", command = procesar)
botonProcesar.place(x=300, y = 250)
botonProcesar.config(bg = "yellow",fg = "blue",font=("Comic Sans MS",12))

ventana.mainloop()     #Llamar al método mainlooop() que visualiza la ventana

