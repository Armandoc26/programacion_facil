### listas y tuplas en python ###

# las listas son variables que pueden almacenar varios valores de diferentes tipos
# una buena practica es que estos datos esten relacionados entre si

# # lista_colores = ["negro", "blanco", "amarillo", "azul"]

# print(lista_colores)
# print(lista_colores[0])
# print(f"este es el tercer color, con la tercera letra: {lista_colores[2]} {lista_colores[2][2]}")

# # sustituir valores dentro de una lista 
# lista_colores[2] = "verde"
# print(lista_colores)

# # agregar valores a una lista
# lista_colores.append("morado")
# print(lista_colores)

# # el metodo insert() nos permite controlar la posicion especifica donde queremos incluir un nuevo elemento
# lista_colores.insert(1, "dorado")
# print(lista_colores)

# #metodos para eleminar los elementos de una lista (todos)
# # lista_colores.clear()

# # con el metodo pop podemos eleminar un elemento de la lista, mediante su posicion en la lista
# lista_colores.pop(4)
# print(lista_colores)

# # con el metodo remove podemos eleminar un elemento, indicando su valor literal
# lista_colores.remove("blanco")
# print(lista_colores)

### ejercicios tema de listas y tuplas ###

# ejercicio 1 
lista_numeros = [10, 45, 55, 76]
print(lista_numeros)
print(lista_numeros[3])

print(f"El valor mas pequenio en la lista es el {lista_numeros[0]}. El mas grande, es {lista_numeros[3]}")

lista_colores = ["rojo", "azul", "verde", "amarillo"]
print(lista_colores[1][2])

# ejercicio 2
lista_colores.insert(0, "gris")
lista_colores.append("rosa")
lista_colores.insert(3, "naranja")
# print(lista_colores)

# eleminar elementos con el metodo pop
# lista_colores.pop(1)
# print(lista_colores)
# lista_colores.pop(3)
# print(lista_colores)
# lista_colores.pop(3)
# print(lista_colores)

# ejercicio 3 duplicar listas

lista_colores_duplicada = lista_colores.copy()
print(lista_colores_duplicada)
print(lista_colores)

# ejercicio 4 ordenar lista de menor a mayor 
lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
lista_numeros.sort()
print(lista_numeros)
lista_numeros.sort(reverse=True)
print(lista_numeros)

lista_colores_duplicada.extend("cromado")
print(lista_colores_duplicada)