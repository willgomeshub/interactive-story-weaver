# backend/models/story.py
from typing import Optional
from beanie import PydanticObjectId
from base import Timestamped
from pymongo import ASCENDING
from abc import ABC


class BaseStory(Timestamped, ABC):
    user_id: PydanticObjectId = ...
    title: str = ...

    class Settings:
        is_document = False
        indexes = [
            {
                "fields": [("user_id", ASCENDING)],
                "name": "user_id_index",
            },
            {
                "fields": [("title", ASCENDING)],
                "name": "title_index",
            },
        ]


class Story(BaseStory):
    draft_story_id: PydanticObjectId = ...
    final_text: str = ...

    class Settings:
        name = "stories"


class DraftStory(BaseStory):
    # defined optional to solve mutual dependency with Interaction
    first_interaction_id: Optional[PydanticObjectId] = None
    current_interaction_id: Optional[PydanticObjectId] = None

    class Settings:
        name = "draft_stories"
