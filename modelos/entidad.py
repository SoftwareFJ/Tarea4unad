"""
Clase abstracta base del sistema.

Conceptos:
- Abstracción
- Herencia

Todas las clases deben implementar mostrar_info()
"""

from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, id):
        self._id = id  # atributo protegido

    @abstractmethod
    def mostrar_info(self):
        pass