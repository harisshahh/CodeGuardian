from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..database.database import SessionLocal, engine
from ..database import models
from ..core.code_analyzer import parse_code



class CodeRequest(BaseModel):
    code: str

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")

async def read_root(db: Session = Depends(get_db)):
    return {"message": "Hello, the app is now connected to the database!"}

@app.post("/api/v1/review_code")
async def review_code(code_request: CodeRequest):
    ast_tree = parse_code(code_request.code)
    
    if isinstance(ast_tree, dict) and "error" in ast_tree:
        return {"result": "Parsing Failed", "details": ast_tree["error"]}
    else:
        return{"result": "Code successfully parsed!", "details": str(ast_tree)}
    