# # explicacion de las funciones lambdas. 

# import tkinter as tk

# # funcion normal
# def mult(a, b):
#     return a * b


# # funcion lambda, aca le asignamos la funcion a una variable para poder utilizarla en el programa
# multiplicacion = lambda a, b : a * b

# # declaracion y llamada a una funcion lambda en la misma linea 
# (lambda a, b : print(a * b)) (29, 3)

# calculo = mult(10, 3)

# root = tk.Tk()

# root.title("Multiplicacion")

# # tamano de la ventana root
# root.geometry("600x400+50+45")

# mensaje = tk.Label(root, text=f" El resultado de la funcion normal es = {calculo}")
# mensaje_2 = tk.Label(root, text=f" El resultado de la funcion lambda es = {multiplicacion(20, 4), multiplicacion(3, 4)}")
# mensaje.pack()
# mensaje_2.pack()

# root.mainloop()

# ejercicios

# ejercicio 1, calculadora de areas de un circulo con una funcion lambda

user_radio = float(input("Ingresa el area del circulo en 'cm' = "))

PI  = 3.14159265

# le asignamos la funcion lambda a la variable radio 
radio = lambda radio : PI * radio ** 2

area = round(radio(user_radio), 2)

print(f"EL area calculada es de : {area} cm")

# ejercicio 2, mostrar un mensaje en la pantalla. Con la expression lambda en la un misma linea.


(lambda name : print(f"Hola {name}")) ("Armando Colina") # declaracion y llamado de la funcion en la misma linea, la sintaxis

# ejercicio 3, mostrar frase con una funcion lambda 

colores = ["rojo", "azul", "verde", "amarillo"]

(lambda color : print(f"El color se encuentra en la posicion {colores.index(color)} de la lista")) ("azul")