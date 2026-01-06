"""Módulo principal para el funcionamiento de la API"""
from typing import Optional

from fastapi import FastAPI, HTTPException
from bcscraper import buscar_curso

from models import CursosResponse
from utils import curso_to_model

app = FastAPI()


@app.get("/api/cursos/", response_model=CursosResponse)
def get_curso(
    periodo: str,
    sigla: Optional[str] = "",
    nrc: Optional[str] = "",
    nombre: Optional[str] = "",
    profesor: Optional[str] = "",
) -> CursosResponse:
    """Obtiene información de cursos según el período y nombre o sigla."""
    if not any((sigla, nrc, nombre, profesor)):
        raise HTTPException(
            status_code=400,
            detail=(
                "Debes proporcionar al menos uno de los parámetros: "
                "'nombre', 'sigla', 'nrc' o 'profesor'."
            )
        )

    try:
        curso = buscar_curso(periodo, sigla, nrc, nombre, profesor)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al buscar cursos: {str(e)}"
        ) from e

    if not curso:
        raise HTTPException(
            status_code=404,
            detail=(
                "No se encontraron cursos que coincidan con los "
                "parámetros proporcionados."
            )
        )

    curso_model = [curso_to_model(c) for c in curso]
    return {
        "data": {
            "curso": curso_model
        },
        "meta": {
            "periodo": periodo,
            "filtro": {
                "sigla": sigla,
                "nrc": nrc,
                "nombre": nombre,
                "profesor": profesor,
            },
            "cursos_encontrados": len(curso_model),
        }
    }
