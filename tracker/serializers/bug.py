from datetime import datetime

from pydantic import ConfigDict

from tracker.serializers.base import Base
from tracker.serializers.story import StoryOutput


class BugBase(Base):
    title: str
    description: str


class BugInput(BugBase):
    story_id: int


class BugOutput(BugInput):
    model_config = ConfigDict(from_attributes=True)

    id: int
    story: StoryOutput
    created_at: datetime
    updated_at: datetime
