from http import HTTPStatus

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from tracker.models.bug import Bug
from tracker.serializers.bug import BugInput, BugOutput
from tracker.services.story import story_by_id


async def bug_not_created() -> HTTPException:
    return HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Bug not created.")


async def bug_by_id(db: AsyncSession, id: int) -> BugOutput | HTTPException:
    query = await db.execute(select(Bug).filter(Bug.id == id))
    res = query.scalars().all()

    if len(res) > 0:
        return res[0]

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND)


def bug_output(bug: Bug) -> BugOutput:
    story = jsonable_encoder(obj=bug.story)
    bug_output = BugOutput(
        id=bug.id,
        title=bug.title,
        description=bug.description,
        story=story,
        story_id=bug.story_id,
        created_at=bug.created_at,
        updated_at=bug.updated_at,
    )

    return bug_output


async def bugs(db: AsyncSession, skip: int = 0, limit: int = 10) -> list[BugOutput]:
    bugs = await db.scalars(select(Bug).offset(offset=skip).limit(limit=limit))
    output = []

    for bug in bugs:
        output.append(bug_output(bug=bug))

    return output


async def create(db: AsyncSession, bug: BugInput) -> BugOutput:
    story = await story_by_id(db=db, id=bug.story_id)

    obj = Bug(**bug.model_dump(), story=story)

    db.add(obj)
    await db.commit()
    await db.refresh(obj)

    if isinstance(obj, Bug):
        return await bug_output(bug=obj)

    return bug_not_created()
