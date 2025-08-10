# backend/repositories/interactions_repository.py
from beanie import PydanticObjectId
from typing import List

from models.interaction import Interaction
from exceptions import InteractionNotFoundException
from repositories.base_repository import BaseRepository


class InteractionRepository(BaseRepository[Interaction]):
    """
    Repository for managing interactions in the database.
    """

    def __init__(self):
        super().__init__(Interaction, "Interaction", InteractionNotFoundException)

    async def find_by_user_id(self, user_id: PydanticObjectId) -> List[Interaction]:
        return await self._find_many_or_raise(
            {"user_id": user_id},
            f"{self.entity_display_name} with user ID '{user_id}' does not exist.",
        )

    async def get_interaction_by_draft_id(
        self, draft_story_id: PydanticObjectId
    ) -> List[Interaction]:
        return await self._find_many_or_raise(
            {"draft_story_id": draft_story_id},
            f"{self.entity_display_name} with draft ID '{draft_story_id}' does not exist.",
        )

    async def find_by_parent_interaction_id(
        self, parent_interaction_id: PydanticObjectId
    ) -> List[Interaction]:
        return await self._find_many_or_raise(
            {"parent_interaction_id": parent_interaction_id},
            f"{self.entity_display_name} with parent interaction ID '{parent_interaction_id}' does not exist.",
        )
