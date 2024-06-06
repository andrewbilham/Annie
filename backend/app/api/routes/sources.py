from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Source, SourceCreate, SourcePublic, SourcesPublic, SourceUpdate, Message

router = APIRouter()


@router.get("/", response_model=SourcesPublic)
def read_sources(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve sources.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Source)
        count = session.exec(count_statement).one()
        statement = select(Source).offset(skip).limit(limit)
        sources = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Source)
            .where(Source.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Source)
            .where(Source.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        sources = session.exec(statement).all()

    return SourcesPublic(data=sources, count=count)


@router.get("/{id}", response_model=SourcePublic)
def read_source(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get source by ID.
    """
    source = session.get(Source, id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    if not current_user.is_superuser and (source.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return source


@router.post("/", response_model=SourcePublic)
def create_source(
    *, session: SessionDep, current_user: CurrentUser, source_in: SourceCreate
) -> Any:
    """
    Create new source.
    """
    source = Source.model_validate(source_in, update={"owner_id": current_user.id})
    session.add(source)
    session.commit()
    session.refresh(source)
    return source


@router.put("/{id}", response_model=SourcePublic)
def update_source(
    *, session: SessionDep, current_user: CurrentUser, id: int, source_in: SourceUpdate
) -> Any:
    """
    Update an source.
    """
    source = session.get(Source, id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    if not current_user.is_superuser and (source.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = source_in.model_dump(exclude_unset=True)
    source.sqlmodel_update(update_dict)
    session.add(source)
    session.commit()
    session.refresh(source)
    return source


@router.delete("/{id}")
def delete_source(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an source.
    """
    source = session.get(Source, id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    if not current_user.is_superuser and (source.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(source)
    session.commit()
    return Message(message="Source deleted successfully")
