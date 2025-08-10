# backend/exceptions.py


class AppBaseException(Exception):
    pass


class NotFoundException(AppBaseException):
    def __init__(self, message: str = "Data not found."):
        super().__init__(message)


class UserNotFoundException(NotFoundException):
    def __init__(self, message: str = ""):

        final_msg = f"User not found."
        if message:
            final_msg = f"{final_msg} Details: {message}"
        super().__init__(final_msg)


class StoryNotFoundException(NotFoundException):
    def __init__(self, message: str = ""):

        final_msg = f"Story not found."
        if message:
            final_msg = f"{final_msg} Details: {message}"
        super().__init__(final_msg)


class InteractionNotFoundException(NotFoundException):
    def __init__(self, message: str = ""):

        final_msg = f"Interaction not found."
        if message:
            final_msg = f"{final_msg} Details: {message}"
        super().__init__(final_msg)
