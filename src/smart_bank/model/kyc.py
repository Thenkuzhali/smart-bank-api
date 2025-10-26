from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.smart_bank.db.session import Base  

class KYC(Base):
    __tablename__ = "kyc"

    user_id = Column(String, ForeignKey("users.id"), primary_key=True)
    kyc_status = Column(String, default="PENDING")  # PENDING / VERIFIED / REJECTED
    verified_by = Column(String, nullable=True)
    verified_at = Column(DateTime, nullable=True)

    # relationship to user
    user = relationship("User", back_populates="kyc")
    # One-to-many relationship with KYC documents
    kyc_documents = relationship("KycDocument", back_populates="user", cascade="all, delete-orphan")