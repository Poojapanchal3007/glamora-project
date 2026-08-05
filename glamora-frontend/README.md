# Glamora by Pooja

AI-Powered Salon Booking and Business Management System

## Tech Stack

- React
- FastAPI
- PostgreSQL
- Telegram Bot
- OpenAI Integration

## Features

- Salon website
- Online appointment booking request form
- Salon manager dashboard for bookings, services, and customer email drafts
- Built-in salon assistant interface for booking, service, and customer-management help
- Admin dashboard
- Inventory management
- Income & expense tracking
- AI assistant
- Telegram management bot

## Developer

Pooja Panchal
University Summer Project 2026

## Booking email setup

The booking form opens a pre-filled email request. Create a `.env.local` file with your real salon inbox before deploying:

```env
VITE_SALON_EMAIL=your-real-email@example.com
```

For automatic booking emails without relying on a visitor's email app, connect the form to an email service or backend (for example, Formspree, Resend, or a FastAPI endpoint).

## Making the assistant real

The current assistant is a frontend prototype. To have it genuinely manage Google/Outlook Calendar, send email, and use OpenAI, connect it to a secure FastAPI backend. The backend should keep API keys private, store bookings in PostgreSQL, and connect only after Pooja authorizes her calendar and email account.
