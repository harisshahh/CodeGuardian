from sqlalchemy.orm import Session
from .import models


def create_code_review(db: Session, code: str, review: str, ast_tree: bytes):
    db_review = models.CodeReview(code=code, review=review, ast_tree=ast_tree)
    db.add(db_review)
    db.commit(db_review)
    db.refresh()
    return db_review

