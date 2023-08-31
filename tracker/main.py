from fastapi import FastAPI

from tracker.db.session import engine
from tracker.models.bug import Bug
from tracker.models.story import Story
from tracker.views.bug import router as bug_router
from tracker.views.story import router as story_router

api = FastAPI()


def configure_db():
    Bug.metadata.create_all(engine)
    Story.metadata.create_all(engine)


def configure_router():
    api.include_router(story_router)
    api.include_router(bug_router)


def configure():
    configure_db()
    configure_router()


configure()
