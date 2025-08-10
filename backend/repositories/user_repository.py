from beanie import PydanticObjectId
from models.user import User
from exceptions import UserNotFoundException
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):

    def __init__(self):
        super().__init__(User, "User", UserNotFoundException)

    async def get_user_by_email(self, email: str) -> User:
        return await self._find_one_or_raise(
            {"email": email},
            f"{self.entity_display_name} with email '{email}' does not exist.",
        )

    async def get_user_by_username(self, username: str) -> User:
        return await self._find_one_or_raise(
            {"username": username},
            f"{self.entity_display_name} with username '{username}' does not exist.",
        )
