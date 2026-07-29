from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.users.repository import UserRepository
from app.users.schemas import UserCreate


class UserService:

    def __init__(self):

        self.repository = UserRepository()

    def create_user(
        self,
        db: Session,
        user: UserCreate,
    ):

        existing = self.repository.get_by_email(
            db,
            user.email,
        )

        if existing:

            raise HTTPException(
                status_code=409,
                detail="Email already exists",
            )

        return self.repository.create(
            db,
            user,
        )