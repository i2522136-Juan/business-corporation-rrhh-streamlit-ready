from __future__ import annotations

from models.roles import Gerente
from models.trabajador import Trabajador


def obtener_areas_disponibles(trabajadores: list[Trabajador]) -> list[str]:
    return sorted({t.get_area() for t in trabajadores if not isinstance(t, Gerente)})


def decisiones_diseno() -> list[str]:
    return [
        "Se usa una lista de objetos en Python como equivalente del array de objetos solicitado.",
        "La solución separa modelos, servicios, utilidades, pruebas y documentación para facilitar mantenimiento.",
        "Se mantiene Streamlit solo como interfaz; la lógica del negocio está fuera de la capa visual.",
        "Se añadió Finanzas como quinta jefatura para resolver la contradicción del enunciado.",
        "El archivo requirements.txt contiene solo dependencias de ejecución para evitar fallos en Streamlit Cloud.",
    ]
