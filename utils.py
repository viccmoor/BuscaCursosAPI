"""Funciones útiles varias"""
from bcscraper import Curso
from models import CursoModel, ModuloModel


def curso_to_model(c: Curso) -> CursoModel:
    """Transforma un curso a su modelo Pydantic correspondiente."""
    return CursoModel(
        nrc=c.nrc,
        sigla=c.sigla,
        retirable=c.retirable,
        ingles=c.ingles,
        seccion=c.seccion,
        aprobacion_especial=c.aprobacion_especial,
        area=c.area,
        formato=c.formato,
        categoria=c.categoria,
        nombre=c.nombre,
        profesor=c.profesor,
        campus=c.campus,
        creditos=c.creditos,
        vacantes_totales=c.vacantes_totales,
        vacantes_disponibles=c.vacantes_disponibles,
        horario=[
            ModuloModel(tipo=m.tipo, dia=m.dia, modulo=m.modulo, sala=m.sala)
            for m in c.horario
        ]
    )
