from datetime import datetime

from pydantic import BaseModel


class Base(BaseModel):
    id: int
    created_at: datetime = datetime.now()
