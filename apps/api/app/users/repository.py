from sqlalchemy.orm import Session

from app.users.models import User
from app.users.schemas import UserCreate


class UserRepository:

    def create(
        self,
        db: Session,
        full_name: str,
        email: str,
        hashed_password: str,
    ) -> User:

        db_user = User(
            full_name=full_name,
            email=email,
            hashed_password=hashed_password,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> User | None:

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_by_id(
        self,
        db: Session,
        user_id: int,
    ) -> User | None:

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def list(
        self,
        db: Session,
    ) -> list[User]:

        return (
            db.query(User)
            .order_by(User.id)
            .all()
        )