from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Trabajador(ABC):
    def __init__(
        self,
        nombre_completo: str,
        documento: str,
        area: str,
        puesto: str,
        rango: str,
        correo: str,
        telefono: str,
        codigo_estado: str = "ACT",
        jefe_inmediato: Optional["Trabajador"] = None,
        anios_experiencia: int = 0,
        activo: bool = True,
    ) -> None:
        self._nombre_completo = nombre_completo
        self._documento = documento
        self._area = area
        self._puesto = puesto
        self._rango = rango
        self._correo = correo
        self._telefono = telefono
        self._codigo_estado = codigo_estado
        self._jefe_inmediato = jefe_inmediato
        self._anios_experiencia = anios_experiencia
        self._activo = activo

    def get_nombre_completo(self) -> str:
        return self._nombre_completo

    def get_documento(self) -> str:
        return self._documento

    def get_area(self) -> str:
        return self._area

    def get_puesto(self) -> str:
        return self._puesto

    def get_rango(self) -> str:
        return self._rango

    def get_correo(self) -> str:
        return self._correo

    def get_telefono(self) -> str:
        return self._telefono

    def get_codigo_estado(self) -> str:
        return self._codigo_estado

    def get_anios_experiencia(self) -> int:
        return self._anios_experiencia

    def get_activo(self) -> bool:
        return self._activo

    def set_nombre_completo(self, valor: str) -> None:
        self._nombre_completo = valor

    def set_documento(self, valor: str) -> None:
        self._documento = valor

    def set_area(self, valor: str) -> None:
        self._area = valor

    def set_puesto(self, valor: str) -> None:
        self._puesto = valor

    def set_rango(self, valor: str) -> None:
        self._rango = valor

    def set_correo(self, valor: str) -> None:
        self._correo = valor

    def set_telefono(self, valor: str) -> None:
        self._telefono = valor

    def set_codigo_estado(self, valor: str) -> None:
        self._codigo_estado = valor

    def set_jefe_inmediato(self, valor: Optional["Trabajador"]) -> None:
        self._jefe_inmediato = valor

    def set_anios_experiencia(self, valor: int) -> None:
        self._anios_experiencia = valor

    def set_activo(self, valor: bool) -> None:
        self._activo = valor

    def get_jefe_inmediato(self) -> str:
        if self._jefe_inmediato is None:
            return "No tiene jefe inmediato"
        return f"{self._jefe_inmediato.get_nombre_completo()} ({self._jefe_inmediato.get_puesto()})"

    def get_estado(self) -> str:
        match self._codigo_estado:
            case "ACT":
                return "Activo"
            case "TC":
                return "Término de contrato (TC)"
            case "D":
                return "Despido (D)"
            case "R":
                return "Renuncia (R)"
            case _:
                return "Estado no definido"

    @abstractmethod
    def get_resumen(self) -> str:
        raise NotImplementedError
