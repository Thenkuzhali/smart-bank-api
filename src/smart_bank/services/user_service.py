from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..repositories.user_repo import UserRepository
from ..schema.user_schema import UserCreate

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class UserService:

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def create_user(db: Session, user: UserCreate):
        # Check if email or phone already exists
        if UserRepository.get_by_email(db, user.email):
            raise ValueError("Email already registered")
        if UserRepository.get_by_phone(db, user.phone_number):
            raise ValueError("Phone number already registered")

        # Hash password
        hashed_password = UserService.hash_password(user.password)

        user_data = user.model_dump()
        user_data["hashed_password"] = hashed_password
        del user_data["password"]  # remove plain password
        
        # Serialize list fields
        import json
        user_data["kyc_document_urls"] = json.dumps(user_data.get("kyc_document_urls", []))

        return UserRepository.create_user(db, user_data)        