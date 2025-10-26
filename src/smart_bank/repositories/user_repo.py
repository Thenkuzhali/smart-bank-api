from sqlalchemy.orm import Session
from ..model.user import User

class UserRepository:

    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_by_phone(db: Session, phone_number: str):
        return db.query(User).filter(User.phone_number == phone_number).first()

    @staticmethod
    def create_user(db: Session, user_data: dict):
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user