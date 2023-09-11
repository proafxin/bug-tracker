from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from tracker.models.base import Base


class Bug(Base):
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500))
    story_id: Mapped[int] = mapped_column(Integer, ForeignKey("story.id"))
    story = relationship("Story", back_populates="bug", lazy="selectin")

    __tablename__ = "bug"

    class Config:
        orm_mode = True

    def __repr__(self) -> str:
        return f"{self.title}, {self.story_id}"
