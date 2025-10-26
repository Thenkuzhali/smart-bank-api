from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..repositories.user_repo import UserRepository
from ..schema.user_schema import UserCreate
from ..model.kyc_documents import KycDocument

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

        # Prepare user data
        user_data = user.model_dump()
        user_data["hashed_password"] = hashed_password
        del user_data["password"]

        # Create user
        db_user = UserRepository.create_user(db, user_data)

        # Add multiple KYC documents if provided
        for doc in user.gov_ids:
            kyc_doc = KycDocument(
                user_id=db_user.id,
                gov_id_type=doc.gov_id_type,
                gov_id_number=doc.gov_id_number,
                document_url=doc.document_url
            )
            db.add(kyc_doc)
        db.commit()

        return db_user