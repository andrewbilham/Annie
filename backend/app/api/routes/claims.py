from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Claim, ClaimCreate, ClaimPublic, ClaimsPublic, ClaimUpdate, Message

router = APIRouter()


@router.get("/", response_model=ClaimsPublic)
def read_claims(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve claims.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Claim)
        count = session.exec(count_statement).one()
        statement = select(Claim).offset(skip).limit(limit)
        claims = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Claim)
            .where(Claim.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Claim)
            .where(Claim.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        claims = session.exec(statement).all()

    return ClaimsPublic(data=claims, count=count)


@router.get("/{id}", response_model=ClaimPublic)
def read_claim(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get claim by ID.
    """
    claim = session.get(Claim, id)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    if not current_user.is_superuser and (claim.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return claim


@router.post("/", response_model=ClaimPublic)
def create_claim(
    *, session: SessionDep, current_user: CurrentUser, claim_in: ClaimCreate
) -> Any:
    """
    Create new claim.
    """
    claim = Claim.model_validate(claim_in, update={"owner_id": current_user.id})
    session.add(claim)
    session.commit()
    session.refresh(claim)
    return claim


@router.put("/{id}", response_model=ClaimPublic)
def update_claim(
    *, session: SessionDep, current_user: CurrentUser, id: int, claim_in: ClaimUpdate
) -> Any:
    """
    Update an claim.
    """
    claim = session.get(Claim, id)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    if not current_user.is_superuser and (claim.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = claim_in.model_dump(exclude_unset=True)
    claim.sqlmodel_update(update_dict)
    session.add(claim)
    session.commit()
    session.refresh(claim)
    return claim


@router.delete("/{id}")
def delete_claim(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an claim.
    """
    claim = session.get(Claim, id)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    if not current_user.is_superuser and (claim.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(claim)
    session.commit()
    return Message(message="Claim deleted successfully")
