from __future__ import annotations

import pandas as pd

from models.roles import Asistente, Gerente, JefeArea, PersonalTecnico
from models.trabajador import Trabajador


def construir_tabla_trabajadores(trabajadores: list[Trabajador]) -> pd.DataFrame:
    filas = []
    for trabajador in trabajadores:
        filas.append(
            {
                "Nombre completo": trabajador.get_nombre_completo(),
                "Documento": trabajador.get_documento(),
                "Área": trabajador.get_area(),
                "Puesto": trabajador.get_puesto(),
                "Rango": trabajador.get_rango(),
                "Resumen": trabajador.get_resumen(),
                "Jefe inmediato": trabajador.get_jefe_inmediato(),
                "Estado": trabajador.get_estado(),
                "Correo": trabajador.get_correo(),
                "Teléfono": trabajador.get_telefono(),
                "Experiencia (años)": trabajador.get_anios_experiencia(),
                "Activo": "Sí" if trabajador.get_activo() else "No",
                "Es asistente": 1 if isinstance(trabajador, Asistente) else 0,
                "Es técnico": 1 if isinstance(trabajador, PersonalTecnico) else 0,
                "Es jefe": 1 if isinstance(trabajador, JefeArea) else 0,
                "Es gerente": 1 if isinstance(trabajador, Gerente) else 0,
            }
        )
    return pd.DataFrame(filas)


def obtener_indicadores(trabajadores: list[Trabajador]) -> dict:
    tabla = construir_tabla_trabajadores(trabajadores)
    return {
        "total_trabajadores": len(tabla),
        "gerentes": int(tabla["Es gerente"].sum()),
        "jefes_area": int(tabla["Es jefe"].sum()),
        "asistentes": int(tabla["Es asistente"].sum()),
        "tecnicos": int(tabla["Es técnico"].sum()),
        "areas": int(tabla["Área"].nunique()),
        "inactivos": int((tabla["Activo"] == "No").sum()),
    }


def construir_ficha_trabajador(trabajador: Trabajador) -> dict:
    return {
        "Nombre completo": trabajador.get_nombre_completo(),
        "Documento": trabajador.get_documento(),
        "Área": trabajador.get_area(),
        "Puesto": trabajador.get_puesto(),
        "Rango": trabajador.get_rango(),
        "Resumen": trabajador.get_resumen(),
        "Jefe inmediato": trabajador.get_jefe_inmediato(),
        "Estado": trabajador.get_estado(),
        "Correo": trabajador.get_correo(),
        "Teléfono": trabajador.get_telefono(),
        "Experiencia (años)": trabajador.get_anios_experiencia(),
        "Activo": trabajador.get_activo(),
    }
