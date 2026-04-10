import streamlit as st
from services.reporting import construir_ficha_trabajador

def render_ficha(repo, trabajadores):
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
