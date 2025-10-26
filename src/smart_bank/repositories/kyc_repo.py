from sqlalchemy.orm import Session
from datetime import datetime
from src.smart_bank.model.kyc import KYC
from src.smart_bank.model.user import User

class KYCRepository:

    @staticmethod
    def verify_user_kyc(db: Session, user_id: str, verified_by: str = "SYSTEM_AI") -> KYC:
        # Fetch KYC record or create one if missing
        kyc = db.query(KYC).filter(KYC.user_id == user_id).first()
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")

        if not kyc:
            kyc = KYC(user_id=user_id)
            db.add(kyc)

        if kyc.kyc_status == "VERIFIED":
            raise ValueError("User KYC is already verified")

        # Update KYC fields
        kyc.kyc_status = "VERIFIED"
        kyc.verified_by = verified_by
        kyc.verified_at = datetime.utcnow()

        db.commit()
        db.refresh(kyc)
        return kyc