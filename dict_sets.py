# diccionarios y conjuntos en python, estructura de datos 


# diccionarios (dict)

# person = {
#     "name": "Armando",
#     "age": 27,
#     "oficio": "constructor",
#     "is_developer": True,
#     "invoices": 3000000
# }

# person["is_soltero"] = True

# print(person["oficio"])
# print(person.keys())
# print(person.items())


# agregar items al inventario de un juego 
# import random
# items = {}

# def add_items(dict_inv):
#     key = input("Ingresa el items que quieres comprar = ")
#     value = random.randint(1, 100)
#     dict_inv[key] = value


# def delete_inv(dict_inv):
#     dict_inv = {}
#     return dict_inv


# def main():
#     items = {}
#     while input("Deseas ingresar un items en tu inventario? [pulsa ENTER]...[escribe SALIR] para salir = ") != "SALIR":
#         add_items(items)

#     delete = input("Deseas eliminar el inventario? = ").capitalize()
#     if delete == "Eliminar":
#         items = delete_inv(items)
#         print("Se a eliminado correctamente tu inventario")
#         print(items.items())
#     else:
#         print("\n--Inventario de proviciones--")
#         for i in items.items():
#             print(str(i[0]).capitalize()) 


# if __name__ == "__main__":
#     main()


# # conjuntos (sets)

# conjunto = ["perro", "iguana", "chivo", "piton", "aguila", "perro", "perro", "perro", "aguila"]

# set_conjunto = set(conjunto)
# print(set_conjunto)
# print(type(set_conjunto))


# ejercicios 

# # ejercicio #1

# colores = {
#     1: "rojo",
#     2: "azul",
#     3: "verde",
#     4: "amarillo",
# }

# colores[5] = "celeste"

# for key in colores:
#     print(f"{key} - {colores[key].capitalize()}")