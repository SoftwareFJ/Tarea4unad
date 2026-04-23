"""
Clase Reserva.

Responsabilidad:
- Representa una reserva realizada por un cliente.

Conceptos aplicados:
- Asociación (Cliente + Servicio)
- Encapsulación
- Manejo de estados
- Validación de datos
"""

class Reserva:
    def __init__(self, cliente, servicio, horas, fecha):
        """
        Constructor de la clase Reserva.

        Parámetros:
        - cliente: objeto Cliente
        - servicio: objeto Servicio
        - horas: cantidad de horas reservadas
        - fecha: fecha de la reserva (string)
        """

        # Validación de horas
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")

        # Validación de fecha (simple)
        if not fecha.strip():
            raise ValueError("La fecha no puede estar vacía")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.fecha = fecha

        # Estado inicial
        self.estado = "Pendiente"

    def confirmar(self):
        """Cambia el estado de la reserva a Confirmada"""
        self.estado = "Confirmada"

    def cancelar(self):
        """Cambia el estado de la reserva a Cancelada"""
        self.estado = "Cancelada"

    def procesar(self):
        """
        Calcula el costo de la reserva.

        Si está cancelada, el costo es 0.
        """
        if self.estado == "Cancelada":
            return 0

        return self.servicio.calcular_costo(self.horas)