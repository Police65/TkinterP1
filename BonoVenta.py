from  tkinter import * # Importar la librería tkinter
from tkinter import messagebox # Importar la librería messagebox
from tkinter import ttk

ventana = Tk()         # Crear una variable de la clase Tk
ventana.title("Ventana principal") # Establece el título de la ventana
#ventana.resizable(False,False) # Evita que el ususrio el tamaño de la ventana
ventana.iconbitmap("python.ico") # Establece el ícono de la ventana
ventana.geometry("850x400") # Establece ancho por alto de la ventana
ventana.config(bg = "pink")  # Establece el color de fondo de la ventana

cedula = StringVar()
dpto = StringVar()
venta = DoubleVar()
comision = DoubleVar()
totalVenta = DoubleVar()
totalComision = DoubleVar()

def procesar():
    global totalVenta
    global totalComision
    if dpto.get() == "Ropa":
        comision.set( venta.get() * 0.4/100)
    elif dpto.get() == "Juguete":
        comision.set( venta.get() * 0.3/100)
    elif dpto.get() == "Lencería":
        comision.set( venta.get() * 0.5/100)
    comision.set(round(comision.get(),2))
    totalVenta.set ( totalVenta.get() + venta.get())
    totalVenta.get()
    totalComision.set(totalComision.get() + round(comision.get(),2))
    round(totalComision.get(),2)
    tabla.insert("", END, text=cedula.get(), values=(dpto.get(),venta.get(),round(comision.get(),2)))
    botonLimpiar.config(state="normal")

def limpiar():
    cedula.set("")
    dpto.set("")
    venta.set(0.00)
    comision.set(0.00)
    botonLimpiar.config(state="disable")

labelCedula = Label(ventana)
labelCedula.config (text = "Cédula",bg = "pink")
labelCedula.place(x = 20, y = 20)

labelDepartamento = Label(ventana)
labelDepartamento.config (text = "Departamento",bg = "pink")
labelDepartamento.place(x = 100, y = 20)

labelVenta = Label(ventana)
labelVenta.config (text = "Venta",bg = "pink")
labelVenta.place(x = 230, y = 20)

labelComision = Label(ventana)
labelComision.config (text = "Comisión",bg = "pink")
labelComision.place(x = 320, y = 20)

labelTotalVenta = Label(ventana)
labelTotalVenta.config (text = "Total venta",bg = "pink")
labelTotalVenta.place(x = 340, y = 350)

labelTotalCopmision = Label(ventana)
labelTotalCopmision.config (text = "Total Comisión",bg = "pink")
labelTotalCopmision.place(x = 550, y = 350)

cajaCedula = Entry(ventana,width =10, textvariable = cedula)
cajaCedula.place(x = 20, y = 50)

comboDepartamento = ttk.Combobox(ventana,width =15,textvariable = dpto)
comboDepartamento.place(x = 100, y = 50)
comboDepartamento["values"]= ("Ropa","Juguete","Lencería")
cajaVenta = Entry(ventana,width =10, textvariable = venta)
cajaVenta.place(x = 230, y = 50)

cajaComisión = Entry(ventana,width =10,textvariable = comision)
cajaComisión.place(x = 320, y = 50)

cajaTotalVenta = Entry(ventana,width =10,textvariable = totalVenta)
cajaTotalVenta.place(x = 420, y = 350)

cajaTotalComisión = Entry(ventana,width =10,textvariable = totalComision)
cajaTotalComisión.place(x = 650, y = 350)


botonProcesar = Button(ventana, text="Procesar", command = procesar)
botonProcesar.place(x=420,y= 50)

botonLimpiar = Button(ventana, text="Limpiar", command = limpiar, state ="disable")

botonLimpiar.place(x=520,y= 50)

tabla = ttk.Treeview(ventana, columns =("Departamento","Venta","Comisión"))
tabla.heading("#0", text="Cédula")
tabla.heading("Departamento", text="Departamento")
tabla.heading("Venta", text="Venta")
tabla.heading("Comisión", text="Comisión")
tabla.place(x=20,y=80)
ventana.mainloop()