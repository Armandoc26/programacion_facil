# ejercicios del archivo tk_img_routing
from tkinter import *
import os 
from PIL import ImageTk, Image 

ruta = os.path.dirname(__file__)
direct_img = os.path.join(ruta, "img")

# creacion de la ventana
root = Tk()
root.title("Curso de programacion facil")

#favicon de la ventana 
root.iconbitmap(os.path.join(direct_img, "favicon_circle_logo.ico"))

#motos 
# ruta al directorio de las motos
motos = os.path.join(direct_img, "motos")

motocycles = [os.path.join(motos, "moto_1.jpg"), os.path.join(motos, "moto_2.jpg"), os.path.join(motos, "moto_3.jpg"), os.path.join(motos, "moto_4.jpg")]

# imagenes 
img = ImageTk.PhotoImage(Image.open(motocycles[0]))

# bucle de ejecucion 
root.mainloop()