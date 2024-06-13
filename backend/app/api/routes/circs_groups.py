from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Circs_Group, Circs_GroupCreate, Circs_GroupPublic, Circs_GroupsPublic, Circs_GroupUpdate, Message

router = APIRouter()


@router.get("/", response_model=Circs_GroupsPublic)
def read_circs_groups(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve circs_groups.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Circs_Group)
        count = session.exec(count_statement).one()
        statement = select(Circs_Group).offset(skip).limit(limit)
        circs_groups = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Circs_Group)
            .where(Circs_Group.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Circs_Group)
            .where(Circs_Group.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        circs_groups = session.exec(statement).all()

    return Circs_GroupsPublic(data=circs_groups, count=count)


@router.get("/{id}", response_model=Circs_GroupPublic)
def read_circs_group(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get circs_group by ID.
    """
    circs_group = session.get(Circs_Group, id)
    if not circs_group:
        raise HTTPException(status_code=404, detail="Circs_Group not found")
    if not current_user.is_superuser and (circs_group.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return circs_group


@router.post("/", response_model=Circs_GroupPublic)
def create_circs_group(
    *, session: SessionDep, current_user: CurrentUser, circs_group_in: Circs_GroupCreate
) -> Any:
    """
    Create new circs_group.
    """
    circs_group = Circs_Group.model_validate(circs_group_in, update={"owner_id": current_user.id})
    session.add(circs_group)
    session.commit()
    session.refresh(circs_group)
    return circs_group


@router.put("/{id}", response_model=Circs_GroupPublic)
def update_circs_group(
    *, session: SessionDep, current_user: CurrentUser, id: int, circs_group_in: Circs_GroupUpdate
) -> Any:
    """
    Update an circs_group.
    """
    circs_group = session.get(Circs_Group, id)
    if not circs_group:
        raise HTTPException(status_code=404, detail="Circs_Group not found")
    if not current_user.is_superuser and (circs_group.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = circs_group_in.model_dump(exclude_unset=True)
    circs_group.sqlmodel_update(update_dict)
    session.add(circs_group)
    session.commit()
    session.refresh(circs_group)
    return circs_group


@router.delete("/{id}")
def delete_circs_group(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an circs_group.
    """
    circs_group = session.get(Circs_Group, id)
    if not circs_group:
        raise HTTPException(status_code=404, detail="Circs_Group not found")
    if not current_user.is_superuser and (circs_group.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(circs_group)
    session.commit()
    return Message(message="Circs_Group deleted successfully")
