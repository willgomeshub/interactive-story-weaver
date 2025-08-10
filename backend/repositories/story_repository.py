# backend/repositories/story_repository.py
from beanie import PydanticObjectId
from abc import ABC
from typing import List, Type

from models.story import BaseStory, Story, DraftStory
from exceptions import StoryNotFoundException
from repositories.base_repository import BaseRepository


class BaseStoryRepository(BaseRepository[BaseStory], ABC):
    def __init__(self, model: Type[BaseStory], entity_display_name: str):
        super().__init__(model, entity_display_name, StoryNotFoundException)

    async def find_by_user_id(self, user_id: PydanticObjectId) -> List[BaseStory]:
        return await self._find_many_or_raise(
            {"user_id": user_id},
            f"{self.entity_display_name} with user ID '{user_id}' does not exist.",
        )

    async def find_by_title(self, title: str) -> BaseStory:
        return await self._find_one_or_raise(
            {"title": title},
            f"{self.entity_display_name} with title '{title}' does not exist.",
        )


class StoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Story, "Story", StoryNotFoundException)

    async def get_story_by_draft_id(
        self, draft_story_id: PydanticObjectId
    ) -> List[Story]:
        return await self._find_many_or_raise(
            {"draft_story_id": draft_story_id},
            f"{self.entity_display_name} with draft ID '{draft_story_id}' does not exist.",
        )

    async def get_story_by_keyword(self, keyword: str) -> List[Story]:
        return await self._find_many_or_raise(
            {"final_text": {"$regex": keyword, "$options": "i"}},
            f"{self.entity_display_name} with keyword '{keyword}' does not exist.",
        )


class DraftStoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(DraftStory, "Draft Story", StoryNotFoundException)
