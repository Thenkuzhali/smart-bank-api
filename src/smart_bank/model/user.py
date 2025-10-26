from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from ..db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone_number = Column(String(20), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    address = Column(Text, nullable=True)

    # Government ID for KYC (store encrypted or hashed)
    gov_id_type = Column(String(50), nullable=True)
    gov_id_number = Column(String(255), nullable=True)  # encrypted
    kyc_document_urls = Column(Text, nullable=True)     # JSON string of URLs

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())