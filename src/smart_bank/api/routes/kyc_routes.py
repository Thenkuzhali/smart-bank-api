from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.smart_bank.schema.kyc_schema import KYCResponse, KYCVerifyRequest
from src.smart_bank.services.kyc_service import KYCService
from src.smart_bank.db.session import get_db

router = APIRouter(prefix="/api/v1/kyc", tags=["KYC"])

@router.post("/verify/{user_id}", response_model=KYCResponse)
def verify_user_kyc(user_id: str, payload: KYCVerifyRequest = Depends(), db: Session = Depends(get_db)):
    """
    Admin or automated service verifies user KYC.
    """
    try:
        kyc = KYCService.verify_kyc(db, user_id, payload.verified_by)
        return kyc
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))