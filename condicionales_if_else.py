### condicionales ###

# my_condicion = True

# if my_condicion: 
#     print('Se ejecuta la condicion if')
    
# print('Se ejecucion continua')

# my_string = ""

# input_user = input('Ingresa el nombre de usuario valido: ')

# if input_user == "armandoc26":
#     my_string = "Lograste ingresar correctamente"
#     my_string.upper()
# else: 
#     print("ingresa un nombre de usuario valido")

# print(my_string)

# 1. Calcular la calificación final de un estudiante:

# Un estudiante ha realizado tres exámenes en una materia. La calificación final se calcula como el promedio de los tres exámenes, con la siguiente ponderación:

# Primer examen: 30%
# Segundo examen: 35%
# Tercer examen: 35%
# Escriba un programa que solicite al usuario las calificaciones de los tres exámenes y muestre la calificación final del estudiante. Considere que las calificaciones están entre 0 y 100.

# p_examen = 0.30
# s_examen = 0.35
# t_examen = 0.35

# print("clasificacion final de los estudiantes")

# input_examen1 = float(input(f"Ingresa la calificacion del examen 1 (0 - 100) = "))
    
# if input_examen1 >= 0 and input_examen1 <= 100:
#     calcular_promedio = input_examen1 * 0.30
#     print(f"El promedio del examen es: {calcular_promedio}")


### Condicionales if, elif, else y match de python o switch###

# las condicionales son estructuras de control de flujo de trabajo en un programa


# numero = 7 

# if numero > 7:
#     print("El numero es mayor que 7.")
# elif numero == 7:
#     print("El numero es igual a 7")
# else:
#     print("El numero es menor o igual a 7")

### if anidados ###
# explicado con un programa para vender alcholes a los mayores de edad

# # bienvenida
# print("Bienvenido a Licores de la Colina")

# # pedimos la edad al usuario
# input_user_age = int(input("Por favor ingresa tu edad = "))

# # declaramos una variable para almacenar la respuesta del usuario
# response = None # la declaramos con el tipo de dato "None" para pasarle un valor luego

# # control de flujo del programa
# if input_user_age >= 18:
#     print("Es mayor de edad puede comprar alcohol. cual desea? Introduzca una opcion que este Disponible: ")

#     #aqui le asignamos valor a nuestra variable "response" creada mas arriba
#     response = input("1- ron. \n2- whisky. \n3- ginebra. \n")

#     if response == "1":
#         print("Ha elegido comprar ron.")
#     elif response == "2":
#         print("Ha elegido comprar whisky.")
#     elif response == "3":
#         print("Ha elegido comprar ginebra.")
#     else:
#         print("Opcion no valida")

# else: 
#     print("Es menor de edad, vuelva de aqui a un tiempo. Hasta cumplir 18")

### operadores logicos, nos permiten crear codicionales aun mas complejos ###

# and == y 
# or == o
# not == no

# color = "amarillo"
# forma = "triangulo"
# tamano = "grande"

# ## operador and 
# if color == "rojo" and forma == "circulo":
#     print("Es un circulo rojo")
# else:
#     print("No se cumple la condicion")  

# ### podemos hacer mas de 2 concatenaciones de operadores logicos en una operacion
# if color == "rojo" and forma == "circulo" and tamano == "grande":
#     print("Es un circulo rojo")
# else:
#     print("No se cumple la condicion")

# ## operador or
# if color == "rojo" or forma == "circulo" or tamano == "grande":
#     print("Es un circulo rojo")
# else:
#     print("No se cumple la condicion")

# ##operador not: este elvalua lo contrario a una operacion True
# if not color == "azul":
#     print("Se cumple la condicion")
# else:
#     print("No se cumple la condicion")

# ## operacion mas compleja con el operador not 

# if not(color == "azul" and forma == "cuadrado"): # lo encerramos entre parentesis para que not considere las los evaluaciones en una misma operacion. de igual manera podria ser sin los parentesis
#     print("Se cumple la condicion")
# else: 
#     print("No se cumple la condicion")

# ### condicional match en python ###
# # el valor por default, en python se coloca un "_" por convencion, pero tambien se podria poner "default" y no daria ningun problema

# error = input("Introduzca un codigo de error:\n")

# match error:
#     case "200":
#         print("todo Ok.")
#     case "301":
#         print("movimiento permanente de la pagina")
#     case "302":
#         print("movimiento temporal de la pagina")
#     case "404":
#         print("pagina no encontrada")
#     case "500":
#         print("error interno del servidor")
#     case "503":
#         print("servidor no disponible")
#     case _:
#         print("error no disponible")

### ejercicios de las condicionales if, elif, else, match ###

# numero = 10 

# if numero > 7:
#     print("verdadero")

# numero_1 = 10
# numero_2 = 10
# numero_3 = 15

# if numero_1 == numero_2 and numero_3 > numero_1:
#     print("Se cumple la condicion")
# else: 
#     print("No se cumple la condicion")

### proyecto tema de condicionales ###

# titulo de la calculadora
print(" === Calculadora condicional === \n")

# solucion 1

# opciones a seleccionar 
print("Hola, elija una opcion: ")
print("1- Suma")
print("2- Resta")
print("3- Multiplicacion")
print("4- Division")
print("5- Modulo") 

input_user = int(input("Teclee un numero y pulse ENTER: \n"))


# flujo de trabajo del programa 
match input_user:
    case 1:
        print("Ha elegido la opcion 'Suma'.")
        input_operando_1 = float(input("Especifique el primer operando:\n"))
        input_operando_2 = float(input("Especifique el segundo operando:\n"))
        suma = input_operando_1 + input_operando_2
        print(f"\nEl resultado de sumar {input_operando_1} mas {input_operando_2} es: {round(suma, 2)}")
    case 2:
        print("Ha elegido la opcion 'Resta'.")
        input_operando_1 = float(input("Especifique el primer operando:\n"))
        input_operando_2 = float(input("Especifique el segundo operando:\n"))
        resta = input_operando_1 - input_operando_2
        print(f"\nEl resultado de restar {input_operando_1} menos {input_operando_2} es: {round(resta, 2)}")
    case 3:
        print("Ha elegido la opcion 'Multiplicacion'.")
        input_operando_1 = float(input("Especifique el primer operando:\n"))
        input_operando_2 = float(input("Especifique el segundo operando:\n"))
        multiplicacion = input_operando_1 * input_operando_2
        print(f"\nEl resultado de multiplicar {input_operando_1} por {input_operando_2} es: {round(multiplicacion, 2)}")
    case 4:
        print("Ha elegido la opcion 'Division'.")
        input_operando_1 = float(input("Especifique el primer operando:\n"))
        input_operando_2 = float(input("Especifique el segundo operando:\n"))
        division = input_operando_1 / input_operando_2
        print(f"\nEl resultado de dividir {input_operando_1} entre {input_operando_2} es: {round(division, 2)}")
    case 5:
        print("Ha elegido la opcion 'Modulo'.")
        input_operando_1 = float(input("Especifique el primer operando:\n"))
        input_operando_2 = float(input("Especifique el segundo operando:\n"))
        modulo = input_operando_1 % input_operando_2
        print(f"\nEl resultado del modulo de {input_operando_1} con {input_operando_2} es: {round(modulo, 2)}")
    case 6:
        print("Ha elegido la opcion 'Exponente'.")
        input_operando_1 = float(input("Especifique el primer operando:\n"))
        input_operando_2 = float(input("Especifique el segundo operando:\n"))
        exponente = input_operando_1 ** input_operando_2
        print(f"\nEl resultado del exponente de {input_operando_1} por {input_operando_2} es: {round(exponente, 2)}")
    case _:
        print("Error, opcion Invalida. \nPor favor, vuelva a ejecutar la calculadora")




# solucion 2

selection = input("Hola, elija una opcion: \n1- Suma. \n2- Resta. \n3- Multiplicacion. \n4- Division. \n5- Modulo. \n6- Exponente. \n\nTeclee un numero y pulse ENTER \n")


#flujo de trabajo del programa
if selection == "1":
    print("Ha elegido la opcion 'Suma'.")
    input_operando_1 = float(input("Especifique el primer operando:\n"))
    input_operando_2 = float(input("Especifique el segundo operando:\n"))
    suma = input_operando_1 + input_operando_2
    print(f"\nEl resultado de sumar {input_operando_1} mas {input_operando_2} es: {round(suma, 2)}")
elif selection == "2":
    print("Ha elegido la opcion 'Resta'.")
    input_operando_1 = float(input("Especifique el primer operando:\n"))
    input_operando_2 = float(input("Especifique el segundo operando:\n"))
    resta = input_operando_1 - input_operando_2
    print(f"\nEl resultado de restar {input_operando_1} menos {input_operando_2} es: {round(resta, 2)}")
elif selection == "3":
    print("Ha elegido la opcion 'Multiplicacion'.")
    input_operando_1 = float(input("Especifique el primer operando:\n"))
    input_operando_2 = float(input("Especifique el segundo operando:\n"))
    multiplicacion = input_operando_1 * input_operando_2
    print(f"\nEl resultado de multiplicar {input_operando_1} por {input_operando_2} es: {round(multiplicacion, 2)}")
elif selection == "4":
    print("Ha elegido la opcion 'Division'.")
    input_operando_1 = float(input("Especifique el primer operando:\n"))
    input_operando_2 = float(input("Especifique el segundo operando:\n"))
    division = input_operando_1 / input_operando_2
    print(f"\nEl resultado de dividir {input_operando_1} entre {input_operando_2} es: {round(division, 2)}")
elif selection == "5":
    print("Ha elegido la opcion 'Modulo'.")
    input_operando_1 = float(input("Especifique el primer operando:\n"))
    input_operando_2 = float(input("Especifique el segundo operando:\n"))
    modulo = input_operando_1 % input_operando_2
    print(f"\nEl resultado del modulo de {input_operando_1} con {input_operando_2} es: {round(modulo, 2)}")
elif selection == "6":
    print("Ha elegido la opcion 'Exponente'.")
    input_operando_1 = float(input("Especifique el primer operando:\n"))
    input_operando_2 = float(input("Especifique el segundo operando:\n"))
    exponente = input_operando_1 ** input_operando_2
    print(f"\nEl resultado del exponente de {input_operando_1} por {input_operando_2} es: {round(exponente, 2)}")
else:
    print("Error, opcion Invalida. \nPor favor, vuelva a ejecutar la calculadora")