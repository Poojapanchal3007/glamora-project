from fastapi import FastAPI

app = FastAPI(
    title="Glamora by Pooja API",
    description="Salon Booking and Management System",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "salon": "Glamora by Pooja",
        "location": "Oulu, Finland",
        "message": "Backend is running successfully"
    }
