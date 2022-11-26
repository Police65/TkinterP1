from  tkinter import *
ventana = Tk()
ventana.title("Ventana principal")
ventana.iconbitmap("python.ico")
ventana.geometry("400x200")
ventana.config(bg = "pink")

labelCedula = Label(ventana)
labelCedula.config (text = "Cédula")
labelCedula.config(bg = "pink")
labelCedula.grid(row=0, column= 0,sticky = "e",padx =20,pady=20)

cuadroCedula = Entry(ventana)
cuadroCedula.grid(row=0, column=1 )

cuadroCedula.config(justify="center")

labelApellido = Label(ventana)
labelApellido.config (text = "Apellido")
labelApellido.config(bg = "pink")
labelApellido.grid(row=1, column= 0,sticky = "w", padx = 20,pady=20 )

cuadroApellido = Entry(ventana)
cuadroApellido.grid(row=1, column=1 )

labelCorreo = Label(ventana)
labelCorreo.config (text = "Correo electrónico")
labelCorreo.config(bg = "pink")
labelCorreo.grid(row=2, column= 0, sticky = "w",padx=20 ,pady=20 )

cuadroCorreo = Entry(ventana)
cuadroCorreo.grid(row=2, column=1, padx=10 )
cuadroCorreo.config(justify="right")

def calcular():
    print("Hola")

botonCalcular = Button(ventana, text = "Calcular", command = calcular)
botonCalcular.grid(row=0, column= 2)
ventana.mainloop()