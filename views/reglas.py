import streamlit as st
from services.reporting import construir_tabla_trabajadores
from views import mostrar_tabla

def render_reglas(repo, trabajadores):
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

def render_tecnica():
    st.subheader("Explicación técnica")
    st.write("• POO con clase abstracta Trabajador y clases derivadas por rol.")
    st.write("• Getters y setters para encapsulamiento y mantenimiento.")
    st.write("• Polimorfismo en get_resumen().")
    st.write("• Reglas del negocio validadas desde un repositorio de objetos.")
    st.write("• Interfaz con Streamlit modular usando componentes nativos y tablas de Pandas.")
    st.write("• Dependencias mínimas para que el despliegue en Streamlit Cloud sea estable.")
    st.warning(
        "El enunciado menciona cuatro áreas específicas, pero exige cinco jefes de área. "
        "Por ello se añadió Finanzas como quinta jefatura."
    )
