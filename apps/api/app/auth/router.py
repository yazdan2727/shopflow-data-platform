from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.schemas import (
    LoginRequest,
    TokenResponse,
)
from app.auth.service import AuthService
from app.db.dependencies import get_db
from app.auth.dependencies import require_admin
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


service = AuthService()


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return service.login(
        db=db,
        email=form_data.username,
        password=form_data.password,
    )