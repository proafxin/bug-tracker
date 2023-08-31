from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from tracker.models.base import Base


class Bug(Base):
    title: str = Column(String(100))
    description: str = Column(String(500))
    story_id = Column(Integer, ForeignKey("story.id"))
    story = relationship("Story", back_populates="bug")

    __tablename__ = "bug"
