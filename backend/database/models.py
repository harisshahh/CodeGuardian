from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class PullRequest(Base):
    __tablename__ = "pull_requests"
    id = Column(Integer, primary_key = True, index = True)
    github_id = Column(Integer, unique = True, index = True)
    title = Column(String)
    reviews = relationship("Reviews", back_populates = "pull_request")
    