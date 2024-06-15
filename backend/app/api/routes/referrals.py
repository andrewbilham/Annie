from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Referral, ReferralCreate, ReferralPublic, ReferralsPublic, ReferralUpdate, Message, \
                        Source

router = APIRouter()


@router.get("/", response_model=ReferralsPublic)
def read_referrals(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve referrals.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Referral)
        count = session.exec(count_statement).one()
        statement = select(Referral).offset(skip).limit(limit)
        referrals = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Referral)
            .where(Referral.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Referral)
            .where(Referral.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        referrals = session.exec(statement).all()

    return ReferralsPublic(data=referrals, count=count)


@router.get("/{id}", response_model=ReferralPublic)
def read_referral(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get referral by ID.
    """
    referral = session.get(Referral, id)
    if not referral:
        raise HTTPException(status_code=404, detail="Referral not found")
    if not current_user.is_superuser and (referral.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return referral


@router.post("/", response_model=ReferralPublic)
def create_referral(
    *, session: SessionDep, current_user: CurrentUser, referral_in: ReferralCreate
) -> Any:
    """
    Create new referral.
    """

    source = session.get(Source, referral_in.source_id)   

    referral = Referral.model_validate(referral_in, update={"owner_id": current_user.id})
    session.add(referral)
    session.commit()
    session.refresh(referral)
    return referral


@router.put("/{id}", response_model=ReferralPublic)
def update_referral(
    *, session: SessionDep, current_user: CurrentUser, id: int, referral_in: ReferralUpdate
) -> Any:
    """
    Update an referral.
    """
    referral = session.get(Referral, id)
    if not referral:
        raise HTTPException(status_code=404, detail="Referral not found")
    if not current_user.is_superuser and (referral.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = referral_in.model_dump(exclude_unset=True)
    referral.sqlmodel_update(update_dict)
    session.add(referral)
    session.commit()
    session.refresh(referral)
    return referral


@router.delete("/{id}")
def delete_referral(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an referral.
    """
    referral = session.get(Referral, id)
    if not referral:
        raise HTTPException(status_code=404, detail="Referral not found")
    if not current_user.is_superuser and (referral.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(referral)
    session.commit()
    return Message(message="Referral deleted successfully")
