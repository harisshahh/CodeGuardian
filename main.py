from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from typing import Dict
import logging

from .models.code_request import CodeRequest, CodeResponse
from .services.openai_service import get_code_review_response
from .config import settings 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title = "Code Guardian API"
    description = "AI-powered code review and explanation service"
    version = "1.0.0"
)

#Configure CORS for React frontend to interact with FastAPI backend
origins = [
    "http://localhost:3000" #Frontend dev server
    "http://127.0.0.1:3000" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = true,
    allow_methods["*"], #Allow all methods (GET, POST, PUSH, etc.)
    allow_headers["*"],
)

@app.get("/")
async def read_root() -> Dict[str, str]:
    '''
    The Root endpoint of the API
    Returns a message to confirm that the API is running
    '''
    return {"message": "Welcome to the CodeGuardian API"}

@app.post("/analyze")
def analyze: req(CodeRequest):
    template = PromptTemplate.from_template(
        "You are an expert software engineer/code analyzer. Please {goal} the following code:\n\n{code}"
    )
    prompt = template.format(goal = req.goal, code = req.code)
    response = llm(prompt)
    return {"result": response}
