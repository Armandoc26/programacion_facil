# programacion orientada a objetos en python.

# creacion de la clase vehiculo 

class Vehiculo():
    # atributos de la clase vehiculo 
    pais_origen = "Alemania"
    patente = 101010

    # constructor o inicializador de los atributos de la clase vehiculo.
    # Atributos de instancia de la clase vehiculo  
    def __init__(self, color, longitud_metros, ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas

    # metodos de la clase vehiculo 
    def encender(self):
        print("El vehiculo esta encendido")

    def arrancar(self):
        print("EL vehiculo ha partido")

    def detenido(self):
        print("El vehiculo esta detenido y apagado")

    def show_info(self):
        print(f"El color es {self.color}, tamano es {self.longitud_metros} metros y tiene {self.ruedas} ruedas")

# instaciando la clase vehiculo

carro_1 = Vehiculo("negro", 2, 4)
camion_1 = Vehiculo("plata", 5, 8)
auto_1 = Vehiculo("plomo", 3, 4)

print(carro_1.arrancar())
print(camion_1.detenido())

print(auto_1.patente)
print(carro_1.pais_origen)
print(auto_1.show_info())
 