from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config.settings import settings


async def connect_to_mongodb():
    client = AsyncIOMotorClient(settings.mongodb_uri)
    await init_beanie(
        database=client.get_default_database(),
        document_models=[],  # Add your document models here
    )
    return client


async def close_mongodb(client: AsyncIOMotorClient):
    """
    Close the MongoDB connection.
    """
    client.close()
    print("MongoDB connection closed.")
