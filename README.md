# Caso práctico N.º 01 - Business Corporation (versión Streamlit lista para despliegue)

## Objetivo
Este proyecto resuelve el caso práctico de Business Corporation con una solución modular en Python. La lógica del negocio está construida con Programación Orientada a Objetos y la interfaz se presenta con Streamlit.

## Qué incluye
- 1 gerente general.
- 5 jefes de área.
- 2 asistentes por área.
- 5 técnicos por área.
- Getters y setters.
- Métodos obligatorios: `get_resumen()`, `get_jefe_inmediato()` y `get_estado()`.
- Interfaz Streamlit lista para GitHub y Streamlit Community Cloud.
- Informe en Word.
- Explicación de archivos.

## Estructura
```text
business_corporation_rrhh_streamlit_ready/
├── app.py
├── requirements.txt
├── requirements-dev.txt
├── generate_report.py
├── pyproject.toml
├── .streamlit/
│   └── config.toml
├── models/
├── services/
├── utils/
├── tests/
├── scripts/
└── docs/
```

## Instalación local
```bash
python scripts/setup_env.py
```

## Ejecución local
```bash
.venv/bin/streamlit run app.py
```

## Pruebas
```bash
.venv/bin/pytest -q
```

## Generar nuevamente el informe Word
```bash
.venv/bin/python generate_report.py
```

## Importante para Streamlit Cloud
El archivo `requirements.txt` contiene solo dependencias de ejecución. Eso evita despliegues lentos o fallidos.

## Repositorio
https://github.com/i2522136-Juan/business-corporation-rrhh-streamlit-ready

## Observación
El enunciado lista cuatro áreas específicas, pero pide cinco jefes de área. Para cumplir el mínimo exigido, se añadió el área de Finanzas.
