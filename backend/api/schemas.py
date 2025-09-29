from pydantic import BaseModel
from typing import Optional



class CodeInput(BaseModel):
    code: str

class CodeDetails(BaseModel):
    result: str
    review_id: int
    code: str
    review: str
    


class Config:
    from_attributes = True
