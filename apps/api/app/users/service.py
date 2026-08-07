from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.users.repository import UserRepository
from app.users.schemas import UserCreate
from app.core.security import hash_password


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(
        self,
        db,
        user,
    ):

        existing = self.repository.get_by_email(
            db,
            user.email,
        )

        if existing:
            raise ValueError("Email already exists")

        hashed_password = hash_password(
            user.password
        )

        return self.repository.create(
            db=db,
            full_name=user.full_name,
            email=user.email,
            hashed_password=hashed_password,
        )

    def list_users(
        self,
        db: Session,
    ):
        return self.repository.list(db)

    def get_user(
        self,
        db: Session,
        user_id: str,
    ):

        user = self.repository.get_by_id(
            db,
            user_id,
        )

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )

        return user