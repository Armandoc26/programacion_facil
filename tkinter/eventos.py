# # explicacion de los eventos de mouse y keyboard con tkinter 

# from tkinter import *

# # ventana principal
# root = Tk()

# # titulo de la ventana
# root.title("Curso de tkinter en programacion facil")

# # Insertar datos, con el widget Entry para ingresar datos en la GUI 
# entrada = Entry(root)
# entrada.insert(0, "Escriba su nombre...")
# entrada.bind("<Button-1>", lambda e : entrada.delete(0, END))
# entrada.pack()

# # evento para manejar el button
# def pulsar_boton():
#     nombre = entrada.get()
#     Label(root, text=f"{nombre}").pack()

# # boton, widget button. Los widget son clases de la libreria tkinter 
# Button(root, text="Send", command=pulsar_boton).pack()

# # llamada a la ventana principal ( bucle infinito, bucle de ejecucion ) 
# root.mainloop()

# ejercicios 

from tkinter import *

# instacia de la ventana principal 
root = Tk()
root.geometry("400x400+50+50")

# eventos 
def pulsar_b(boton_num):
    etiqueta = Label(root, text=f"Boton {boton_num} pulsado")
    etiqueta.pack()

# titulo
root.title("Curso de tkinder en programacion facil")

# botones 
Button(root, text="Send-1", command=lambda:pulsar_b(1)).pack()
Button(root, text="Send-2", command=lambda:pulsar_b(2)).pack()
Button(root, text="Send-3", command=lambda:pulsar_b(3)).pack()
Button(root, text="Send-4", command=lambda:pulsar_b(4)).pack()


# bucle de ejecucion 
root.mainloop()