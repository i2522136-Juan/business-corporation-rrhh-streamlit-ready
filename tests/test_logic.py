from services.data_factory import crear_datos_demo


def test_total_esperado_de_trabajadores() -> None:
    repo = crear_datos_demo()
    assert len(repo.listar_trabajadores()) == 41


def test_reglas_de_negocio_cumplen() -> None:
    repo = crear_datos_demo()
    validaciones = repo.validar_reglas_de_negocio()
    assert all(item["cumple"] for item in validaciones)


def test_gerente_sin_jefe_y_tecnico_con_experiencia() -> None:
    repo = crear_datos_demo()
    gerente = next(t for t in repo.listar_trabajadores() if t.get_puesto() == "Gerente General")
    tecnico = next(t for t in repo.listar_trabajadores() if t.get_puesto() == "Personal Técnico")
    assert gerente.get_jefe_inmediato() == "No tiene jefe inmediato"
    assert "Experiencia" in tecnico.get_resumen()
