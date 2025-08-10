from beanie import Document, PydanticObjectId

from typing import TypeVar, Generic, Type, Any, List, Optional
from abc import ABC

from exceptions import NotFoundException


T = TypeVar("T", bound=Document)


class BaseRepository(Generic[T], ABC):
    """
    Generic repository for MongoDB operations using Beanie ODM.

    Type Parameters:
        T: A Beanie Document subclass
    """

    def __init__(
        self,
        model: Type[T],
        entity_display_name: str,
        not_found_exception_model: Type[NotFoundException],
    ):
        self.model = model
        self.entity_display_name = entity_display_name
        self.not_found_exception_model = not_found_exception_model

    async def create(self, entity: T) -> T:
        """
        Create a new entity in the database.

        Args:
            entity: The entity to create

        Returns:
            The created entity with populated ID
        """
        return await entity.insert()

    # TODO ADD MORE DOCUMENTATION TO ALL METHODS
    async def list(self) -> List[T]:
        return await self.model.find_all().to_list()

    async def get_by_id(self, entity_id: PydanticObjectId) -> T:
        entity = await self.model.get(entity_id)
        if entity:
            return entity

        raise self.not_found_exception_model(
            f"{self.entity_display_name} with ID '{entity_id}' does not exist."
        )

    async def _find_one_or_raise(
        self, query: dict[str, Any], error_msg: Optional[str] = None
    ) -> T:
        entity = await self.model.find_one(query)
        if entity:
            return entity

        if not error_msg:
            error_msg = (
                f"{self.entity_display_name} not found with the provided criteria."
            )
        raise self.not_found_exception_model(error_msg)

    async def _find_many_or_raise(
        self, query: dict[str, Any], error_message: Optional[str] = None
    ) -> List[T]:
        entiy = await self.model.find(query).to_list()
        if entiy:
            return entiy

        if not error_message:
            error_message = (
                f"{self.entity_display_name} not found with the provided criteria."
            )
        raise self.not_found_exception_model(error_message)

    async def update(self, entity_id: PydanticObjectId, data: dict[str, Any]) -> T:
        entity = await self.get_by_id(entity_id)
        for key, value in data.items():
            if hasattr(entity, key):
                setattr(entity, key, value)
        await entity.save()
        return entity

    async def delete(self, entity_id: PydanticObjectId) -> None:
        entity = await self.get_by_id(entity_id)
        await entity.delete()
