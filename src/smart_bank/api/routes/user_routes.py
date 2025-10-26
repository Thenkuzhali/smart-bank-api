import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.smart_bank.db.session import get_db
from src.smart_bank.services.user_service import UserService
from src.smart_bank.schema.user_schema import UserCreate, UserResponse
from src.smart_bank.model.user import User 

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        # Convert kyc_document_urls list to JSON string for storage
        user_data = user.model_dump()
        user_data["kyc_document_urls"] = json.dumps(user_data.get("kyc_document_urls", []))
        new_user = UserService.create_user(db, user)
        # Convert kyc_document_urls back to list for response
        new_user.kyc_document_urls = json.loads(new_user.kyc_document_urls or "[]")
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{user_id}", response_model=UserResponse)
def get_user_profile(user_id: str, db: Session = Depends(get_db)):
    """
    Fetch user profile and KYC status by user_id.
    """
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Convert kyc_document_urls from JSON string back to list
    if isinstance(user.kyc_document_urls, str):
        try:
            user.kyc_document_urls = json.loads(user.kyc_document_urls)
        except json.JSONDecodeError:
            user.kyc_document_urls = []

    # Ensure is_active always exists (fallback default)
    if not hasattr(user, "is_active"):
        user.is_active = True

    return user