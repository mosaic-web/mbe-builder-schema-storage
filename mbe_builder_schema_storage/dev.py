import uvicorn


def start():
    """Launched with `poetry run dev` at root level"""
    uvicorn.run(
        "mbe_builder_schema_storage.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
