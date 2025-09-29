from pydantic import BaseModel
from typing import Optional, List


class CodeRequest(BaseModel):
    code: str

class ReviewResponse(BaseModel):
    result: str
    review_id: int
    code_snippet: str

class ReviewList(BaseModel):
    reviews: List[ReviewResponse] 
    total: int

class Config:
    from_attributes = True
