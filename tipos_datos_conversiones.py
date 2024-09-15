###tipos de datos, conversiones, operaciones y mas###

#comillas dentro de strings
print("hola 'a todos' como estan?")

#funcion len() solo se puede usar con los string

frase = "Que lindo dia es hoy"
print(len(frase))

## tipos de datos 

numero_1 = 200
numero_2 = 25.550
cadena = "esto es un string"
booleano = True 

# la funcion type() nos permite saber de que tipo de dato en una variable
print(type(numero_1))
print(type(numero_2))
print(type(cadena))
print(type(booleano))

numero_int = 5025042098

print(len(str(numero_int))) # se transforma a sting para poder hacer la operacion con la funcion len

## con la funcion round() podemos redondear los numeros de decimales a enteros o con 2 decimales despues de la ","

suma_decimal_1 = "5.5403"
suma_decimal_2 = "10.7685"

suma_total = float(suma_decimal_1) + float(suma_decimal_2) # convertimos a numero flotante para poder hacer la operacion
print(suma_total)
print(type(suma_total))
# con la funcion round() redondeamos a entero toda la operacion
print(round(suma_total))

# con la funcion round() pasandole despues de la "," cuantos decimales queremos
print(round(suma_total, 2))


## divisiones con el operator floor disivion con la sintaxis "//"

division = 10 / 3
division_floor = 10 // 2

print(division)
print(type(division))

# resultado con el operador floor "//"
print(division_floor)
print(type(division_floor))

## el operador modulo con la sitaxis "%" esto devuelve el resto o reciduo de una division

division_resto = 7 % 2 

print(division_resto) # estudiar mas a profundidad este tema

## operadores de incremento y decremento

# +=
# -=

digit = 10
digit += 10

print(digit)

digit -= 3
print(digit)

## formateo de strings 

suma = 90 + 67
print(type(suma))

print("el resultado de la suma es = " + str(suma))# convertimos la variable "suma" a string para poder hacer la concatenacion y que se muestre correctamente el resultados de la operacion

# Otra manera mas optima de hacer este formateo es con el ooperator "f" para formatear strings
print(f"el resultado de la suma es = {suma}")

###Ejercicios del tema 2, tipos de datos, conversiones, operaciones y mas###
print("###Ejercicios del tema 2, tipos de datos, conversiones, operaciones y mas###")

#ejercicio 1 al 4
palabra = "automaticamente"
print(len(palabra))
print((palabra[5]))

#ejercicio 5
exponente = 10 ** 5
print(exponente)

# ejercicio 8 
numero_float = 685.87
print(type(numero_float))

# ejercicio 9
count_digit = 768763823
print(len(str(count_digit)))

#ejercicio 10

float_1 = "14.527"
float_2 = "560.92"

conversion_float_1 = float(float_1) 
conversion_float_2 = float(float_2)

conversion_int_1 = int(conversion_float_1)
conversion_int_2 = int(conversion_float_2)
print(conversion_int_1, conversion_int_2)

# solucion 2
float_1 = float("14.527")
float_2 = float("560.92")
print(int(float_1), int(float_2))


#ejercicio 11
round_number_1 = 10.897654876534
round_number_2 = 7674.7886
round_number_3 = 68754.78

print(
    round(round_number_1, 3),
    round(round_number_2, 2),
    round(round_number_3, 1)
)

#ejercicio 13 
number_incre = 10 
number_decre = 24
number_incre_2 = 65.67

number_incre += 60
number_decre -= 100
number_incre_2 += 4.33
print(
    number_incre,
    number_decre,
    number_incre_2
)

#ejercicio 14 
number_1 = 4
number_2 = 769.97
text = "am I a string"
decision = True

print(f"El valor {number_2} es bastante mas grande que {number_1}. {text.capitalize()}? the answer is {decision}")

###proyect tema de tipos de datos, conversiones, operaciones y mas###

print("--- Calculadora de exponentes ---")

# datos que ingresara el usuario, numeros enteros. Debemos de transformarlos ya que los input almacenan strings
input_user = int(input("Introduzca el primer numero. \n"))
input_user_2 = int(input("Introduzca el segundo numero. \n"))

#operacion de la calculadora  
result = input_user ** input_user_2
print(f"El resultado de {input_user} elevado a {input_user_2} es = {result}")