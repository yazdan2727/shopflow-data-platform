from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    verify_password,
)
from app.users.repository import UserRepository


class AuthService:

    def __init__(self):
        self.repository = UserRepository()

    def login(
        self,
        db: Session,
        email: str,
        password: str,
    ):

        user = self.repository.get_by_email(
            db,
            email,
        )

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        token = create_access_token(
            user_id=user.id,
            role=user.role.value,
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }