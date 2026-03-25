from __future__ import annotations

from models.trabajador import Trabajador


class Gerente(Trabajador):
    def get_resumen(self) -> str:
        return f"{self.get_puesto()} | Rango: {self.get_rango()}"


class JefeArea(Trabajador):
    def get_resumen(self) -> str:
        return f"{self.get_puesto()} del área de {self.get_area()} | Rango: {self.get_rango()}"


class Asistente(Trabajador):
    def get_resumen(self) -> str:
        return f"{self.get_puesto()} del área de {self.get_area()} | Rango: {self.get_rango()}"


class PersonalTecnico(Trabajador):
    def get_resumen(self) -> str:
        return (
            f"{self.get_puesto()} del área de {self.get_area()} | Rango: {self.get_rango()} | "
            f"Experiencia: {self.get_anios_experiencia()} años"
        )
