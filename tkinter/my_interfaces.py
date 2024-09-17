from tkinter import *

NAME = "Armando Colina"
# creacion de la ventana main
root = Tk()

# titulo de la ventana main 
root.title("Curso de programacion facil")

# tamano de la ventana main 
root.geometry("600x450+50+75")

# mensajes, mostrar mensajes
mensaje = Label(root, text="Hola este es mi primero programa").grid(column=0, row=1)
mensaje_2 = Label(root, text=f"Bienvenido {NAME}").grid(column=1, row= 1)

root.mainloop()
