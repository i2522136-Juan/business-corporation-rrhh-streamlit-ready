# -*- coding: utf-8 -*-
from __future__ import annotations

import streamlit as st

from services.data_factory import crear_datos_demo
from utils.helpers import obtener_areas_disponibles

# Importar las vistas modulares
from views.dashboard import render_dashboard
from views.listado import render_listado_completo, render_consulta_area
from views.ficha import render_ficha
from views.reglas import render_reglas, render_tecnica
from views.nuevo_trabajador import render_nuevo_trabajador

st.set_page_config(page_title="Business Corporation | RR. HH.", page_icon="🏢", layout="wide")

# Inicializar o recuperar el repositorio del estado de sesión
if "repo" not in st.session_state:
    st.session_state.repo = crear_datos_demo()

repo = st.session_state.repo
trabajadores = repo.listar_trabajadores()

st.title("🏢 Sistema de Recursos Humanos - Business Corporation")
st.caption("Proyecto modular en Python + Streamlit preparado para ejecutarse correctamente en Streamlit Cloud.")

with st.sidebar:
    st.header("Menú")
    vista = st.radio(
        "Seleccione una opción",
        [
            "Resumen general",
            "Nuevo trabajador",
            "Listado completo",
            "Consulta por área",
            "Ficha de trabajador",
            "Validación de reglas",
            "Explicación técnica",
        ],
    )

if vista == "Resumen general":
    render_dashboard(trabajadores)

elif vista == "Nuevo trabajador":
    render_nuevo_trabajador(repo)
    # Refrescar la lista en cache si se agrega
    st.session_state.repo = repo 

elif vista == "Listado completo":
    render_listado_completo(trabajadores)

elif vista == "Consulta por área":
    render_consulta_area(repo, trabajadores)

elif vista == "Ficha de trabajador":
    render_ficha(repo, trabajadores)

elif vista == "Validación de reglas":
    render_reglas(repo, trabajadores)

else:
    render_tecnica()
