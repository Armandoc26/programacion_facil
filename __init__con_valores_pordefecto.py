# __init__ con valor por defecto

class User():

    # metodo constructor 
    def __init__(self, telephone, name="usuario", lastname="apellido", age=0):
        self.telephone = telephone
        self.name = name
        self.lastname = lastname
        self.age = age

    def describe(self):
        print(f"Nombre : {self.name}") 
        print(f"Apellido : {self.lastname}") 
        print(f"Edad : {self.age}") 
        print(f"Telefono : {self.telephone}") 

# instancias de la clase User()
user_1 = User("90234", "Armando", "Colina", 27)
user_2 = User("2193049", "Joao", "Gonzalez", 34)
user_3 = User("9023421324")

# argumentos por claves 
user_4 = User(lastname="Oliviera", age=20, telephone="90234324")

print(user_1.describe())
print(user_2.describe())
print(user_3.describe())
print(user_4.describe())