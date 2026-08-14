from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.users.models import User
from app.db.dependencies import get_db
from app.users.schemas import UserCreate, UserResponse
from app.users.service import UserService
from app.auth.dependencies import get_current_user_id
from app.auth.dependencies import require_admin

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

service = UserService()


@router.post(
    "",
    response_model=UserResponse,
    status_code=201,
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):

    return service.create_user(
        db,
        user,
    )

@router.get("/admin")
def admin_endpoint(
    current_user: User = Depends(require_admin),
):
    return {
        "message": "Welcome admin",
        "user_id": current_user.id,
    }

@router.get(
    "/admin-test",
)
def admin_test(
    current_user: User = Depends(require_admin),
):
    return {
        "message": "You are an admin",
        "user_id": current_user.id,
        "role": current_user.role,
    }

@router.get(
    "",
    response_model=list[UserResponse],
)
def list_users(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_id),
):
    return service.list_users(db)

@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User= Depends(get_current_user_id),
):
    return current_user

@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user_id),
):
    return service.get_user(
        db,
        user_id,
    )