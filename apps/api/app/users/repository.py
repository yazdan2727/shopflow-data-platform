from sqlalchemy.orm import Session

from app.users.models import User
from app.users.schemas import UserCreate


class UserRepository:

    def create(
        self,
        db: Session,
        user: UserCreate,
    ) -> User:

        db_user = User(
            full_name=user.full_name,
            email=user.email,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    def get_by_email(
        self,
        db: Session,
        email: str,
    ):

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_by_id(
        self,
        db: Session,
        user_id: str,
    ):

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )