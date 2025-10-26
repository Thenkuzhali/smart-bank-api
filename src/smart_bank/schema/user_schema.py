from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    password: str
    address: Optional[str]
    gov_id_type: Optional[str]
    gov_id_number: Optional[str]
    kyc_document_urls: Optional[List[str]] = []

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    address: Optional[str]
    gov_id_type: Optional[str]
    gov_id_number: Optional[str]
    kyc_document_urls: Optional[List[str]] = []
    is_active: bool

    class Config:
        orm_mode = True