from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Referral_Allocation, Referral_AllocationCreate, Referral_AllocationPublic, Referral_AllocationsPublic, Referral_AllocationUpdate, Message

router = APIRouter()


@router.get("/", response_model=Referral_AllocationsPublic)
def read_referral_allocations(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve referral_allocations.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Referral_Allocation)
        count = session.exec(count_statement).one()
        statement = select(Referral_Allocation).offset(skip).limit(limit)
        referral_allocations = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Referral_Allocation)
            .where(Referral_Allocation.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Referral_Allocation)
            .where(Referral_Allocation.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        referral_allocations = session.exec(statement).all()

    return Referral_AllocationsPublic(data=referral_allocations, count=count)


@router.get("/{id}", response_model=Referral_AllocationPublic)
def read_referral_allocation(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get referral_allocation by ID.
    """
    referral_allocation = session.get(Referral_Allocation, id)
    if not referral_allocation:
        raise HTTPException(status_code=404, detail="Referral_Allocation not found")
    if not current_user.is_superuser and (referral_allocation.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return referral_allocation


@router.post("/", response_model=Referral_AllocationPublic)
def create_referral_allocation(
    *, session: SessionDep, current_user: CurrentUser, referral_allocation_in: Referral_AllocationCreate
) -> Any:
    """
    Create new referral_allocation.
    """
    referral_allocation = Referral_Allocation.model_validate(referral_allocation_in, update={"owner_id": current_user.id})
    session.add(referral_allocation)
    session.commit()
    session.refresh(referral_allocation)
    return referral_allocation


@router.put("/{id}", response_model=Referral_AllocationPublic)
def update_referral_allocation(
    *, session: SessionDep, current_user: CurrentUser, id: int, referral_allocation_in: Referral_AllocationUpdate
) -> Any:
    """
    Update an referral_allocation.
    """
    referral_allocation = session.get(Referral_Allocation, id)
    if not referral_allocation:
        raise HTTPException(status_code=404, detail="Referral_Allocation not found")
    if not current_user.is_superuser and (referral_allocation.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = referral_allocation_in.model_dump(exclude_unset=True)
    referral_allocation.sqlmodel_update(update_dict)
    session.add(referral_allocation)
    session.commit()
    session.refresh(referral_allocation)
    return referral_allocation


@router.delete("/{id}")
def delete_referral_allocation(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an referral_allocation.
    """
    referral_allocation = session.get(Referral_Allocation, id)
    if not referral_allocation:
        raise HTTPException(status_code=404, detail="Referral_Allocation not found")
    if not current_user.is_superuser and (referral_allocation.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(referral_allocation)
    session.commit()
    return Message(message="Referral_Allocation deleted successfully")
