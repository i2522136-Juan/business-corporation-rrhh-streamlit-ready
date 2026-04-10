import streamlit as st
from services.reporting import obtener_indicadores, construir_tabla_trabajadores
from utils.helpers import decisiones_diseno
from views import mostrar_tabla

def render_dashboard(trabajadores):
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
