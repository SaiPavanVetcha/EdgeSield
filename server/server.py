import uvicorn
from config import HOST, PORT
from fastapi import FastAPI
from routes.metrics import router as metrics_router

app = FastAPI(
    title="EdgeShield Central Server API",
    description="Backend service for collecting telemetry and environmental metrics.",
    version="1.0.0",
)

# Register routes
app.include_router(metrics_router)


@app.on_event("startup")
def startup_event():
    print("[*] EdgeShield Central Server started successfully.")


@app.get("/")
def health_check():
    return {"status": "online", "system": "EdgeShield Server Backend"}


if __name__ == "__main__":
    print(f"[*] Starting EdgeShield Server on http://{HOST}:{PORT}")
    uvicorn.run("server:app", host=HOST, port=PORT, reload=True)