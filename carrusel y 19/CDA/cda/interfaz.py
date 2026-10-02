# interfaz.py
# Interfaz GRÁFICA del CDA con tkinter (viene incluido con Python). Se ejecuta con:  python interfaz.py
# Solo dibuja ventanas y botones; la lógica real sigue estando en cola_cda.py.

import tkinter as tk                      # tk = ventanas, etiquetas, botones, cajas de texto
from tkinter import ttk, messagebox       # ttk = widgets más modernos (tabla, lista desplegable); messagebox = ventanitas de aviso
from datetime import datetime             # para poner la hora en el historial
from vehiculo import Vehiculo, TIPOS_VALIDOS, validar_placa
from cola_cda import ColaCDA

# Colores en formato hexadecimal (#RRGGBB). Se definen una vez y se reutilizan.
FONDO, INK, GRIS = "#EEF1F2", "#14232B", "#5A6B73"
AMARILLO, ROJO, TEAL = "#FFC72C", "#C8372D", "#0F5C63"


# Nuestra ventana ES una ventana de tkinter (tk.Tk) con cosas extra: por eso la clase "hereda" de tk.Tk.
class App(tk.Tk):
    def __init__(self):
        super().__init__()                # Crea la ventana base de tkinter
        self.title("CDA - Sistema de atención")
        self.geometry("1000x680")         # Tamaño inicial: ancho x alto
        self.minsize(920, 620)            # No deja hacerla más pequeña que esto
        self.configure(bg=FONDO)          # bg = color de fondo
        self.cda = ColaCDA()              # La lógica: aquí viven las filas
        self.estilos()
        self.widgets()                    # Dibuja todo
        self.actualizar()                 # Llena la tabla y contadores por primera vez

    def estilos(self):
        """Colores y tamaños de la tabla."""
        st = ttk.Style(self)
        st.theme_use("clam")              # Tema que sí permite cambiar colores
        st.configure("Treeview", rowheight=28, font=("Segoe UI", 10))
        st.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"),
                     background=TEAL, foreground="white")
        # Al seleccionar una fila, se pinta amarilla.
        st.map("Treeview", background=[("selected", AMARILLO)],
               foreground=[("selected", INK)])

    def tarjeta(self, padre, titulo, color):
        """Crea una cajita con un título y un número grande (los contadores de arriba).
        Devuelve la etiqueta del número para poder cambiarlo después."""
        # highlightthickness es el grosor del borde de color.
        f = tk.Frame(padre, bg="white", highlightbackground=color, highlightthickness=2)
        # pack() coloca el elemento en la ventana. side="left" = uno al lado del otro.
        f.pack(side="left", expand=True, fill="x", padx=4)
        tk.Label(f, text=titulo, bg="white", fg=GRIS, font=("Segoe UI", 10)).pack(pady=(6, 0))
        n = tk.Label(f, text="0", bg="white", fg=color, font=("Segoe UI", 26, "bold"))
        n.pack(pady=(0, 6))
        return n

    def widgets(self):
        """Dibuja toda la pantalla. 'Widget' = cualquier elemento visual (botón, texto, tabla...)."""
        # ---- Encabezado ----
        cab = tk.Frame(self, bg=FONDO)    # Frame = caja contenedora para agrupar cosas
        cab.pack(fill="x", padx=16, pady=(14, 6))
        tk.Label(cab, text=" CDA ", bg=AMARILLO, fg=INK, bd=3, relief="solid",
                 font=("Segoe UI", 18, "bold")).pack(side="left")   # Parece una placa
        tk.Label(cab, text="  Sistema de atención de vehículos", bg=FONDO, fg=INK,
                 font=("Segoe UI", 16, "bold")).pack(side="left")

        # ---- Contadores: cuántos hay en total, de especiales y de normales ----
        cont = tk.Frame(self, bg=FONDO)
        cont.pack(fill="x", padx=12, pady=4)
        self.n_pend = self.tarjeta(cont, "Pendientes", TEAL)
        self.n_esp = self.tarjeta(cont, "Especiales", ROJO)
        self.n_nor = self.tarjeta(cont, "Normales", GRIS)

        # ---- Cuerpo: formulario a la izquierda, cola a la derecha ----
        cuerpo = tk.Frame(self, bg=FONDO)
        cuerpo.pack(fill="both", expand=True, padx=16, pady=8)
        # grid() coloca por filas y columnas. weight=1 hace que la columna 1 se estire al agrandar la ventana.
        cuerpo.columnconfigure(1, weight=1)
        cuerpo.rowconfigure(0, weight=1)

        # ---- Formulario (orden: tipo, placa, marca, color) ----
        form = tk.Frame(cuerpo, bg="white", padx=14, pady=12,
                        highlightbackground="#D3DBDE", highlightthickness=1)
        form.grid(row=0, column=0, sticky="ns", padx=(0, 12))
        tk.Label(form, text="Registrar vehículo", bg="white", fg=INK,
                 font=("Segoe UI", 13, "bold")).pack(anchor="w", pady=(0, 8))

        # StringVar = "variable especial" de tkinter: guarda lo que hay escrito en una caja
        # y permite leerlo (.get()) o cambiarlo (.set()) desde el código.
        self.tipo, self.placa = tk.StringVar(), tk.StringVar()
        self.marca, self.color = tk.StringVar(), tk.StringVar()

        tk.Label(form, text="1. Tipo de vehículo", bg="white").pack(anchor="w")
        # Combobox = lista desplegable. state="readonly" evita escribir texto libre (RF-10).
        cb = ttk.Combobox(form, textvariable=self.tipo, values=TIPOS_VALIDOS,
                          state="readonly", width=26)
        cb.pack(pady=(0, 8))
        tk.Label(form, text="2. Placa", bg="white").pack(anchor="w")
        # textvariable conecta la caja de texto con la variable de arriba.
        tk.Entry(form, textvariable=self.placa, width=28,
                 font=("Segoe UI", 11, "bold")).pack()
        # Esta etiqueta dice en vivo si la placa va bien (✔) o mal (✘).
        self.pista = tk.Label(form, text="Elige primero el tipo", bg="white", fg=GRIS,
                              font=("Segoe UI", 9))
        self.pista.pack(anchor="w", pady=(0, 8))
        tk.Label(form, text="3. Marca", bg="white").pack(anchor="w")
        tk.Entry(form, textvariable=self.marca, width=28).pack(pady=(0, 8))
        tk.Label(form, text="4. Color", bg="white").pack(anchor="w")
        tk.Entry(form, textvariable=self.color, width=28).pack(pady=(0, 10))

        # command=... es la función que se ejecuta al hacer clic.
        tk.Button(form, text="Registrar", command=self.registrar, bg=TEAL, fg="white",
                  font=("Segoe UI", 11, "bold"), relief="flat", pady=6).pack(fill="x")
        # Aquí salen los mensajes de éxito o error (wraplength = ancho máximo antes de saltar de línea).
        self.mensaje = tk.Label(form, text="", bg="white", wraplength=230, justify="left")
        self.mensaje.pack(anchor="w", pady=8)

        # trace_add("write", f) = "ejecuta f cada vez que cambie esta variable".
        # Así la placa se valida mientras la escribes.
        self.placa.trace_add("write", self.validar_en_vivo)
        self.tipo.trace_add("write", self.validar_en_vivo)

        # ---- Lado derecho: siguiente, tabla, botones e historial ----
        der = tk.Frame(cuerpo, bg=FONDO)
        der.grid(row=0, column=1, sticky="nsew")

        # Banner grande que dice quién sigue (rojo si es especial, amarillo si es normal).
        self.banner = tk.Label(der, text="", font=("Segoe UI", 15, "bold"), pady=10)
        self.banner.pack(fill="x")

        # Treeview = tabla. "columns" son los identificadores internos de cada columna.
        cols = ("pos", "placa", "tipo", "marca", "color", "prioridad")
        self.tabla = ttk.Treeview(der, columns=cols, show="headings", height=9)
        # zip(a, b, c) recorre tres listas al mismo tiempo: id de columna, título y ancho.
        for c, t, w in zip(cols, ("Pos.", "Placa", "Tipo", "Marca", "Color", "Prioridad"),
                           (50, 90, 100, 110, 90, 90)):
            self.tabla.heading(c, text=t)
            self.tabla.column(c, width=w, anchor="center")
        # Un "tag" es una etiqueta de estilo: las filas marcadas "esp" se pintan rosadas.
        self.tabla.tag_configure("esp", background="#FBE4E1")
        self.tabla.pack(fill="both", expand=True, pady=6)
        # bind = "cuando pase este evento, ejecuta esta función". Aquí: al seleccionar una fila.
        self.tabla.bind("<<TreeviewSelect>>", self.al_seleccionar)

        self.delante = tk.Label(der, text="Selecciona un vehículo para ver cuántos hay por delante.",
                                bg=FONDO, fg=GRIS, anchor="w")
        self.delante.pack(fill="x")

        botones = tk.Frame(der, bg=FONDO)
        botones.pack(fill="x", pady=6)
        tk.Button(botones, text="Atender siguiente", command=self.atender, bg=AMARILLO,
                  fg=INK, font=("Segoe UI", 11, "bold"), relief="flat",
                  padx=14, pady=6).pack(side="left")
        tk.Button(botones, text="Retirar seleccionado", command=self.retirar, bg="white",
                  fg=ROJO, font=("Segoe UI", 11, "bold"), relief="solid", bd=1,
                  padx=14, pady=6).pack(side="left", padx=8)

        tk.Label(der, text="Historial (lo que ya salió)", bg=FONDO, fg=INK,
                 font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(6, 2))
        # Listbox = lista simple de líneas de texto (aquí, el historial).
        self.historial = tk.Listbox(der, height=5, font=("Consolas", 10), bd=1)
        self.historial.pack(fill="x")

    # ---------------- LÓGICA DE LA PANTALLA ----------------

    # El "*_" recibe y descarta los argumentos que tkinter manda automáticamente al avisar un cambio.
    def validar_en_vivo(self, *_):
        """Muestra ✔ o ✘ mientras se escribe la placa."""
        tipo, placa = self.tipo.get(), self.placa.get().strip().upper()
        if not tipo:
            self.pista.config(text="Elige primero el tipo", fg=GRIS)
            return
        ejemplo = "ABC12D" if tipo == "moto" else "ABC123"
        if not placa:
            self.pista.config(text=f"Ejemplo: {ejemplo}", fg=GRIS)
        elif validar_placa(tipo, placa):
            self.pista.config(text="✔ Placa válida", fg=TEAL)
        else:
            self.pista.config(text=f"✘ Formato inválido. Ejemplo: {ejemplo}", fg=ROJO)

    def aviso(self, texto, color):
        """Escribe un mensaje bajo el botón Registrar."""
        self.mensaje.config(text=texto, fg=color)

    def log(self, accion, v):
        """Agrega una línea al historial con la hora."""
        hora = datetime.now().strftime("%H:%M:%S")   # strftime da formato a la hora
        # insert(0, ...) la pone de primera, así lo más reciente queda arriba.
        # {accion:<9} rellena con espacios hasta 9 caracteres para alinear las columnas.
        self.historial.insert(0, f"{hora}  {accion:<9} {v.placa}  ({v.tipo})")
        self.historial.itemconfig(0, fg=TEAL if accion == "ATENDIDO" else ROJO)

    def registrar(self):
        """Se ejecuta al pulsar 'Registrar'. Valida todo y, si está bien, lo manda a la cola."""
        tipo = self.tipo.get()
        placa = self.placa.get().strip().upper()
        marca, color = self.marca.get().strip(), self.color.get().strip()
        # "return self.aviso(...)" muestra el error y sale de la función de una vez.
        if not tipo:
            return self.aviso("Elige el tipo de vehículo.", ROJO)
        if not validar_placa(tipo, placa):
            return self.aviso("La placa no tiene el formato correcto.", ROJO)
        if not marca:
            return self.aviso("La marca es obligatoria.", ROJO)
        if not color.replace(" ", "").isalpha():   # solo letras (permite espacios)
            return self.aviso("El color solo admite letras.", ROJO)
        if self.cda.registrar(Vehiculo(placa, tipo, color, marca)):
            self.aviso(f"Vehículo {placa} registrado.", TEAL)
            for var in (self.tipo, self.placa, self.marca, self.color):
                var.set("")                        # Limpia el formulario
            self.actualizar()
        else:
            self.aviso("Esa placa ya está pendiente de atención.", ROJO)

    def atender(self):
        """Se ejecuta al pulsar 'Atender siguiente'."""
        v = self.cda.atender()
        if v is None:
            return messagebox.showinfo("CDA", "No hay vehículos pendientes.")
        self.log("ATENDIDO", v)
        self.actualizar()

    def retirar(self):
        """Se ejecuta al pulsar 'Retirar seleccionado': saca de la cola el vehículo elegido en la tabla."""
        sel = self.tabla.selection()               # Devuelve la fila seleccionada
        if not sel:
            return messagebox.showinfo("CDA", "Selecciona un vehículo de la tabla.")
        # item(...)["values"] son los datos de esa fila; el índice [1] es la placa.
        placa = str(self.tabla.item(sel[0])["values"][1])
        if messagebox.askyesno("Retirar", f"¿Retirar {placa} de la cola?"):
            v = self.cda.retirar(placa)
            if v:
                self.log("RETIRADO", v)
            self.actualizar()

    def al_seleccionar(self, _):
        """Al elegir una fila, dice cuántos vehículos hay por delante (posición - 1)."""
        sel = self.tabla.selection()
        if sel:
            pos = int(self.tabla.item(sel[0])["values"][0])
            self.delante.config(text=f"Por delante: {pos - 1} vehículo(s).", fg=INK)

    def actualizar(self):
        """Redibuja tabla, contadores y banner según el estado actual de la cola.
        Se llama después de cada cambio (registrar, atender, retirar)."""
        for fila in self.tabla.get_children():     # Borra todas las filas viejas
            self.tabla.delete(fila)
        # ordenados() ya viene en orden de atención: especiales primero.
        # enumerate(..., 1) da la posición 1, 2, 3...
        for i, v in enumerate(self.cda.ordenados(), 1):
            # tags=("esp",) pinta la fila rosada si es especial; () = sin estilo extra.
            self.tabla.insert("", "end", tags=("esp",) if v.es_especial else (),
                              values=(i, v.placa, v.tipo, v.marca, v.color,
                                      "ESPECIAL" if v.es_especial else "Normal"))
        self.n_pend.config(text=self.cda.pendientes())
        self.n_esp.config(text=len(self.cda.cola_especiales))
        self.n_nor.config(text=len(self.cda.cola_normales))
        s = self.cda.siguiente()
        if s is None:
            self.banner.config(text="No hay vehículos pendientes", bg="white", fg=GRIS)
        else:
            self.banner.config(text=f"SIGUIENTE: {s.placa} · {s.tipo}",
                               bg=ROJO if s.es_especial else AMARILLO,
                               fg="white" if s.es_especial else INK)
        self.delante.config(text="Selecciona un vehículo para ver cuántos hay por delante.", fg=GRIS)


if __name__ == "__main__":
    app = App()
    app.mainloop()
