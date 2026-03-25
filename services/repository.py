from __future__ import annotations

from collections import defaultdict
from typing import List, Optional

from models.roles import Asistente, Gerente, JefeArea, PersonalTecnico
from models.trabajador import Trabajador


class RepositorioTrabajadores:
    def __init__(self) -> None:
        self._trabajadores: List[Trabajador] = []

    def agregar_trabajador(self, trabajador: Trabajador) -> None:
        self._trabajadores.append(trabajador)

    def listar_trabajadores(self) -> List[Trabajador]:
        return self._trabajadores

    def listar_por_area(self, area: str) -> List[Trabajador]:
        return [t for t in self._trabajadores if t.get_area() == area]

    def buscar_por_nombre(self, nombre: str) -> Optional[Trabajador]:
        for trabajador in self._trabajadores:
            if trabajador.get_nombre_completo() == nombre:
                return trabajador
        return None

    def validar_reglas_de_negocio(self) -> list[dict]:
        gerentes = [t for t in self._trabajadores if isinstance(t, Gerente)]
        jefes = [t for t in self._trabajadores if isinstance(t, JefeArea)]
        asistentes_por_area = defaultdict(int)
        tecnicos_por_area = defaultdict(int)

        for trabajador in self._trabajadores:
            if isinstance(trabajador, Asistente):
                asistentes_por_area[trabajador.get_area()] += 1
            elif isinstance(trabajador, PersonalTecnico):
                tecnicos_por_area[trabajador.get_area()] += 1

        validaciones = [
            {
                "cumple": len(gerentes) >= 1,
                "mensaje": f"Existe al menos un gerente: {'sí' if len(gerentes) >= 1 else 'no'}."
            },
            {
                "cumple": len(jefes) >= 5,
                "mensaje": f"Existen al menos cinco jefes de área: {'sí' if len(jefes) >= 5 else 'no'}."
            },
        ]

        for area, total in asistentes_por_area.items():
            validaciones.append(
                {
                    "cumple": total <= 2,
                    "mensaje": f"Área {area}: asistentes = {total} (máximo 2)."
                }
            )

        for area, total in tecnicos_por_area.items():
            validaciones.append(
                {
                    "cumple": total <= 5,
                    "mensaje": f"Área {area}: técnicos = {total} (máximo 5)."
                }
            )

        return validaciones
