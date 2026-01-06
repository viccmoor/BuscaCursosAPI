# BuscaCursosAPI

API hecha con FastAPI para [buscacursos.uc.cl](https://buscacursos.uc.cl) utilizando la librería de [**BCScraper**](https://pypi.org/project/bcscraper/).

## Características

- **Búsqueda de cursos** por *nombre* y *sigla*.

## REST API

### Buscar curso por nombre

```http
GET /api/cursos/cursos/?periodo=2026-1&nombre=Calculo+II
```

### Buscar curso por sigla

```http
GET /api/cursos/cursos/?periodo=2026-1&sigla=MAT1620
```

> [!IMPORTANT]
> Para probar la API de forma interactiva y explorar todos los endpoints disponibles, puedes acceder a la ruta **/docs**, que utiliza la interfaz Swagger proporcionada por FastAPI.
