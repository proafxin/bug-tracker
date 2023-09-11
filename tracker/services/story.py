from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from tracker.models.story import Story
from tracker.serializers.story import StoryInput, StoryOutput


async def stories(
    db: AsyncSession, skip: int = 0, limit: int = 10
) -> list[StoryOutput]:
    query = await db.execute(select(Story).offset(skip).limit(limit=limit))

    return query.scalars().all()


async def story_by_id(db: AsyncSession, id: int) -> StoryOutput | HTTPException:
    query = await db.execute(select(Story).where(Story.id == id))
    story = query.scalars().first()

    if isinstance(story, Story):
        return story

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND)


async def create(db: AsyncSession, story: StoryInput) -> StoryOutput:
    story_new = Story(name=story.name)

    db.add(story_new)
    await db.commit()
    await db.refresh(story_new)

    return story_new
