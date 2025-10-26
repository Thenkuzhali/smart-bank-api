from fastapi import FastAPI
from src.smart_bank.db.session import Base, engine
from src.smart_bank.api.routes.user_routes import router as user_router
from src.smart_bank.api.routes.kyc_routes import router as kyc_router
# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Bank API")

# Include user routes
app.include_router(user_router)
app.include_router(kyc_router, prefix="/kyc")

@app.get("/")
def root():
    return {"message": "Welcome to Smart Bank API"}