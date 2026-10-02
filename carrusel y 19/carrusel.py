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

#QUEMAR CÓDIGO: Usamos una lista con los nombres de las archivos.
# Si quieres agregar más fotos, solo las añades a esta lista.
archivos_imagenes = [
    'OIP-16028716.jpg',
    'OIP-2381066382.jpg',
    'OIP-2665566393.jpg'
]

# ORDENAR CÓDIGO DE NODOS: Carga dinámica usando un bucle
nodos = []
for archivo in archivos_imagenes:
    # Abrimos, redimensionamos y convertimos cada imagen dinámicamente
    imagen_cargada = ImageTk.PhotoImage(Image.open(archivo).resize((img_width, img_height)))
    nodos.append(Nodo(imagen_cargada))

# Conectar los nodos (circularidad)
total_nodos = len(nodos)
for i in range(total_nodos):
    nodos[i].next = nodos[(i + 1) % total_nodos]
    nodos[i].prev = nodos[(i - 1) % total_nodos]

# Empezar desde el primer nodo
nodo_actual = nodos[0]

# MOSTRAR LA IMAGEN
lbl_img = Label(window, image=nodo_actual.imagen)
lbl_img.grid(row=0, column=0, columnspan=3)

# CAMBIAR DE IMAGEN
def cambiar_imagen(direccion):
    global nodo_actual
    if direccion == 1:
        nodo_actual = nodo_actual.next
    elif direccion == -1:
        nodo_actual = nodo_actual.prev
    
    lbl_img.config(image=nodo_actual.imagen)

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

for key, command in keyboard_shortcuts.items():
    window.bind(f'<{key}>', command)

# INICIAR
window.mainloop()
