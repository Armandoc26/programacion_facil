# Ejercicios 

class Motocicletas():
    # atributos de clase
    made_in = "Japon"
    status = "New"
    motor = False

    # atributos de instancias
    def __init__(self, color, patente, combustible_litros, marca, modelo, velocidad, precio, tanque_litros):
        self.color = color
        self.patente = patente
        self.combustible_litros = combustible_litros
        self.marca = marca 
        self.modelo = modelo
        self.velocidad = velocidad
        self.precio = precio
        self.tanque_litros = tanque_litros

    # metodos de la clase Motocicleta
    def arrancar(self):
        if self.motor == False:
            print("El vehiculo ha arrancado perfectamente")
            self.motor = True
        elif self.motor == True: 
            print("El motor del vehiculo ya estaba en marcha ")
            self.motor = False

    def detener(self):
        if self.motor == True:
            print("El motor se ha detenido")
            self.motor = False
        elif self.motor == False: 
            print("El motor ya estaba detenido")
            self.motor = True 

    def consultar_precio(self):
        print(f"El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio}$") 

    def comprobar_tanque(self):
        title_reporte = f"Reporte de deposito de combustible de la moto {self.marca} {self.modelo}"

        print(f"--> {title_reporte} <--")
        print(f"--> Combustible que tiene la moto: {self.combustible_litros} Lts")
        print(f"--> Capacidad del tanque: {self.tanque_litros} Lts")
        print(f"--> Faltan {self.tanque_litros - self.combustible_litros} Lts\n")

    def repostar_combustible(self):
        user_indicator = int(input("Indica la cantidad de combustible que quieres repostar: "))
        tope_combustible = self.tanque_litros - self.combustible_litros

        while True:
            if user_indicator > tope_combustible: 
                print(f"La cantidad es superior a la del tanque de combustible, debe repostar {self.tanque_litros - self.combustible_litros} Lts.\n")

                # volvemos a preguntar cuando combustible quiere repostar
                user_indicator = int(input("Indica la cantidad de combustible que quieres repostar: "))
            else: 
                print(f"\nRepostaje exitoso")
                print(f"--> Se han repostado {user_indicator} Lts")
                print(f"--> El tanque tiene {user_indicator + self.combustible_litros} Lts")
                break
    

# instancias de la Clase Motocicletas
moto = Motocicletas("Roja", 202020, 12, "kawasaki", "Chiron", 390, 10000, 20)

moto_yamaha = Motocicletas(
    color="blanca y roja", 
    modelo="Yha-kaka", 
    marca="yamaha", 
    velocidad=400, 
    combustible_litros=0, 
    patente=101010, 
    tanque_litros=18)

moto.comprobar_tanque()
moto.repostar_combustible()
moto.comprobar_tanque()
