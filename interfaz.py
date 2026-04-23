"""
Interfaz gráfica del sistema (Tkinter)
FUNCIONALIDADES:
✔ Registrar clientes
✔ Crear reservas
✔ Confirmar reservas
✔ Cancelar reservas
✔ Mostrar datos en tabla
✔ Colores por estado
✔ Limpieza automática de campos
"""

# -----------------------------
# IMPORTACIONES
# -----------------------------
# Tkinter sirve para crear la interfaz gráfica (ventanas, botones, etc.)

import tkinter as tk

# messagebox permite mostrar mensajes (éxito, error)
# ttk permite usar componentes más avanzados como tablas (Treeview) y combos
from tkinter import messagebox, ttk

# Importamos nuestras clases del sistema (modelo)
from modelos.cliente import Cliente
from modelos.reserva import Reserva
from modelos.servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada

# Librería para manejar errores y guardarlos en un archivo
import logging

# -----------------------------
# TIPADO (SOLO PARA VS CODE)
# -----------------------------
# Esto NO afecta el programa, solo evita que VS Code muestre errores falsos
from typing import Any

# Variables de interfaz inicializadas en None (vacías)
# Luego se asignan dentro de la función iniciar_app()
entry_id: Any = None
entry_nombre: Any = None
entry_correo: Any = None
combo_clientes: Any = None
combo_servicios: Any = None
entry_horas: Any = None
tabla: Any = None


# -----------------------------
# CONFIGURACIÓN LOGS
# -----------------------------
logging.basicConfig(
    filename="logs.txt", # archivo donde se guardan errores
    level=logging.ERROR,# nivel de error
    format="%(asctime)s - %(levelname)s - %(message)s" # formato del mensaje
)

# -----------------------------
# DATOS EN MEMORIA
# -----------------------------
# Listas donde se almacenan los clientes y reservas
# (no se usa base de datos en este proyecto)
clientes = []
reservas = []

# -----------------------------
# VARIABLES GLOBALES UI
# -----------------------------
combo_clientes = None
tabla = None

# -----------------------------
# SERVICIOS DISPONIBLES
# -----------------------------
# Diccionario con los tipos de servicios que ofrece el sistema
# Cada servicio tiene su lógica de cálculo
servicios_disponibles = {
    "Reserva Sala": ReservaSala("Sala", 50000),
    "Alquiler Equipo": AlquilerEquipo("Laptop", 30000),
    "Asesoría": AsesoriaEspecializada("Consultoría", 80000)
}

# -----------------------------
# LIMPIAR CAMPOS
# -----------------------------
def limpiar_campos():
    """Limpia los campos de entrada después de registrar cliente"""
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)

# -----------------------------
# REGISTRAR CLIENTE
# -----------------------------
def registrar_cliente():
    global combo_clientes
    try:
        cliente = Cliente(
            entry_id.get(),
            entry_nombre.get(),
            entry_correo.get()
        )

        clientes.append(cliente)

        # Actualiza el ComboBox
        combo_clientes['values'] = [
            c.mostrar_info() for c in clientes
        ]

        limpiar_campos()

        messagebox.showinfo("Éxito", "Cliente registrado")

    except Exception as e:
        logging.error(str(e))
        messagebox.showerror("Error", str(e))


# -----------------------------
# CREAR RESERVA
# -----------------------------
def crear_reserva():
    global tabla
    try:
        # VALIDACIONES
        if combo_clientes.current() == -1:
            raise ValueError("Seleccione un cliente")

        if combo_servicios.get() == "":
            raise ValueError("Seleccione un servicio")

        if entry_horas.get() == "":
            raise ValueError("Ingrese las horas")

        cliente = clientes[combo_clientes.current()]
        servicio = servicios_disponibles[combo_servicios.get()]
        horas = float(entry_horas.get())

        reserva = Reserva(cliente, servicio, horas)
        reservas.append(reserva)

        actualizar_tabla()

        messagebox.showinfo("Éxito", "Reserva creada")

    except Exception as e:
        logging.error(str(e))
        messagebox.showerror("Error", str(e))


# -----------------------------
# CONFIRMAR RESERVA
# -----------------------------
def confirmar_reserva():
    seleccion = tabla.selection()

    if not seleccion:
        messagebox.showwarning("Atención", "Seleccione una reserva")
        return

    index = tabla.index(seleccion[0])
    reservas[index].confirmar()

    actualizar_tabla()


# -----------------------------
# CANCELAR RESERVA
# -----------------------------
def cancelar_reserva():
    seleccion = tabla.selection()

    if not seleccion:
        messagebox.showwarning("Atención", "Seleccione una reserva")
        return

    index = tabla.index(seleccion[0])
    reservas[index].cancelar()

    actualizar_tabla()


# -----------------------------
# ACTUALIZAR TABLA
# -----------------------------
def actualizar_tabla():
    """Refresca la tabla con los datos actuales"""
    
    for fila in tabla.get_children():
        tabla.delete(fila)

    for r in reservas:
        # COLOR SEGÚN ESTADO
        color = "green" if r.estado == "Confirmada" else "red"

        tabla.insert("", "end", values=(
            r.cliente.mostrar_info(),
            r.servicio.nombre,
            r.horas,
            r.estado,
            f"${r.procesar():,.0f}"
        ), tags=(color,))


# -----------------------------
# INTERFAZ PRINCIPAL
# -----------------------------
def iniciar_app():
    global entry_id, entry_nombre, entry_correo
    global combo_clientes, combo_servicios, entry_horas
    global tabla

    ventana = tk.Tk()
    ventana.title("Software FJ")
    ventana.geometry("700x550")

    # -------- CLIENTES --------
    tk.Label(ventana, text="ID").pack()
    entry_id = tk.Entry(ventana)
    entry_id.pack()

    tk.Label(ventana, text="Nombre").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Correo").pack()
    entry_correo = tk.Entry(ventana)
    entry_correo.pack()

    tk.Button(
        ventana,
        text="Registrar Cliente",
        command=registrar_cliente
    ).pack(pady=5)

    # -------- RESERVAS --------
    tk.Label(ventana, text="Cliente").pack()
    combo_clientes = ttk.Combobox(ventana)
    combo_clientes.pack()

    tk.Label(ventana, text="Servicio").pack()
    combo_servicios = ttk.Combobox(
        ventana,
        values=list(servicios_disponibles.keys())
    )
    combo_servicios.pack()

    tk.Label(ventana, text="Horas").pack()
    entry_horas = tk.Entry(ventana)
    entry_horas.pack()

    tk.Button(
        ventana,
        text="Crear Reserva",
        command=crear_reserva
    ).pack(pady=5)

    # -------- BOTONES EXTRA --------
    tk.Button(
        ventana,
        text="Confirmar Reserva",
        command=confirmar_reserva
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Cancelar Reserva",
        command=cancelar_reserva
    ).pack(pady=5)

    # -------- TABLA --------
    tabla = ttk.Treeview(
        ventana,
        columns=("Cliente", "Servicio", "Horas", "Estado", "Costo"),
        show="headings"
    )

    for col in ("Cliente", "Servicio", "Horas", "Estado", "Costo"):
        tabla.heading(col, text=col)
        tabla.column(col, width=160)  # Ajuste de tamaño

    # COLORES
    tabla.tag_configure("green", foreground="green")
    tabla.tag_configure("red", foreground="red")

    tabla.pack(pady=10)

    ventana.mainloop()