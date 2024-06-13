from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Source_Rate, Source_RateCreate, Source_RatePublic, Source_RatesPublic, Source_RateUpdate, Message

router = APIRouter()


@router.get("/", response_model=Source_RatesPublic)
def read_source_rate_rates(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve source_rate_rates.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Source_Rate)
        count = session.exec(count_statement).one()
        statement = select(Source_Rate).offset(skip).limit(limit)
        source_rate_rates = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Source_Rate)
            .where(Source_Rate.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Source_Rate)
            .where(Source_Rate.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        source_rate_rates = session.exec(statement).all()

    return Source_RatesPublic(data=source_rate_rates, count=count)


@router.get("/{id}", response_model=Source_RatePublic)
def read_source_rate_rate(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get source_rate_rate by ID.
    """
    source_rate_rate = session.get(Source_Rate, id)
    if not source_rate_rate:
        raise HTTPException(status_code=404, detail="Source_Rate not found")
    if not current_user.is_superuser and (source_rate_rate.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return source_rate_rate


@router.post("/", response_model=Source_RatePublic)
def create_source_rate_rate(
    *, session: SessionDep, current_user: CurrentUser, source_rate_in: Source_RateCreate
) -> Any:
    """
    Create new source_rate.
    """
    source_rate = Source_Rate.model_validate(source_rate_in, update={"owner_id": current_user.id})
    session.add(source_rate)
    session.commit()
    session.refresh(source_rate)
    return source_rate


@router.put("/{id}", response_model=Source_RatePublic)
def update_source_rate(
    *, session: SessionDep, current_user: CurrentUser, id: int, source_rate_in: Source_RateUpdate
) -> Any:
    """
    Update an source_rate.
    """
    source_rate = session.get(Source_Rate, id)
    if not source_rate:
        raise HTTPException(status_code=404, detail="Source_Rate not found")
    if not current_user.is_superuser and (source_rate.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = source_rate_in.model_dump(exclude_unset=True)
    source_rate.sqlmodel_update(update_dict)
    session.add(source_rate)
    session.commit()
    session.refresh(source_rate)
    return source_rate


@router.delete("/{id}")
def delete_source_rate(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an source_rate.
    """
    source_rate = session.get(Source_Rate, id)
    if not source_rate:
        raise HTTPException(status_code=404, detail="Source_Rate not found")
    if not current_user.is_superuser and (source_rate.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(source_rate)
    session.commit()
    return Message(message="Source_Rate deleted successfully")
