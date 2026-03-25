# Explicación de archivos del proyecto

## app.py
Archivo principal de la aplicación. Presenta el dashboard, los listados, la consulta por área y la ficha individual del trabajador.

## models/trabajador.py
Clase abstracta base con atributos comunes, getters, setters, `get_jefe_inmediato()` y `get_estado()`.

## models/roles.py
Subclases `Gerente`, `JefeArea`, `Asistente` y `PersonalTecnico`. Aquí se aplica polimorfismo con `get_resumen()`.

## services/repository.py
Gestiona la lista de objetos trabajador y valida las reglas del negocio.

## services/data_factory.py
Carga los datos iniciales requeridos por la consigna y arma toda la jerarquía organizacional.

## services/reporting.py
Convierte los objetos a DataFrames para mostrarlos de forma clara en Streamlit.

## utils/constants.py
Constantes reutilizables del sistema.

## utils/helpers.py
Funciones auxiliares de apoyo para vistas y decisiones de diseño.

## tests/test_logic.py
Pruebas básicas que verifican cantidad de trabajadores, cumplimiento de reglas y métodos clave.

## scripts/setup_env.py
Script en Python para crear el entorno virtual e instalar dependencias.

## requirements.txt
Dependencias mínimas de ejecución para que la app despliegue correctamente en Streamlit Cloud.

## requirements-dev.txt
Dependencias de desarrollo, usadas para pruebas y para regenerar el informe en Word.

## generate_report.py
Script que regenera el informe técnico en formato Word.

## docs/flujograma_pseudocodigo.txt
Descripción en pseudocódigo del flujo funcional del sistema.

## docs/informe_tecnico.docx
Informe formal listo para presentar o adjuntar en la entrega.
