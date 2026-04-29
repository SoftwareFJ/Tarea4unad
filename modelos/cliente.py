"""
Clase Cliente.

Conceptos:
- Herencia
- Encapsulación
- Validación de datos
"""

from modelos.entidad import Entidad

class Cliente(Entidad):
    def __init__(self, id_cliente, nombre, correo):
        super().__init__(id_cliente)

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def mostrar_info(self):
         return f"[{self._id}] {self.__nombre} - {self.__correo}" # se agrega ID para que en la visual se pueda ver