# manejo de imagenes y rutas con tkinder
# importar directorios 
# modulos para imagenes, redimensionar imagenes, cambiar icono de ventada de tkinter 

# importacions 
import tkinter as tk 
import os 
from PIL import ImageTk, ImageColor, Image


#-- carga de directorios -- 
# directorio principal
direct_main = os.path.dirname(__file__) # optencion de ruta dinamicamente (__file__) esto es una variable especial de python

# directorio de imagenes
direct_img = os.path.join(direct_main, "img")
direct_paisajes = os.path.join(direct_img, "paisajes")

# creacion de ventana principal 
root = tk.Tk()
root.title("www.programacionfacil.org") 
# favicon de la ventana
root.iconbitmap(os.path.join(direct_img, "favicon_circle_logo.ico"))

#carga de imagen 
animal = ImageTk.PhotoImage(Image.open("/Users/armandocolina/Development/curso_programacion_facil/programacion_facil/img/paisajes/buei.jpg").resize((550, 400)))
etiqueta = tk.Label(image=animal)
etiqueta.pack()



# bucle de ejecucion
root.mainloop()