# SEO Content API

API REST para generar contenido SEO utilizando Inteligencia Artificial con FastAPI y Azure OpenAI.

## Estructura del Proyecto

```
seo-content-api/
├── app/
│   ├── main.py              # Aplicación FastAPI y configuración de routers
│   ├── config.py            # Gestión de configuración y variables de entorno
│   ├── models/              # Modelos Pydantic para Request y Response
│   ├── services/            # Lógica de negocio e integración con OpenAI
│   └── routers/             # Endpoints de la API
├── .env                     # Variables de entorno (Claves de API, etc.)
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación
```

## Requisitos

- Python 3.12 o superior
- Cuenta de Azure OpenAI con un modelo desplegado (recomendado: gpt-4o o gpt-4o-mini)

## Instalación

1.  Crear un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

2.  Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3.  Configurar variables de entorno:
    Renombra o crea un archivo `.env` en la raíz con el siguiente contenido:
    ```env
    AZURE_OPENAI_API_KEY=tu_clave_api
    AZURE_OPENAI_ENDPOINT=https://tu-endpoint.openai.azure.com/
    OPENAI_API_VERSION=2024-08-01-preview
    AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini
    ```

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
uvicorn app.main:app --reload
```

La documentación interactiva (Swagger UI) estará disponible en: `http://127.0.0.1:8000/docs`

## Endpoints

-   `POST /api/keywords/generate`: Generación de keywords y clasificación de intención.
-   `POST /api/articles/generate`: Creación de artículos estructurados (H1, H2, H3).
-   `POST /api/metadata/generate`: Generación de Meta Titles y Meta Descriptions.
-   `POST /api/faqs/extract`: Extracción de preguntas frecuentes y esquema JSON-LD.
-   `POST /api/social/summaries`: Generación de contenido para redes sociales.
