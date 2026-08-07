from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    verify_password,
)
from app.users.repository import UserRepository


class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()

    def login(
        self,
        db: Session,
        email: str,
        password: str,
    ):

        user = self.user_repository.get_by_email(
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

        access_token = create_access_token(
            {
                "sub": user.id,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }