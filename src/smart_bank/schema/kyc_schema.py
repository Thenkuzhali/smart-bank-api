from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class KYCVerifyRequest(BaseModel):
    verified_by: Optional[str] = "SYSTEM_AI"

class KYCResponse(BaseModel):
    user_id: str
    kyc_status: str
    verified_by: Optional[str]
    verified_at: Optional[datetime]

    class Config:
        orm_mode = True