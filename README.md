# 🏛️ CSR Valera - Backend API

Main backend for the CSR Valera church digital platform. This API handles business logic, secure database connections, and provides necessary endpoints for the web client.

This repository follows a strict **Hexagonal Architecture (Ports and Adapters)** to ensure a clear separation of concerns, high testability, and framework agnosticism.

## 🛠️ Tech Stack

* **Framework:** Python with FastAPI (High performance and async support).
* **Dependency Management:** Poetry (Deterministic builds via `poetry.lock`).
* **Data Validation:** Pydantic and Type Hints.
* **Database:** SQL Server (Transact-SQL) with async connection pooling.
* **Architecture:** Hexagonal Architecture, RESTful API, SOLID principles, and DRY code.

## 🏗️ Scaffolding Overview (Hexagonal Architecture)

The project is structured as follows:

    src/
    ├── domain/               # Enterprise business rules and models. NO external dependencies here.
    │   ├── entities/         # Pydantic models representing business objects.
    │   ├── exceptions/       # Custom business logic exceptions.
    │   └── ports/            # Abstract base classes/Interfaces (e.g., Repository interfaces).
    │
    ├── application/          # Application business rules (Use Cases).
    │   ├── use_cases/        # Orchestrates the flow of data using Domain entities and Ports.
    │   └── dtos/             # Data Transfer Objects for input/output validation.
    │
    ├── infrastructure/       # External agencies (Database, Web Framework, Third-party APIs).
    │   ├── adapters/         # Implementations of the domain ports (e.g., SQLServerUserRepository).
    │   │   └── database/     # Async SQL Server connection pooling and Transact-SQL execution.
    │   ├── api/              # FastAPI specific code (Controllers/Routers).
    │   │   ├── routers/      # Endpoint definitions.
    │   │   └── dependencies/ # FastAPI dependency injection (e.g., get_db_session).
    │   └── config/           # Environment variables and app configuration.
    │
    ├── tests/                # Unit and Integration tests.
    │
    └── main.py               # Application entry point, FastAPI setup, and DI wiring.

## 🧠 Key Architecture Principles
- **Dependency Inversion:** The `domain` does not depend on `infrastructure`. The `infrastructure` depends on the `domain`.
- **Type Hinting & Pydantic:** Strict typing is enforced across all layers to ensure data integrity.
- **Error Handling:** SQL Server specific errors must be caught at the `infrastructure` layer and translated into domain exceptions before reaching the `application` layer.

## ⚙️ Local Setup (Development)

This project uses **Poetry** for dependency management to ensure deterministic builds.

1. Clone this repository:
   `git clone https://github.com/tu-org/csr-backend.git`
2. Ensure you have Poetry installed on your system (https://python-poetry.org/docs/#installation).
3. Install dependencies and create the virtual environment automatically:
   `poetry install`
4. Activate the virtual environment shell:
   `poetry shell`
5. Set up your environment variables in a `.env` file (Request SQL Server credentials from the Tech Lead).
6. Run the development server (Example):
   `fastapi dev src/main.py` (or `uvicorn src.main:app --reload`)

## 🌿 Gitflow & Workflow

This project enforces strict conventions:
* `main`: Production (Stable and tested). **Direct commits are forbidden.**
* `develop`: Integration environment. All features are born and merged here via Pull Requests.
* Branch naming conventions: `feat/feature-name`, `chore/setup-task`, `fix/bug-description`.
* Commits: Must follow the Conventional Commits standard.