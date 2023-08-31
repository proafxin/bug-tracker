from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.orm import Session

from tracker.models.bug import Bug
from tracker.serializers.bug import BugInput, BugOutput
from tracker.services.story import story_by_id


def bug_not_created() -> HTTPException:
    return HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Bug not created.")


def bug_not_found(id: int) -> HTTPException:
    return HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail=f"Bug {id} not found."
    )


def bug_by_id(db: Session, id: int) -> BugOutput | HTTPException:
    bug = db.query(Bug).filter(Bug.id == id).first()

    if not bug:
        return bug_not_found(id=id)

    return bug


def bugs(db: Session, skip: int = 0, limit: int = 10) -> list[BugOutput]:
    return db.query(Bug).offset(offset=skip).limit(limit=limit).all()


def create(db: Session, bug: BugInput) -> BugOutput | HTTPException:
    story = story_by_id(db=db, id=bug.story_id)

    if isinstance(story, HTTPException):
        return bug_not_created()

    obj = Bug(title=bug.title, description=bug.description, story_id=bug.story_id)

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj
