from fastapi import FastAPI

from tracker.db.session import engine
from tracker.views.bug import router as bug_router
from tracker.views.story import router as story_router

app = FastAPI(title="Bug Tracker", description="Simple bug tracking  API.")


@app.on_event(event_type="startup")
async def start():
    await configure()


@app.on_event(event_type="shutdown")
async def shutdown():
    await engine.dispose()


def configure_router():
    app.include_router(story_router)
    app.include_router(bug_router)


async def configure():
    configure_router()
