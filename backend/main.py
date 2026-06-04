from fastapi import FastAPI
from app.api import auth, dashboard

app = FastAPI(title="BalKavach AI Backend")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}
