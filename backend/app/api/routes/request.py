from typing import Any
import random

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select, desc, asc

from app.api.deps import CurrentUser, SessionDep
from app.models import Referral, RequestCreate, Claim,Supplier_Stat

router = APIRouter()



@router.post("/")
def create_request(
    *, session: SessionDep, current_user: CurrentUser, request_in: RequestCreate
) -> Any:
    """

    Create new request.
    """

    #### ADD CLAIM ####
    claim = Claim.model_validate(request_in, 
                                update={"owner_id": current_user.id,
                                "circs_grade_id" : random.randint(1,3),
                                "veh_group_id" : random.randint(1,2)} )

    session.add(claim)
    session.commit()
    session.refresh(claim)

    #### ADD Referral ####
    referral = Referral.model_validate(request_in, 
                                       update={"owner_id": current_user.id,
                                       "circs_group_id" : random.randint(1,3),
                                       "veh_group_id" : random.randint(1,2),
                                       "claim_id": claim.id})

    session.add(referral)
    session.commit()
    session.refresh(referral)

    # Create the initial select statement
    statement = select(Supplier_Stat).limit(1).order_by(desc(Supplier_Stat.total_rank))

    # Conditionally add the WHERE clause
    if referral.authority_id is not None:
        statement = statement.where(Supplier_Stat.authority_id == referral.authority_id)
    # Conditionally add the WHERE clause
    if referral.circs_group_id is not None:
        statement = statement.where(Supplier_Stat.circs_group_id == referral.circs_group_id)
    # Conditionally add the WHERE clause
    if referral.veh_group_id is None:
        statement = statement.where(Supplier_Stat.veh_group_id == referral.veh_group_id)
    final_query_text = str(statement)

    supplier = session.exec(statement).one()

    


    return {"Referral ID": referral.id, 
            "Supplier": supplier,
            "query": print(final_query_text),
            "Circs_grade":referral.circs_group_id}
