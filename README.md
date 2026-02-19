# AI-Assisted STEM Education App

This project provides an AI-assisted STEM education app built with FastAPI and React. The backend is responsible for Python code execution and AI explanation endpoints, while the frontend features a code editor for user interaction.

## Setup

### Backend
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Frontend
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```

## Local Run

### Backend
Run the FastAPI app:
```bash
uvicorn main:app --reload
```

### Frontend
Run the React app:
```bash
npm start
```

## Deployment

For deploying the application on Railway, follow the deployment guide provided in `DEPLOYMENT.md`.  

Make sure to configure environment variables as mentioned in `.env.example` before deployment.
