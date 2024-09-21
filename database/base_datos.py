# Las bases de datos es un conjunto de datos almacenados conectados o relaciones entre si, estas bases de datos forman una estructura de tablas.

# una tabla es una seria de filas o coloumnas, ejemplos lo podemos en una hoja de calculo 

# para almacenar datos en una base de datos debemos crear tablas.

import mysql.connector
import mysql.connector.cursor

# conexion con la base de datos 
PASSWORD_SERVER = "JdmIK9HzZq2SxLeC7w1xzahfaHZTYTT"

db = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = PASSWORD_SERVER,
    database = "american_rider"
)

# instanciamos un cursor que es el handle de nuestras base de datos
cursor = db.cursor()

# el metodo execute es para ejecutar operaciones en las bases de datos 
# manejos los errores y posibles errores con python para hacer la UX mas confortable 

try: 
    # creacion de tables en en la base de datos de american_rider 
    cursor.execute("""
        CREATE TABLE cliente(
            id INT NOT NULL AUTO_INCREMENT,
            nombre VARCHAR(32) NOT NULL, 
            apellidos VARCHAR(64) NOT NULL,    
            telefono VARCHAR(9) NOT NULL,
            direccion VARCHAR(256) NOT NULL,
            PRIMARY KEY (id)
        )
    """)

    print("Se creo correctamenta la tabla clientes")

except:
    print("Ocurrio un error en la creacion de la base de datos") 



