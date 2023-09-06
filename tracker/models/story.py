from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from tracker.models.base import Base


class Story(Base):
    name: str = Column(String(50))

    bug = relationship("Bug", back_populates="story")

    __tablename__: str = "story"

    class Config:
        orm_mode = True
