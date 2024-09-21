# # Mas metodos de los strings 

# # definicion de strings 
# name = "armando"
# lastname = "colina"

# # metodo de la clase str.
# print(" ".join([name, lastname]))

# # metodo format 
# print("{} {}".format(name, lastname))

# # formateo convencional 
# print(f"{name} {lastname}")

# ejercicios 1

# frase = ["Estoy", "aprendiendo", "Python", "con", "el", "curso", "de", "100", "días", "de", "Programación", "Fácil."]

# print(" ".join(frase))

# ejercicios 2

# colores = ["rojo", "azul", "verde", "amarillo"]
# GUION = "-"
# PUNTO = "."

# for color in colores:
#     print("{}{}{}".format(GUION, color.capitalize(), PUNTO))

# ejercicios 3

# numero_1 = 10
# numero_2 = 34.50
# resultado = numero_1 * numero_2

# print("La multiplicacion de %i * %.3f da como resultado: %.3f" % (numero_1, numero_2, resultado))

# ejercicios 4

# poema = "Podrá nublarse el sol eternamente; Podrá secarse en un instante el mar; Podrá romperse el eje de la tierra Como un débil cristal. ¡Todo sucederá! Podrá la muerte Cubrirme con su fúnebre crespón; Pero jamás en mí podrá apagarse La llama de tu amor."

# print("###-Busca una letra-###")

# letter_user = input("Indica la letra que quieres buscar: \n")
# letter_count = 0
    
# for letter in poema: 
#     if letter_user in letter:
#         letter_count += 1
        
# print(f'Se encontro {letter_count} veces la letra "{letter_user}"')


