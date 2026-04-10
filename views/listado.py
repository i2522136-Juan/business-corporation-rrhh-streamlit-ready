import streamlit as st
from services.reporting import construir_tabla_trabajadores
from utils.helpers import obtener_areas_disponibles
from views import mostrar_tabla

def render_listado_completo(trabajadores):
    st.subheader("Listado general de trabajadores")
    mostrar_tabla(construir_tabla_trabajadores(trabajadores))

def render_consulta_area(repo, trabajadores):
    st.subheader("Trabajadores por área")
    areas = obtener_areas_disponibles(trabajadores)
    area = st.selectbox("Área", areas)
    mostrar_tabla(construir_tabla_trabajadores(repo.listar_por_area(area)))
