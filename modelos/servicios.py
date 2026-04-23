"""
Servicios especializados.

Conceptos:
- Herencia
- Polimorfismo
"""

from modelos.servicio import Servicio

class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        return self.tarifa * horas


class AlquilerEquipo(Servicio):
    def calcular_costo(self, horas):
        return self.tarifa * horas * 1.1


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas):
        return self.tarifa * horas * 1.25