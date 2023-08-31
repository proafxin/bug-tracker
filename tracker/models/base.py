from sqlalchemy import TIMESTAMP, Column, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.sql import func

from tracker.db.session import BaseModel


class Base(BaseModel):
    __abstract__ = True

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at: Mapped[TIMESTAMP] = Column(
        TIMESTAMP, server_default=func.now(), index=True
    )
    updated_at: Mapped[TIMESTAMP] = Column(
        TIMESTAMP,
        server_default=func.now(),
        server_onupdate=func.current_timestamp(),
        index=True,
    )
