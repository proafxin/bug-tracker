import asyncio

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from tracker.db.session import get_db
from tracker.models.base import Base
from tracker.views.bug import router as bug_router
from tracker.views.story import router as story_router

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test_db.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionTesting = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture(scope="class")
async def app():
    session = SessionTesting()
    app_test = FastAPI()
    app_test.dependency_overrides[get_db] = lambda: session
    app_test.include_router(bug_router)
    app_test.include_router(story_router)

    yield app_test

    await session.close()


@pytest_asyncio.fixture(scope="class")
async def client(app: FastAPI) -> AsyncClient:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        async with AsyncClient(app=app, base_url="http://test") as _client:
            yield _client

        await conn.run_sync(Base.metadata.drop_all)
        await conn.close()

        await engine.dispose()


@pytest.fixture(scope="class")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
