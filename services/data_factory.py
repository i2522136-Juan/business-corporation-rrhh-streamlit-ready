from __future__ import annotations

from models.roles import Asistente, Gerente, JefeArea, PersonalTecnico
from services.repository import RepositorioTrabajadores

AREAS_CON_JEFATURA = ["Marketing", "Sistemas", "Producción", "Logística", "Finanzas"]

ESTADOS_TECNICOS = {
    "Marketing": ["ACT", "ACT", "TC", "ACT", "R"],
    "Sistemas": ["ACT", "ACT", "ACT", "D", "ACT"],
    "Producción": ["ACT", "ACT", "ACT", "ACT", "ACT"],
    "Logística": ["ACT", "TC", "ACT", "ACT", "ACT"],
    "Finanzas": ["ACT", "ACT", "R", "ACT", "ACT"],
}


def crear_datos_demo() -> RepositorioTrabajadores:
    repo = RepositorioTrabajadores()

    gerente = Gerente(
        nombre_completo="Patricia Elena Salazar Mendoza",
        documento="46851234",
        area="Gerencia General",
        puesto="Gerente General",
        rango="Estratégico",
        correo="patricia.salazar@businesscorp.pe",
        telefono="+51 999 100 100",
    )
    repo.agregar_trabajador(gerente)

    for indice, area in enumerate(AREAS_CON_JEFATURA, start=1):
        jefe = JefeArea(
            nombre_completo=f"Jefe {area} {indice}",
            documento=f"70000{indice:03d}",
            area=area,
            puesto="Jefe de Área",
            rango="Táctico",
            correo=f"jefe.{area.lower()}@businesscorp.pe".replace("ó", "o"),
            telefono=f"+51 999 200 {100 + indice}",
            jefe_inmediato=gerente,
        )
        repo.agregar_trabajador(jefe)

        for nro_asistente in range(1, 3):
            codigo_estado = "ACT" if nro_asistente == 1 else "TC"
            asistente = Asistente(
                nombre_completo=f"Asistente {area} {nro_asistente}",
                documento=f"710{indice:02d}{nro_asistente:02d}",
                area=area,
                puesto="Asistente",
                rango="Operativo",
                correo=f"asistente{nro_asistente}.{area.lower()}@businesscorp.pe".replace("ó", "o"),
                telefono=f"+51 999 300 {indice}{nro_asistente}",
                codigo_estado=codigo_estado,
                jefe_inmediato=jefe,
                activo=codigo_estado == "ACT",
            )
            repo.agregar_trabajador(asistente)

        for nro_tecnico in range(1, 6):
            codigo_estado = ESTADOS_TECNICOS[area][nro_tecnico - 1]
            tecnico = PersonalTecnico(
                nombre_completo=f"Técnico {area} {nro_tecnico}",
                documento=f"720{indice:02d}{nro_tecnico:02d}",
                area=area,
                puesto="Personal Técnico",
                rango="Especialista",
                correo=f"tecnico{nro_tecnico}.{area.lower()}@businesscorp.pe".replace("ó", "o"),
                telefono=f"+51 999 400 {indice}{nro_tecnico}",
                codigo_estado=codigo_estado,
                jefe_inmediato=jefe,
                anios_experiencia=2 + nro_tecnico,
                activo=codigo_estado == "ACT",
            )
            repo.agregar_trabajador(tecnico)

    return repo
