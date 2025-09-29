from sqlalchemy.orm import Session
from . import models


def create_code_review(db: Session, code: str, review: str, ast_tree: bytes, pull_request_id: int | None):
    db_review = models.CodeReview(
        code=code,
        review=review,
        ast_tree=ast_tree,
        pull_request_id=pull_request_id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_code_review_by_id(db: Session, review_id: int):
    # retrieves a single code review by primary key id
    return db.query(models.CodeReview).filter(models.CodeReview.id==review_id).first()

def get_all_code_reviews(db: Session, skip: int = 0, limit: int = 100):
    # retrieves a paginated list of all the code reviews
    return db.query(models.CodeReview).offset(skip).limit(limit).all()

