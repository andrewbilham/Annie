from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Supplier_Rate, Supplier_RateCreate, Supplier_RatePublic, Supplier_RatesPublic, Supplier_RateUpdate, Message

router = APIRouter()


@router.get("/", response_model=Supplier_RatesPublic)
def read_supplier_rate_rates(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve supplier_rate_rates.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Supplier_Rate)
        count = session.exec(count_statement).one()
        statement = select(Supplier_Rate).offset(skip).limit(limit)
        supplier_rate_rates = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Supplier_Rate)
            .where(Supplier_Rate.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Supplier_Rate)
            .where(Supplier_Rate.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        supplier_rate_rates = session.exec(statement).all()

    return Supplier_RatesPublic(data=supplier_rate_rates, count=count)


@router.get("/{id}", response_model=Supplier_RatePublic)
def read_supplier_rate_rate(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get supplier_rate_rate by ID.
    """
    supplier_rate_rate = session.get(Supplier_Rate, id)
    if not supplier_rate_rate:
        raise HTTPException(status_code=404, detail="Supplier_Rate not found")
    if not current_user.is_superuser and (supplier_rate_rate.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return supplier_rate_rate


@router.post("/", response_model=Supplier_RatePublic)
def create_supplier_rate_rate(
    *, session: SessionDep, current_user: CurrentUser, supplier_rate_in: Supplier_RateCreate
) -> Any:
    """
    Create new supplier_rate.
    """
    supplier_rate = Supplier_Rate.model_validate(supplier_rate_in, update={"owner_id": current_user.id})
    session.add(supplier_rate)
    session.commit()
    session.refresh(supplier_rate)
    return supplier_rate


@router.put("/{id}", response_model=Supplier_RatePublic)
def update_supplier_rate(
    *, session: SessionDep, current_user: CurrentUser, id: int, supplier_rate_in: Supplier_RateUpdate
) -> Any:
    """
    Update an supplier_rate.
    """
    supplier_rate = session.get(Supplier_Rate, id)
    if not supplier_rate:
        raise HTTPException(status_code=404, detail="Supplier_Rate not found")
    if not current_user.is_superuser and (supplier_rate.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = supplier_rate_in.model_dump(exclude_unset=True)
    supplier_rate.sqlmodel_update(update_dict)
    session.add(supplier_rate)
    session.commit()
    session.refresh(supplier_rate)
    return supplier_rate


@router.delete("/{id}")
def delete_supplier_rate(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an supplier_rate.
    """
    supplier_rate = session.get(Supplier_Rate, id)
    if not supplier_rate:
        raise HTTPException(status_code=404, detail="Supplier_Rate not found")
    if not current_user.is_superuser and (supplier_rate.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(supplier_rate)
    session.commit()
    return Message(message="Supplier_Rate deleted successfully")
