import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import random

# Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-bridge")

# initialize API service (entry point for all endpoints)
app = FastAPI(
    title="AI-Bridge-Service",
    description="Enterprise-ready API wrapper for LLM orchestration (Mock Mode)",
    version="1.0.0"
)

# request schema for incoming prompts (auto validation)
class AIQuery(BaseModel):
    """Schema for incoming AI prompts with validation."""
    prompt: str = Field(..., min_length=1, example="Was ist Musik?")


@app.get("/")
async def root():
    """Health check endpoint."""
    return {"status": "online", "message": "AI-Bridge-Service is ready."}


# main endpoint: receives prompt and returns mock AI response
@app.post("/analyze")
async def ask_ai(query: AIQuery):
    """Processes the prompt and returns a randomized mock AI response."""
    logger.info(f"Received AI query: {query.prompt}")

    # mock responses (simulating LLM output)
    responses = [
        f"Analyse abgeschlossen für: {query.prompt}. Ergebnis: Hohe Relevanz.",
        "Die Daten wurden erfolgreich verarbeitet und validiert.",
        "KI-Modell empfiehlt: System-Integration fortsetzen."
    ]

    return {
        "status": "success",
        "answer": random.choice(responses),
        "engine": "mock-llm-1.5"
    }


# run local dev server
if __name__ == "__main__":
    import uvicorn


    uvicorn.run(app, host="127.0.0.1", port=8000)