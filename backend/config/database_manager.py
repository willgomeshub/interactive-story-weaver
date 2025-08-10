# config/database_manager.py
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from typing import List, Type
from beanie import Document


class DatabaseManager:
    _client: AsyncIOMotorClient = None
    _database = None

    @classmethod
    async def connect(
        cls, connection_string: str, database_name: str, models: List[Type[Document]]
    ):
        """Conecta ao MongoDB e inicializa Beanie"""
        if cls._client is None:
            cls._client = AsyncIOMotorClient(connection_string)
            cls._database = cls._client[database_name]
            # cls._database = cls._client.get_default_database()
            await init_beanie(database=cls._database, document_models=models)

    @classmethod
    async def close(cls):
        """Fecha a conexão"""
        if cls._client:
            cls._client.close()
            cls._client = None
            cls._database = None

    @classmethod
    @asynccontextmanager
    async def get_session(cls):
        """Context manager para transações (se necessário)"""
        if cls._client is None:
            raise RuntimeError("Database not connected. Call connect() first.")

        async with await cls._client.start_session() as session:
            yield session


#   #session usage example
#   async def create_with_transaction(self, data: dict) -> T:
#       async with DatabaseManager.get_session() as session:
#           async with session.start_transaction():
#               entity = self.model(**data)
#               return await entity.insert(session=session)
