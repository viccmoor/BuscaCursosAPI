"""Módulo principal para el funcionamiento de la API"""
from typing import Optional

from fastapi import FastAPI, HTTPException
from bcscraper import buscar_curso, buscar_sigla

from models import CursosResponse
from utils import curso_to_model

app = FastAPI()


@app.get("/api/cursos/", response_model=CursosResponse)
def get_curso(
    periodo: str,
    nombre: Optional[str] = None,
    sigla: Optional[str] = None
) -> CursosResponse:
    """Obtiene información de cursos según el período y nombre o sigla."""
    if (
        (nombre is None and sigla is None) or
        (nombre is not None and sigla is not None)
    ):
        raise HTTPException(
            status_code=400,
            detail=(
                "Debes proporcionar exactamente uno de los parámetros: "
                "'nombre' o 'sigla'."
            )
        )

    try:
        if nombre:
            cursos = buscar_curso(periodo, nombre)
        else:
            cursos = buscar_sigla(periodo, sigla)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al buscar cursos: {str(e)}"
        ) from e

    if not cursos:
        raise HTTPException(
            status_code=404,
            detail=(
                "No se encontraron cursos que coincidan con los "
                "parámetros proporcionados."
            )
        )

    curso_model = [curso_to_model(c) for c in cursos]
    return {
        "data": {
            "curso": curso_model
        },
        "meta": {
            "periodo": periodo,
            "filtro": {
                "nombre": nombre,
                "sigla": sigla,
            },
            "cursos_encontrados": len(curso_model),
        }
    }
