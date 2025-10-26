from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.smart_bank.db.session import get_db
from src.smart_bank.services.user_service import UserService
from src.smart_bank.schema.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = UserService.create_user(db, user)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))