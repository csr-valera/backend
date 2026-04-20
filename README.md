# 🏛️ CSR Valera - Backend API

Main backend for the CSR Valera church digital platform. This API handles business logic, secure database connections, and provides necessary endpoints for the web client.

## 🛠️ Tech Stack

* **Framework:** Python with FastAPI (High performance and async support).
* **Data Validation:** Pydantic and Type Hints.
* **Database:** SQL Server (Transact-SQL) with async connection pooling.
* **Architecture:** RESTful API, SOLID principles, and DRY code.

## ⚙️ Local Setup (Development)

1. Clone this repository:
   `git clone https://github.com/tu-org/csr-backend.git`
2. Create a virtual environment:
   `python -m venv venv`
3. Activate the virtual environment:
   * Windows: `.\venv\Scripts\activate`
   * Mac/Linux: `source venv/bin/activate`
4. Install dependencies (Once requirements.txt is created):
   `pip install -r requirements.txt`
5. Set up your environment variables in a `.env` file (Request SQL Server credentials from the Tech Lead).

## 🌿 Gitflow & Workflow

This project enforces strict conventions:
* `main`: Production (Stable and tested). **Direct commits are forbidden.**
* `develop`: Integration environment. All features are born and merged here via Pull Requests.
* Branch naming conventions: `feat/feature-name`, `chore/setup-task`, `fix/bug-description`.
* Commits: Must follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standard.