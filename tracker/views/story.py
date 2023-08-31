from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from tracker.db.session import get_db
from tracker.serializers.story import StoryInput, StoryOutput
from tracker.services.story import create as create_story
from tracker.services.story import stories, story_by_id

router = APIRouter()


@router.post("/story", response_model=StoryOutput)
# trunk-ignore(ruff/B008)
def create(story: StoryInput, db: Session = Depends(get_db)):
    obj = create_story(db=db, story=story)

    if isinstance(obj, HTTPException):
        raise obj

    return obj


@router.get("/stories", response_model=list[StoryOutput])
# trunk-ignore(ruff/B008)
def get_stories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return stories(db=db, skip=skip, limit=limit)


@router.get("/story/{id}", response_model=StoryOutput)
# trunk-ignore(ruff/B008)
def get_story(id: int, db: Session = Depends(get_db)):
    obj = story_by_id(db=db, id=id)

    if isinstance(obj, HTTPException):
        raise obj

    return obj
