from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.schemas import (
    LoginRequest,
    TokenResponse,
)
from app.auth.service import AuthService
from app.db.dependencies import get_db


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


service = AuthService()


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    return service.login(
        db=db,
        email=request.email,
        password=request.password,
    )