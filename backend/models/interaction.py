# backend/models/interaction.py
from beanie import PydanticObjectId
from pydantic import Field
from base import Timestamped
from pymongo import ASCENDING
from typing import Optional
from abc import ABC


class InteractionNode(Timestamped, ABC):
    # when parent is none, it means this is the first interaction
    parent_interaction_id: Optional[PydanticObjectId] = None
    # when child is none, it means that this interaction is a leaf
    child_interaction_id: Optional[PydanticObjectId] = None
    # if there are no alternatives, this is an empty list
    alternative_interactions_ids: list[PydanticObjectId] = Field(default_factory=list)

    @property
    def is_leaf(self) -> bool:
        return not self.child_interaction_id

    @property
    def is_first(self) -> bool:
        return not self.parent_interaction_id

    @property
    def is_alternative(self) -> bool:
        return bool(self.alternative_interactions_ids)

    class Settings:
        is_document = False
        indexes = [
            {
                "fields": [("parent_interaction_id", ASCENDING)],
                "name": "parent_interaction_id_index",
            }
        ]


class Interaction(InteractionNode):
    user_id: PydanticObjectId = ...
    # the draft story can exist without an interaction
    draft_story_id: PydanticObjectId = ...

    prompt_text: str = Field(..., min_length=1)
    edited_prompt_text: Optional[str] = Field(None, min_length=1)
    ai_response_text: str = Field(..., min_length=1)
    edited_ai_response_text: Optional[str] = Field(None, min_length=1)

    @property
    def is_prompt_edited(self) -> bool:
        return bool(self.edited_prompt_text)

    @property
    def is_ai_response_edited(self) -> bool:
        return bool(self.edited_ai_response_text)

    @property
    def is_edited(self) -> bool:
        return self.is_prompt_edited or self.is_ai_response_edited

    class Settings:
        name = "interactions"
        indexes = [
            {
                "fields": [("user_id", ASCENDING)],
                "name": "user_id_index",
            },
            {
                "fields": [("draft_story_id", ASCENDING)],
                "name": "draft_story_id_index",
            },
        ]
