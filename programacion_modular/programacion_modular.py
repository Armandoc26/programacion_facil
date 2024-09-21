# Explicacion de la programacion modular 

# La programacion modular consiste en dividir un programa grande en diversos modulos o subprogramas, aporta un mayor manejo del desarrollo y es mas facil de leer.

# Un modulo en python se crear a partir de un archivo nuevo, ejemplo en el directorio del programa principal se crear una nueva carpeta con el modulo que queremos implementar.

# al conjuntos de modulos de un programa lo podemos denominar como librerias o bibliotecas en espanol, en ese contexto los modulos seria los libros (tomese como ejemplo este simil).

# una biblioteca, es un cojunto de modulos.

# # Como dato, en si todos los archivos en python son un modulo. 
# import math 
# # como importar modulos propios o de terceros
# import suma

# def pow(a, b):
#     return a ** b

# calculo_1 = pow(2, 7)
# print(calculo_1)

# resultado = suma.sumar(2, 2)
# print(resultado)

# # ejemplos de acceder a los metodos del modulo importado (math)
# print(math.pi)

# print(math.pow(10, 2))

# ejercicio 1 

from tkinter import messagebox as tkmg 

resultado = tkmg.showinfo("www.programacionfacil.org", "Este es el mensaje informativo")
print(resultado)