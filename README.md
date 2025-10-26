# Smart Bank Backend System

##  Overview
Smart Bank is a secure backend banking system designed using a **3-tier architecture** (Controller → Service → Repository) built with **FastAPI**.  
It supports multi-user operations and is designed to scale with features like:

- **KYC verification**
- **Account management**
- **Money transfer**
- **Loan processing**
- **Fraud detection**
- **Audit logging**

The system prioritizes **data security**, **encryption of sensitive information**, and **modular design**.

---

## System Architecture
```
FastAPI Backend (3-Tier)
│
├── Controller Layer → Handles API endpoints, request validation
├── Service Layer → Business logic, workflow orchestration
└── Repository Layer → Database interaction (CRUD via SQLAlchemy)
```

### Additional Components

- **Authentication & Authorization** → JWT-based multi-role system (Admin, Customer, Auditor)  
- **Encryption Service** → Encrypts sensitive details like Government ID using AES/RSA  
- **File Service** → Secure KYC document upload to cloud/local storage  
- **Logging Service** → Audit trails for all key operations  
- **Reporting API** → Analytics and dashboards for administrators  

---

## First Use Case: User Registration & KYC Verification

### Description

A new customer registers by submitting **personal details** and **KYC documents**.  

The system:

1. Validates user input.
2. Encrypts sensitive government ID fields.
3. Uploads KYC documents securely.
4. Stores the user profile and verification status.
5. Triggers a KYC validation workflow (manual or automated).

---

## API Contract

### 1️⃣ `POST /api/v1/users/register`

Registers a new user and stores encrypted KYC details.

**Request Body:**

```json
{
    "first_name": "Thenkuzhali",
    "last_name": "S",
    "email": "thenkuzhali@example.com",
    "phone_number": "+91-9876543210",
    "password": "Strong@123",
    "address": "Trichy, Tamil Nadu, India",
    "gov_id_type": "Aadhaar",
    "gov_id_number": "1234-5678-9123",
    "kyc_document_urls": [
        "https://storage.smartbank.in/kyc/thenkuzhali_adhar_front.png",
        "https://storage.smartbank.in/kyc/thenkuzhali_adhar_back.png"
    ]
}
```
**Response:**
```json
{
    "user_id": "USR-20251026-001",
    "message": "User registered successfully. KYC validation in progress.",
    "status": "PENDING_KYC"
}
```

### 2️⃣ GET /api/v1/users/{user_id}

Fetch user profile and KYC status.

**Response:**
```json
{
    "user_id": "USR-20251026-001",
    "name": "Thenkuzhali S",
    "email": "thenkuzhali@example.com",
    "phone_number": "+91-9876543210",
    "kyc_status": "VERIFIED",
    "created_at": "2025-10-26T10:32:00Z"
}
```
### 3️⃣ POST /api/v1/kyc/verify/{user_id}

Admin or automated service verifies user KYC.

**Response:**
```json
{
    "user_id": "USR-20251026-001",
    "kyc_status": "VERIFIED",
    "verified_by": "SYSTEM_AI",
    "verified_at": "2025-10-26T12:45:00Z"
}
```

### 🔒 Security Highlights

Passwords stored using bcrypt hashing

Government IDs stored via AES-256 encryption

JWT-based authentication tokens

Audit logs for every registration and KYC update

Role-based access control (RBAC)