import streamlit as st
from models.roles import Asistente, Gerente, JefeArea, PersonalTecnico
from utils.helpers import obtener_areas_disponibles

def render_nuevo_trabajador(repo):
    st.subheader("Registrar Nuevo Trabajador")
    st.markdown("Complete el siguiente formulario modular para ingresar un trabajador al sistema.")
    
    with st.form("form_nuevo_trabajador", clear_on_submit=False):
        st.write("### Datos Personales")
        nombre = st.text_input("Nombre completo")
        documento = st.text_input("Documento de identidad (DNI)")
        correo = st.text_input("Correo electrónico")
        telefono = st.text_input("Teléfono")
        
        st.write("### Datos Laborales")
        c1, c2 = st.columns(2)
        with c1:
            # We use a static list of areas according to the business logic mostly, but we can also use dynamic if needed.
            # Here we hardcode the ones that have jefatura to avoid issues, or use dynamic.
            area = st.selectbox("Área", ["Marketing", "Sistemas", "Producción", "Logística", "Finanzas", "Gerencia General"])
            rol = st.selectbox("Rol", ["Gerente", "Jefe de Área", "Asistente", "Personal Técnico"])
        with c2:
            anios_exp = st.number_input("Años de experiencia", min_value=-10, value=0)
            st.write("")
            st.write("")
            activo = st.checkbox("Trabajador activo", value=True)
            
        submit_btn = st.form_submit_button("Crear Trabajador")
        
    if submit_btn:
        errores = []
        
        # Validaciones
        if not nombre.strip():
            errores.append("El nombre completo no puede estar vacío.")
        
        if len(documento.strip()) != 8 or not documento.isdigit():
            errores.append("El documento de identidad debe tener exactamente 8 dígitos numéricos.")
            
        if anios_exp < 0:
            errores.append("Los años de experiencia deben ser mayor o igual que 0.")
            
        if not correo.strip() or "@" not in correo:
            errores.append("Debe ingresar un correo electrónico válido.")
            
        if errores:
            for error in errores:
                st.error(f"⚠️ {error}")
        else:
            # Si no hay errores, se procede a la creación modular del objeto
            puesto = rol
            
            # Asignación de rangos según el rol seleccionado
            if rol == "Asistente":
                rango = "Operativo"
            elif rol == "Personal Técnico":
                rango = "Especialista"
            elif rol == "Jefe de Área":
                rango = "Táctico"
            else:
                rango = "Estratégico"
                
            codigo_estado = "ACT" if activo else "TC"
            
            # Instanciación polimórfica
            if rol == "Gerente":
                nuevo = Gerente(nombre, documento, area, puesto, rango, correo, telefono, codigo_estado, activo=activo)
            elif rol == "Jefe de Área":
                nuevo = JefeArea(nombre, documento, area, puesto, rango, correo, telefono, codigo_estado, activo=activo)
            elif rol == "Asistente":
                nuevo = Asistente(nombre, documento, area, puesto, rango, correo, telefono, codigo_estado, activo=activo)
            else:
                nuevo = PersonalTecnico(nombre, documento, area, puesto, rango, correo, telefono, codigo_estado, anios_experiencia=anios_exp, activo=activo)
                
            repo.agregar_trabajador(nuevo)
            st.success(f"✅ ¡Trabajador '{nombre}' creado correctamente en el área de {area}!")
