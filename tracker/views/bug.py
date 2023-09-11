from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from tracker.db.session import get_db
from tracker.serializers.bug import BugInput, BugOutput
from tracker.services.bug import bug_by_id, bugs
from tracker.services.bug import create as create_bug

router = APIRouter()


@router.post("/bugs/", response_model=BugOutput)
# trunk-ignore(ruff/B008)
async def create(bug: BugInput, db: Session = Depends(get_db)):
    obj = await create_bug(db=db, bug=bug)

    if isinstance(obj, HTTPException):
        raise obj

    return obj


@router.get("/bugs/", response_model=list[BugOutput])
# trunk-ignore(ruff/B008)
async def get(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await bugs(db=db, skip=skip, limit=limit)


@router.get("/bugs/{id}", response_model=BugOutput)
# trunk-ignore(ruff/B008)
async def get_bug(id: int, db: Session = Depends(get_db)):
    obj = await bug_by_id(db=db, id=id)

    if isinstance(obj, HTTPException):
        raise obj

    return obj
