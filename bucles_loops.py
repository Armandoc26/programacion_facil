# ### Bucles o loops en python ###

# # los bucles son estructuras de control de flujo que nos permiten realizar repeticiones en el codigo. en python tenemos varios tipos de bucles, for, while y do while (no existe en python)

# # flujo de ejecucion

# # sintaxis buble for (range() es un metodo en python que revuelve un rango de numeros)

# for i in range(5):
#     print(f"el valor del bucle es: {i}")

# # metodo range(start, stop, step (agregar un incremente o decremento))

# for i in range(3, 10):
#     print(f"el valor del bucle es: {i}")


# # Sintaxis del bucle while 

# i = 0

# while(i > 5):
#     print(f"el valor de i es: {i}")

# ###funcionalidades que se pueden hacer con los bucles###

# # iterrar sobre una lista o tupla

# colores = ["rojo", "azul", "verde", "amarillo"]

# print("***Lista de colores***")

# for color in colores:
#     print(f" * {color}")

# # condicionales dentro de los bucles

# for color in colores:
#     if color == "azul" or color == "verde":
#         print("se ha saltado este valor")
#         continue # continua con el bucle
#         # break # rompe el bucle
#     print(f"-Color {color}.")

# print("bucle while")

# i = 0

# while i < 5:
#     print(f"el valor del bucle es: {i}")
#     i += 1


# ### emulador la funcionalidad del bucle do while en python ###

# # while True:
# #     salida = input("Intoduce salir para finalizar:\n").lower()
# #     print("Haz salido del programa")
# #     break

# ### ejercicios practicos ###

# #ejercicio 1 
# # for i in range(6, 15):
# #     print(f"El valor del bucle es: {i}.")

# #ejercicio 2
# i = 7

# while i <= 14:
#     print(f"El valor del bucle es: {i}.")
#     i += 1

#ejercicio 3 
# for i in range(0, -5001, -500):
#     print(f"El valor del bucle es: {i}.")

# i = 0

# while i >= -5000:
#     print(f"El valor del bucle es: {i}.")
#     i -= 500

# ejercicio 4

# paises = ["Afghanistan","Albania","Algeria",
# "Andorra","Angola","Anguilla",
# "Antigua and Barbuda",
# "Argentina","Armenia",
# "Aruba","Australia","Austria",
# "Azerbaijan","Bahamas","Bahrain",
# "Bangladesh","Barbados","Belarus",
# "Belgium","Belize","Benin","Bermuda",
# "Bhutan","Bolivia","Bosnia & Herzegovina",
# "Botswana","Brazil","British Virgin Islands",
# "Brunei","Bulgaria","Burkina Faso","Burundi",
# "Cambodia","Cameroon","Cape Verde",
# "Cayman Islands","Chad","Chile","China",
# "Colombia","Congo","Cook Islands",
# "Costa Rica","Cote D Ivoire","Croatia",
# "Cruise Ship","Cuba","Cyprus","Czech Republic",
# "Denmark","Djibouti","Dominica",
# "Dominican Republic","Ecuador","Egypt",
# "El Salvador","Equatorial Guinea",
# "Estonia","Ethiopia","Falkland Islands",
# "Faroe Islands","Fiji","Finland","France",
# "French Polynesia","French West Indies","Gabon",
# "Gambia","Georgia","Germany","Ghana","Gibraltar",
# "Greece","Greenland","Grenada","Guam","Guatemala",
# "Guernsey","Guinea","Guinea Bissau","Guyana",
# "Haiti","Honduras","Hong Kong","Hungary","Iceland",
# "India","Indonesia","Iran","Iraq","Ireland",
# "Isle of Man","Israel","Italy","Jamaica","Japan",
# "Jersey","Jordan","Kazakhstan","Kenya","Kuwait",
# "Kyrgyz Republic","Laos","Latvia","Lebanon",
# "Lesotho","Liberia","Libya","Liechtenstein",
# "Lithuania","Luxembourg","Macau","Macedonia",
# "Madagascar","Malawi","Malaysia","Maldives",
# "Mali","Malta","Mauritania","Mauritius","Mexico",
# "Moldova","Monaco","Mongolia","Montenegro",
# "Montserrat","Morocco","Mozambique","Namibia",
# "Nepal","Netherlands","Netherlands Antilles",
# "New Caledonia","New Zealand","Nicaragua","Niger",
# "Nigeria","Norway","Oman","Pakistan","Palestine",
# "Panama","Papua New Guinea","Paraguay","Peru",
# "Philippines","Poland","Portugal","Puerto Rico",
# "Qatar","Reunion","Romania","Russia","Rwanda",
# "Saint Pierre & Miquelon","Samoa","San Marino",
# "Satellite","Saudi Arabia","Senegal","Serbia",
# "Seychelles","Sierra Leone","Singapore","Slovakia",
# "Slovenia","South Africa","South Korea","Spain",
# "Sri Lanka","St Kitts & Nevis","St Lucia",
# "St Vincent","St. Lucia","Sudan","Suriname","Swaziland",
# "Sweden","Switzerland","Syria","Taiwan","Tajikistan",
# "Tanzania","Thailand","Timor L'Este","Togo","Tonga",
# "Trinidad & Tobago","Tunisia","Turkey","Turkmenistan",
# "Turks & Caicos","Uganda","Ukraine",
# "United Arab Emirates","United Kingdom","Uruguay",
# "Uzbekistan","Venezuela","Vietnam",
# "Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]


#con el bucle for
# for pais in paises:
#     print(f"- {pais}")


# con el bucle while
# i = 0 

# while i < len(paises):
#     element = paises[i]
#     print(f"- {element}")
#     i += 1

## ejercicio numero 5

# lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]

# # ordenamos la lista de menor a mayor para poder conseguir el resultado.
# lista_numeros.sort()

# for number in lista_numeros: 
#     if number == 10: 
#         continue # se omiten los valores 10

#     elif number == 356:
#         break # se rompe con el valores 356

#     else:
#         print(f"El valor del elemento es: {number}")

# print(lista_numeros)

### proyecto bucles o loops ###

print("---> Pizzeria La Colina <---")

# input para ingresar el dinero
dinero = float(input("Ingresa el dinero que tienes para prepararte una pizza a medida:\n"))

# dinero disponible por el usuario
DINERO_INICIAL = dinero
TOTAL = 0
VUELTO = 0
pedido = []

# definimos las variables de las pizzas
margarita = 7.85
jamon_queso = 9.65
cuatro_quesos = 8.95

extra_queso = 1.25
champinones = 0.85
albahaca = 0.5

print(" --- En preparacion ---\n")

# int(input(f"1 - margarita - {margarita}\n2 - Jamon y queso - {jamon_queso}\n3 - Cuatro quesos - {cuatro_quesos}\n"))

input_pizza = int(input(f"1 - margarita - {margarita}\n2 - Jamon y queso - {jamon_queso}\n3 - Cuatro quesos - {cuatro_quesos}\n"))

match input_pizza:
    case 1:
        print(f"Haz seleccionado la pizza - Margarita -")
        print(f"Total a pagar: {TOTAL + margarita}$")
        print(f"Le quedan: {DINERO_INICIAL - margarita}$")
        pedido.append(margarita)
    case 2:
        print(f"Haz seleccionado la pizza - Jamon y queso -")
        print(f"Total a pagar: {TOTAL + jamon_queso}$")
        print(f"Le quedan: {DINERO_INICIAL - jamon_queso}$")
        pedido.append(jamon_queso)
    case 3:
        print(f"Haz seleccionado la pizza - Cuatro quesos -")
        print(f"Total a pagar: {TOTAL + cuatro_quesos}$")
        print(f"Le quedan: {DINERO_INICIAL - cuatro_quesos}$")
        pedido.append(cuatro_quesos)

print("\n")
print("Seleccione algun incrediente extra\n")

# seleccion de ingredientes extras 
# creamos un diccionario, para poder recorrer los valores.
dict_IE = {"1. Queso extra": extra_queso, "2. Champinones": champinones, "3. Albahaca": albahaca, "4. No anadir algo extra y pagar": None}
items = dict_IE.items()

for clave, valor in items:
    if valor == None:
        print("4. No anadir algo extra y pagar")
        continue
    print(f"{clave}: {valor}")

# crearemos el flujo de procesos para los IE (ingredientes extras)

input_IE = int(input("Si desea algun ingrediente extra, Seleccionelo: \n"))

# condicionales para el flujo {

# if input_IE == 1:
#     print(f"Extra a pagar: {extra_queso}")
#     print(f"Total a pagar: {extra_queso += TOTAL}")
#     print(f"Le quedad: {quedan}")


 