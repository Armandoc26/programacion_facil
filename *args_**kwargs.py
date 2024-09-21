# *args **kwargs son dos elementos de python que nos van a permitir usar multiples argumentos en las funciones

# EJEMPLOS DE *args
# recibe argumentos posicionales
# nos devuelve una tupla
# def prueba(*args):
#     valor = 0
#     for i in args:
#         valor += 1 
#         print(f"El argumento nuemro {valor} es {i}")


# prueba("armando", "jose", "colina", "sanchez")

# EJEMPLOS DE **kwargs
# recibe argumentos por clave
# nos devuelve un direccionario
# def prueba_kwargs(**kwargs):
#     number = 0
#     for clave in kwargs.keys():
#         number += 1
#         print(f"clave: {number}: {clave}")

# prueba_kwargs(nombre="armando", apellido="colina", edad="27")


# def imprimir_kwargs(**kwargs):
#     for i in kwargs.items():
#         print(f"{i[0].capitalize()} = {i[1]}")
            
# diccionario = {"name": "armando", "lastname": "colina", "age": 27}

# imprimir_kwargs(**diccionario)

# ejercicio 1 

def show_info(**kwargs):
    print("$$$-- Datos del usuario --$$$")

    data_user = []
    for data in kwargs.values():
        data_user.append(data)
    
    print(f"el nombre es {data_user[0]}, sus apellidos son {data_user[1]} y tiene {data_user[2]} annos de edad.")


user = {"nombre": "javier", "apellidos": "gomez de la barca", "edad": "27"}
user_1 = {"nombre": "armando", "apellidos": "colina sanchez", "edad": "27"}

show_info(**user)
show_info(**user_1)