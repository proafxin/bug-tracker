from datetime import datetime

from tracker.serializers.base import Base


class StoryInput(Base):
    name: str


class StoryOutput(StoryInput):
    id: int
    created_at: datetime
    updated_at: datetime
