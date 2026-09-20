from tkinter import *
from PIL import ImageTk, Image
# NODO
class Nodo:
    def __init__(self, imagen):
        self.imagen = imagen
        self.prev = None
        self.next = None
# VENTANA
window = Tk()
window.title('Carrusel Infinito')
# TAMAÑO DE LAS IMÁGENES
img_width = 400
img_height = 300
# CARGAR LAS IMÁGENES
img1 = ImageTk.PhotoImage(
    Image.open('OIP-16028716.jpg').resize((img_width, img_height))
)
img2 = ImageTk.PhotoImage(
    Image.open('OIP-2381066382.jpg').resize((img_width, img_height))
)
img3 = ImageTk.PhotoImage(
    Image.open('OIP-2665566393.jpg').resize((img_width, img_height))
)
# Crear los nodos
nodos = [
    Nodo(img1),
    Nodo(img2),
    Nodo(img3)
]
# Conectar los nodos
for i in range(len(nodos)):
    nodos[i].next = nodos[(i + 1) % len(nodos)]
    nodos[i].prev = nodos[(i - 1) % len(nodos)]
# for i in se uso para recorrer la lista de nodos y conectar 1 con 2 y 2 con 3 y 3 con 1, para q sea infinito 
# i: indica el nodo actual 
# Empezar desde el primer nodo
nodo_actual = nodos[0]
# MOSTRAR LA IMAGEN
lbl_img = Label(window, image=nodo_actual.imagen)
lbl_img.grid(row=0, column=0, columnspan=3)

#grind: amarra la imagen ala columna y fila en la ventana---
# CAMBIAR DE IMAGEN

def cambiar_imagen(direccion):

    global nodo_actual

    if direccion == 1:
        nodo_actual = nodo_actual.next

    elif direccion == -1:
        nodo_actual = nodo_actual.prev

    lbl_img.config(image=nodo_actual.imagen)
# global: es una variable que se puede usar en cualquier parte del programa, no solo en la función
# elif : es una abreviatura de else if, se usa para evaluar varias condiciones y ejecutar un bloque de código si se cumple alguna de ellas
# BOTÓN ATRÁS
btn_atras = Button(
    window,
    text='<-',
    command=lambda: cambiar_imagen(-1)
)
btn_atras.grid(row=1, column=0)
# BOTÓN ADELANTE
btn_adelante = Button(
    window,
    text='->',
    command=lambda: cambiar_imagen(1)
)
btn_adelante.grid(row=1, column=2)
# TECLADO
keyboard_shortcuts = {
    'Left': lambda event: cambiar_imagen(-1),
    'Right': lambda event: cambiar_imagen(1)
}
# lambda event: cambia la imagen al presionar el teclado 
for key, command in keyboard_shortcuts.items():
    window.bind(f'<{key}>', command)
# INICIAR

window.mainloop()
