"""Modelos de datos"""
from typing import List

from pydantic import BaseModel


class ModuloModel(BaseModel):
    """Modelo para representar un módulo de horario"""
    tipo: str
    dia: str
    modulo: int
    sala: str


class CursoModel(BaseModel):
    """Modelo para representar un curso"""
    nrc: str
    sigla: str
    retirable: bool
    ingles: bool
    seccion: int
    aprobacion_especial: bool
    area: str
    formato: str
    categoria: str
    nombre: str
    profesor: List[str]
    campus: str
    creditos: int
    vacantes_totales: int
    vacantes_disponibles: int
    horario: List[ModuloModel]
