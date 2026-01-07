# BuscaCursosAPI

API hecha con FastAPI para [buscacursos.uc.cl](https://buscacursos.uc.cl) utilizando la librería de [**BCScraper**](https://pypi.org/project/bcscraper/).

## Características

- **Búsqueda de cursos** por *sigla*, *NRC*, *nombre* y *profesor*.

## REST API

### Buscar curso

```http
GET /api/cursos/cursos/?periodo=2026-1&sigla=MAT1610&nrc=12345&nombre=Calculo+I&profesor=Nombre+Apellido
```

**Parámetros**

| Nombre | Descripción |
|--------|-------------|
| `periodo` | Período académico del curso (ej: 2026-1) |
| `sigla` | Código que identifica al curso (ej: MAT1610) |
| `nrc` | Número de referencia del curso (ej: 12345) |
| `nombre` | Nombre del curso (ej: Cálculo I) |
| `profesor` | Nombre del profesor (ej: Nombre Apellido) |
| `proxy_url` | Servidor intermedio o un mirror de BuscaCursos (recomendado) |

El parámetro `periodo` es obligatorio y debe acompañarse de al menos uno de los parámetros.

> [!IMPORTANT]
> Para probar la API de forma interactiva y explorar todos los endpoints disponibles, puedes acceder a la ruta **/docs**, que utiliza la interfaz Swagger proporcionada por FastAPI.
