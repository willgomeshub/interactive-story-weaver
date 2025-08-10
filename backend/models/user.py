# backend/models/user.py
from pydantic import EmailStr
from pymongo import ASCENDING

from models.base import Timestamped


class User(Timestamped):
    username: str = ...
    email: EmailStr = ...
    password_hash: str = ...

    class Settings:
        name = "users"
        is_document = True
        # indexes = [
        #     {
        #         "fields": [("username", ASCENDING)],
        #         "name": "username_index",
        #         "unique": True,
        #     },
        #     {
        #         "fields": [("email", ASCENDING)],
        #         "name": "email_index",
        #         "unique": True,
        #     },
        # ]
