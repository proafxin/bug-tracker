from fastapi import FastAPI

from tracker.db.session import engine
from tracker.models.bug import Bug
from tracker.models.story import Story
from tracker.views.bug import router as bug_router
from tracker.views.story import router as story_router

api = FastAPI(title="Bug Tracker", description="Simple bug tracking  API.")


@api.on_event(event_type="startup")
async def start():
    await configure()


@api.on_event(event_type="shutdown")
async def shutdown():
    await engine.dispose()


async def configure_db():
    async with engine.begin() as conn:
        await conn.run_sync(Bug.metadata.create_all)
        await conn.run_sync(Story.metadata.create_all)


def configure_router():
    api.include_router(story_router)
    api.include_router(bug_router)


async def configure():
    configure_router()
