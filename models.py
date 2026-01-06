"""Modelos de datos"""
from typing import List, Dict, Optional

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


class CursosData(BaseModel):
    """Modelo para representar los datos de un curso."""
    curso: List[CursoModel]


class CursosMeta(BaseModel):
    """
    Modelo para representar los metadatos de la respuesta de la
    búsqueda de un curso.
    """
    periodo: str
    filtro: Dict[str, Optional[str]]
    cursos_encontrados: int


class CursosResponse(BaseModel):
    """
    Modelo para representar la respuesta completa de la búsqueda de
    un curso.
    """
    data: CursosData
    meta: CursosMeta
