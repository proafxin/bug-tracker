from datetime import datetime

from pydantic import ConfigDict

from tracker.serializers.base import Base


class StoryInput(Base):
    name: str


class StoryOutput(StoryInput):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
