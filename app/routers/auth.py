from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserLogin, UserRegister, UserResponse
from app.schemas.token import LogoutRequest, RefreshRequest, TokenResponse
from app.services.token import refresh_token
from app.limiter import limiter
from app.services.user import register, login, logout

router = APIRouter(prefix='/auth')

@router.post('/register', response_model=UserResponse)
@limiter.limit("1/minute")
def register_user(request: Request, payload: UserRegister, db: Session = Depends(get_db)):
    return register(payload, db)

@router.post('/login', response_model=TokenResponse)
@limiter.limit("5/minute")
def login_user(request: Request, payload: UserLogin, db: Session = Depends(get_db)):
    return login(payload, db)

@router.post('/refresh', response_model=TokenResponse)
@limiter.limit("5/minute")
def refresh(request: Request, payload: RefreshRequest, db: Session = Depends(get_db)):
    return refresh_token(payload, db)

@router.post("/logout", response_model=dict)
@limiter.limit("5/minute")
def logout_user(request: Request, payload : LogoutRequest, db: Session = Depends(get_db)):
    logout(payload, db)
    return {"message": "Logged out successfully"}



