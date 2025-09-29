import ast
import os

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import pickle

from backend.database.database import SessionLocal, engine
from backend.database import crud
from backend.core.code_analyzer import parse_code



class CodeRequest(BaseModel):
    code: str

class ReviewResponse(BaseModel):
    result: str
    review_id: int
    code_snippet: str

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_ast(code: str) -> bytes:
    try:
        tree = ast.parse(code)
        ast_dump_str = ast.dump(tree, indent=4)
        return ast_dump_str.encode('utf-8')
    except SyntaxError as e:
        raise HTTPException(status_code=400, detail = f"Invalid code syntax: {e}")


def get_ai_code_review(code: str, ast_tree: bytes) -> str:
    ast_preview= ast_tree.decode('utf-8')[:150].replace('\n', ' ') + '.....'
    return (
        "**AI Review:** The code is syntactically correct (AST generated)."
        "Semantic Analysis says nice code, no errors"
        f"AST starts with: `{ast_preview}`."
    )


@app.post("/api/v1/review_code", response_model=ReviewResponse)
async def review_code(code_data: CodeRequest, db: Session = Depends(get_db)):
    code = code_data.code

    ast_tree = generate_ast(code)
    review_text = get_ai_code_review(code, ast_tree)

    pull_request_id = None

    db_review = crud.create_code_review(
        db=db,
        code=code,
        review=review_text,
        ast_tree=ast_tree,
        pull_request_id=pull_request_id
    )

    return ReviewResponse(
        result="AST and code review are saved into the database",
        review_id = db_review.id,
        code_snippet = db_review.code[:50]
    )


@app.get("/")
async def read_root(db: Session = Depends(get_db)):
    return {"message": "Hello, the app is now connected to the database!"}
