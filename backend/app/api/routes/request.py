from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Referral, RequestCreate

router = APIRouter()



@router.post("/")
def create_referral(
    *, session: SessionDep, current_user: CurrentUser, request_in: RequestCreate
) -> Any:
    """
    Create new request.
    """

    claim = Claim(client_firstname = request_in.client_firstname, client_lastname = request_in.client_lastname,authority_id = request_in.authority_id, owner_id = current_user.id )

    session.add(claim)
    session.commit()
    session.refresh(claim)

    referral = Referral(claim_id = claim.id, type = request_in.type, source_id = request_in.source_id, owner_id = current_user.id )

    session.add(referral)
    session.commit()
    session.refresh(referral)

    return {"claim": claim.id, "referral": referral.id}

