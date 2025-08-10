# backend/models/base.py
from datetime import datetime
from beanie import Document, PydanticObjectId
from pydantic import Field
from pymongo import DESCENDING


class Timestamped(Document):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    async def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        await super().save(*args, **kwargs)

    class Settings:
        is_document = False
        # indexes = [
        #     {
        #         "fields": [("created_at", DESCENDING)],
        #         "name": "created_at_index",
        #     },
        #     {
        #         "fields": [("updated_at", DESCENDING)],
        #         "name": "updated_at_index",
        #     },
        # ]
