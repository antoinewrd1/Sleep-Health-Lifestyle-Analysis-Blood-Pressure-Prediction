from fastapi import FastAPI

from src.api.routes import router


app = FastAPI(
    title="Sleep Health Blood Pressure Prediction Platform",
    version="1.0.0",
    description="API for prediction, monitoring, logging, and reporting.",
)

app.include_router(router)