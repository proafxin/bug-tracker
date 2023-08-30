from datetime import datetime

from tracker.serializers.base import Base
from tracker.serializers.story import StoryOutput


class BugBase(Base):
    title: str
    description: str


class BugInput(BugBase):
    story_id: int


class BugOutput(BugInput):
    story: StoryOutput
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
