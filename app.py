from __future__ import annotations

import pandas as pd
import streamlit as st

from services.data_factory import crear_datos_demo
from services.reporting import construir_ficha_trabajador, construir_tabla_trabajadores, obtener_indicadores
from utils.helpers import decisiones_diseno, obtener_areas_disponibles

st.set_page_config(page_title="Business Corporation | RR. HH.", page_icon="🏢", layout="wide")


def mostrar_tabla(df: pd.DataFrame) -> None:
    st.dataframe(df, use_container_width=True, hide_index=True)


repo = crear_datos_demo()
trabajadores = repo.listar_trabajadores()
areas = obtener_areas_disponibles(trabajadores)

st.title("🏢 Sistema de Recursos Humanos - Business Corporation")
st.caption("Proyecto modular en Python + Streamlit preparado para ejecutarse correctamente en Streamlit Cloud.")

with st.sidebar:
    st.header("Menú")
    vista = st.radio(
        "Seleccione una opción",
        [
            "Resumen general",
            "Listado completo",
            "Consulta por área",
            "Ficha de trabajador",
            "Validación de reglas",
            "Explicación técnica",
        ],
    )

if vista == "Resumen general":
    indicadores = obtener_indicadores(trabajadores)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total trabajadores", indicadores["total_trabajadores"])
    c2.metric("Gerentes", indicadores["gerentes"])
    c3.metric("Jefes de área", indicadores["jefes_area"])
    c4.metric("Áreas", indicadores["areas"])

    c5, c6, c7 = st.columns(3)
    c5.metric("Asistentes", indicadores["asistentes"])
    c6.metric("Técnicos", indicadores["tecnicos"])
    c7.metric("No activos", indicadores["inactivos"])

    st.subheader("Decisiones de diseño")
    for item in decisiones_diseno():
        st.write(f"• {item}")

    st.subheader("Vista previa")
    mostrar_tabla(construir_tabla_trabajadores(trabajadores).head(10))

elif vista == "Listado completo":
    st.subheader("Listado general de trabajadores")
    mostrar_tabla(construir_tabla_trabajadores(trabajadores))

elif vista == "Consulta por área":
    st.subheader("Trabajadores por área")
    area = st.selectbox("Área", areas)
    mostrar_tabla(construir_tabla_trabajadores(repo.listar_por_area(area)))

elif vista == "Ficha de trabajador":
    st.subheader("Consulta individual")
    nombre = st.selectbox("Trabajador", [t.get_nombre_completo() for t in trabajadores])
    trabajador = repo.buscar_por_nombre(nombre)
    if trabajador is not None:
        ficha = construir_ficha_trabajador(trabajador)
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Nombre:** {ficha['Nombre completo']}")
            st.write(f"**Documento:** {ficha['Documento']}")
            st.write(f"**Área:** {ficha['Área']}")
            st.write(f"**Puesto:** {ficha['Puesto']}")
            st.write(f"**Rango:** {ficha['Rango']}")
            st.write(f"**Resumen:** {ficha['Resumen']}")
        with col2:
            st.write(f"**Jefe inmediato:** {ficha['Jefe inmediato']}")
            st.write(f"**Estado:** {ficha['Estado']}")
            st.write(f"**Correo:** {ficha['Correo']}")
            st.write(f"**Teléfono:** {ficha['Teléfono']}")
            st.write(f"**Experiencia (años):** {ficha['Experiencia (años)']}")
            st.write(f"**Activo:** {'Sí' if ficha['Activo'] else 'No'}")

elif vista == "Validación de reglas":
    st.subheader("Validación del negocio")
    for validacion in repo.validar_reglas_de_negocio():
        if validacion["cumple"]:
            st.success(validacion["mensaje"])
        else:
            st.error(validacion["mensaje"])

    st.subheader("Control por área")
    tabla = construir_tabla_trabajadores(trabajadores)
    resumen = (
        tabla.groupby("Área")[["Es asistente", "Es técnico"]]
        .sum()
        .rename(columns={"Es asistente": "Asistentes", "Es técnico": "Técnicos"})
        .reset_index()
    )
    mostrar_tabla(resumen)

else:
    st.subheader("Explicación técnica")
    st.write("• POO con clase abstracta Trabajador y clases derivadas por rol.")
    st.write("• Getters y setters para encapsulamiento y mantenimiento.")
    st.write("• Polimorfismo en get_resumen().")
    st.write("• Reglas del negocio validadas desde un repositorio de objetos.")
    st.write("• Interfaz con Streamlit usando componentes nativos y tablas de Pandas.")
    st.write("• Dependencias mínimas para que el despliegue en Streamlit Cloud sea estable.")
    st.warning(
        "El enunciado menciona cuatro áreas específicas, pero exige cinco jefes de área. "
        "Por ello se añadió Finanzas como quinta jefatura."
    )
