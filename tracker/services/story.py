from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.orm import Session

from tracker.models.story import Story
from tracker.serializers.story import StoryInput, StoryOutput


def story_not_found(story_id: int) -> HTTPException:
    return HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail=f"Story {story_id} not found."
    )


def stories(db: Session, skip: int = 0, limit: int = 10) -> list[StoryOutput]:
    return db.query(Story).offset(offset=skip).limit(limit=limit).all()


def story_by_id(db: Session, id: int) -> StoryOutput | HTTPException:
    story = db.query(Story).filter(Story.id == id).first()

    if not story:
        return story_not_found(story_id=id)

    return story


def create(db: Session, story: StoryInput) -> StoryOutput:
    story_new = Story(name=story.name)

    db.add(story_new)
    db.commit()
    db.refresh(story_new)

    return story_new
