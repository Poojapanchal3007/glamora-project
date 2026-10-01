# Glamora by Pooja

A salon website and booking-management frontend prototype, with a small FastAPI backend starter.

## Technologies

React · JavaScript · Vite · CSS · Python · FastAPI

## Current scope

The frontend includes booking-request and salon-management interfaces. The booking form uses a pre-filled email request. The assistant is a frontend prototype; live AI, calendar, database and messaging integrations require further backend work. The current FastAPI backend provides a root endpoint returning salon information.

## Run the frontend

```bash
cd glamora-frontend
npm install
npm run dev
```

Build it with `npm run build`. See the [frontend documentation](glamora-frontend/README.md) for booking email configuration and integration plans.

## Run the backend starter

In a Python virtual environment:

```bash
python -m pip install fastapi uvicorn
cd glamora-api
python -m uvicorn main:app --reload
```

## Explore the code

- [React frontend](glamora-frontend/src/)
- [FastAPI starter](glamora-api/main.py)
- [Project directory](PROJECTS.md) — links to my web, mobile and team academic projects
