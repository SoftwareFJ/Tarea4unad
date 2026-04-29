"""
Clase Cliente.

Representa un cliente del sistema.

Hereda de Entidad, por lo que tiene un ID único.
Aplica encapsulación (atributos privados) y validaciones.
"""

from modelos.entidad import Entidad


class Cliente(Entidad):
    def __init__(self, id_cliente, nombre, correo):
        """
        Constructor de la clase Cliente.

        Parámetros:
        - id_cliente: identificador único del cliente
        - nombre: nombre del cliente
        - correo: correo electrónico
        """

        # Llamamos al constructor de la clase padre (Entidad)
        super().__init__(id_cliente)

        # -----------------------------
        # VALIDACIONES
        # -----------------------------

        # Validar que el nombre no esté vacío
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        # Validar que el correo tenga formato básico
        if "@" not in correo:
            raise ValueError("Correo inválido")

        # -----------------------------
        # ATRIBUTOS PRIVADOS
        # -----------------------------
        self.__nombre = nombre
        self.__correo = correo

    # -----------------------------
    # MÉTODOS GET (ACCESO CONTROLADO)
    # -----------------------------
    def get_nombre(self):
        """Retorna el nombre del cliente"""
        return self.__nombre

    def get_correo(self):
        """Retorna el correo del cliente"""
        return self.__correo

    # -----------------------------
    # MÉTODO PARA MOSTRAR INFORMACIÓN
    # -----------------------------
    def mostrar_info(self):
        """
        Retorna la información del cliente en formato texto.

        Se usa en la interfaz (ComboBox y tabla).
        """
        return f"[{self._id}] {self.__nombre} - {self.__correo}"