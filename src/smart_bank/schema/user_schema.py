from pydantic import BaseModel, EmailStr
from typing import List, Optional

class KycDocumentCreate(BaseModel):
    gov_id_type: str
    gov_id_number: str
    document_url: str

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    password: str
    address: Optional[str]
    gov_ids: Optional[List[KycDocumentCreate]] = []  # list of multiple KYC documents

class KycDocumentResponse(BaseModel):
    gov_id_type: str
    gov_id_number: str
    document_url: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    address: Optional[str]
    is_active: bool
    gov_ids: Optional[List[KycDocumentResponse]] = []

    class Config:
        orm_mode = True