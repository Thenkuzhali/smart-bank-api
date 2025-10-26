from sqlalchemy.orm import Session
from src.smart_bank.repositories.kyc_repo import KYCRepository
from src.smart_bank.model.kyc import KYC

class KYCService:
    @staticmethod
    def verify_kyc(db: Session, user_id: str, verified_by: str = "SYSTEM_AI") -> KYC:
        try:
            kyc = KYCRepository.verify_user_kyc(db, user_id, verified_by)
            return kyc
        except ValueError as e:
            raise e