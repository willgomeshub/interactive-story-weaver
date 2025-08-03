from fastapi import FastAPI
from contextlib import asynccontextmanager

from config.settings import settings
from repositories.base_repository import connect_to_mongodb, close_mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager to handle startup and shutdown events.
    """
    db_client = None
    try:
        db_client = await connect_to_mongodb()
        print("Connected to MongoDB")
        app.state.db_client = db_client
        yield

    # Here you can add any cleanup code if needed

    # add finally to close connections or cleanup resources
    finally:
        print("Shutting down application...")
        if hasattr(app.state, "db_client") and app.state.db_client:
            await close_mongodb(app.state.db_client)

        print("Application shutdown complete")


app = FastAPI(
    title=settings.project_name,
    version=settings.project_version,
    description="API for Interactive Story Weaver",
    lifespan=lifespan,
)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Interactive Story Weaver API!"}
