from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .database import Base

class PullRequest(Base):
    __tablename__ = "pull_requests"
    id = Column(Integer, primary_key = True, index = True)
    github_id = Column(Integer, unique = True, index = True)
    title = Column(String)
    reviews = relationship("Reviews", back_populates = "pull_request")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key = True, index = True)
    pull_request_id = Column(Integer, ForeignKey("pull_requests.id"))
    content = Column(String)
    pull_request = relationship("PullRequest", back_populates = "reviews")

class CodeReview(Base):
    __tablename__ = "code_reviews"
    id = Column(Integer, primary_key = True, index = True)
    code = Column(String)
    review = Column(String)
    ast_tree = Column(LargeBinary, nullable=True)
