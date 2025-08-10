from fastapi import FastAPI
from contextlib import asynccontextmanager

from config.settings import settings
from config.database_manager import DatabaseManager
from starlette.middleware.cors import CORSMiddleware

from models.user import User  # Import your Beanie document models here

from repositories.user_repository import UserRepository

user_repository: UserRepository = UserRepository()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager to handle startup and shutdown events.
    """
    models = [User]  # Import your Beanie document models here
    try:
        await DatabaseManager.connect(
            settings.mongodb_uri, settings.database_name, models
        )
        print("Connected to MongoDB")
        # app.state.db_client = db_client
        # user_repository = UserRepository()  # Initialize the user repository
        yield

    # Here you can add any cleanup code if needed

    # add finally to close connections or cleanup resources
    finally:
        print("Shutting down application...")
        await DatabaseManager.close()
        print("Application shutdown complete")


app = FastAPI(
    title=settings.project_name,
    version=settings.project_version,
    description="API for Interactive Story Weaver",
    lifespan=lifespan,
)

# --- Add CORSMiddleware ---
# maybe later get it from settings
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello")
async def read_root():
    return {"message": "Welcome to the Interactive Story Weaver API!"}


@app.get("/users/fake_create")
async def create_user(
    username: str = "test", email: str = "user@test.te", password: str = "test"
):
    user = User(username=username, email=email, password_hash=password)
    await user_repository.create(user)
    return {"message": "User created!"}


@app.get("/users")
async def list_users():
    users = await user_repository.list()
    return users


@app.get("/users/by_email/{email}")
async def get_user(email: str = "user@test.te"):
    user = await user_repository.get_user_by_email(email)
    if user:
        return user
    return {"error": "User not found"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await user_repository.get_by_id(user_id)
    if user:
        return user
    return {"error": "User not found"}
