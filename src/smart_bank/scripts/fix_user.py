import json
from sqlalchemy.orm import Session
from src.smart_bank.db.session import get_db
from src.smart_bank.model.user import User

db: Session = next(get_db())

users = db.query(User).all()

for u in users:
    # Fix stringified JSON lists
    if isinstance(u.kyc_document_urls, str):
        try:
            u.kyc_document_urls = json.loads(u.kyc_document_urls)
        except json.JSONDecodeError:
            u.kyc_document_urls = []

    # Fix missing active flag
    if u.is_active is None:
        u.is_active = True

db.commit()
print("✅ Fixed all user records.")
