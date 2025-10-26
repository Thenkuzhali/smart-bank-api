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

Audit logs for every registration and KYC update

## Use Case 2: Account Creation

### Trigger
Customer requests to create a new bank account.

---

### Flow
1. **Choose Account Type**  
   - Customer selects the type of account (Savings, Current, Fixed Deposit, etc.) via API request.  
   - System validates that the account type is supported.  

2. **System Generates Account Number**  
   - Backend generates a unique account number following a pattern, e.g., `ACC-YYYYMMDD-XXXX`.  
   - Ensures no collisions with existing accounts.  

3. **Initial Deposit Validation**  
   - Customer submits initial deposit amount.  
   - System validates against the minimum required deposit for the chosen account type.  
   - If valid, account creation proceeds; if invalid, the request is rejected with a meaningful error message.  

4. **Account Creation Confirmation**  
   - Backend stores account details in the database (linked to user ID).  
   - Returns the account number, type, initial balance, and status (`ACTIVE`).  

---

### JWT Authentication for Login
- **Purpose:** Secure customer access to account operations.  
- **Flow:**
  1. Customer logs in with email and password.
  2. Backend verifies credentials and returns a JWT token.  
  3. Token includes user ID, role, and expiration time.  
  4. Token is required for subsequent operations like account creation, balance check, and transactions.  

- **Endpoints:**
  - `POST /api/v1/auth/login` → Returns JWT token.
  - Middleware validates JWT token for protected endpoints.

---

### API Contract

#### 1. Create Account
**POST /api/v1/accounts/create**  

**Request Body:**
```json
{
  "user_id": "USR-20251026-001",
  "account_type": "SAVINGS",
  "initial_deposit": 5000
}
```
**Response:**
```json
{
  "account_number": "ACC-20251026-0001",
  "account_type": "SAVINGS",
  "balance": 5000,
  "status": "ACTIVE",
  "message": "Account created successfully."
}
```
#### 2. Get Account Details

**GET /api/v1/accounts/{account_number}**

**Response:**
{
  "account_number": "ACC-20251026-0001",
  "user_id": "USR-20251026-001",
  "account_type": "SAVINGS",
  "balance": 5000,
  "status": "ACTIVE",
  "created_at": "2025-10-26T13:00:00Z"
}
