<div align="center">

# 🚀 FastAPI Fundamentals - Platzi

> A comprehensive learning project exploring core FastAPI concepts and best practices

[![Python](https://img.shields.io/badge/Python-3.13+-3776ab?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.124.4+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLModel](https://img.shields.io/badge/SQLModel-0.0.27+-blue?style=flat&logo=sql&logoColor=white)](https://sqlmodel.tiangolo.com/)

</div>

## 📋 Overview

This project is a practical implementation of FastAPI fundamentals, covering essential concepts including:

- **API Design** – RESTful endpoints and request/response handling
- **Database Integration** – SQLite with SQLModel ORM
- **Models** – Structured data models for Customers, Invoices, Plans, and Transactions
- **Testing** – Unit tests with Pytest for reliable code
- **Project Organization** – Modular architecture with routers and separation of concerns

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| **FastAPI** | 0.124.4+ | Web framework for building APIs |
| **SQLModel** | 0.0.27+ | SQL toolkit & ORM |
| **SQLite3** | Built-in | Database |
| **Pytest** | Latest | Testing framework |
| **Python** | 3.13+ | Programming language |

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- pip package manager

### Setup

1. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate (Linux/macOS)
   source venv/bin/activate
   
   # Activate (Windows)
   venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install "fastapi[standard]"
   pip install sqlmodel
   pip install pytest
   ```

3. **Run the development server**
   ```bash
   fastapi dev
   ```

## 📊 Database Management

### SQLite3 Commands

Access and manage your SQLite database:

```bash
# Open SQLite3 shell
sqlite3 .\db.sqlite3

# List all tables
.tables

# Exit SQLite3
.exit
```

## 📁 Project Structure

```
src/
├── app/              # Main application module
│   ├── main.py      # FastAPI application entry point
│   ├── routers/     # API endpoint definitions
│   └── test.py      # Application tests
├── models/          # Data models
│   ├── Customer.py
│   ├── Invoice.py
│   ├── Plan.py
│   └── Transaction.py
├── db.py            # Database configuration
├── conftest.py      # Pytest configuration
└── requirements.txt # Project dependencies
```

## 🧪 Testing

Run tests using Pytest:

```bash
pytest
```

## 🔧 VS Code Extensions

Recommended extensions are automatically installed via PowerShell script:

```powershell
./scripts/install-vscode-extensions.ps1
```

> **Note:** If using a proxy or self-signed certificates, install extensions manually through VS Code UI or add the CA to your Windows trust store.

## 📚 Key Concepts Covered

- ✅ REST API principles
- ✅ Request validation with Pydantic models
- ✅ Database relationships with SQLModel
- ✅ Async/await patterns
- ✅ Error handling and status codes
- ✅ Dependency injection
- ✅ Unit testing best practices

## 📝 License

This project is open source and available under the MIT License.

<div align="center" style="margin-top: 40px; padding: 20px;">

Made with ❤️ and ☕ from 🇳🇮, Juan Gómez

</div>