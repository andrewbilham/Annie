from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Veh_Group, Veh_GroupCreate, Veh_GroupPublic, Veh_GroupsPublic, Veh_GroupUpdate, Message

router = APIRouter()


@router.get("/", response_model=Veh_GroupsPublic)
def read_veh_groups(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve veh_groups.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Veh_Group)
        count = session.exec(count_statement).one()
        statement = select(Veh_Group).offset(skip).limit(limit)
        veh_groups = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Veh_Group)
            .where(Veh_Group.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Veh_Group)
            .where(Veh_Group.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        veh_groups = session.exec(statement).all()

    return Veh_GroupsPublic(data=veh_groups, count=count)


@router.get("/{id}", response_model=Veh_GroupPublic)
def read_veh_group(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get veh_group by ID.
    """
    veh_group = session.get(Veh_Group, id)
    if not veh_group:
        raise HTTPException(status_code=404, detail="Veh_Group not found")
    if not current_user.is_superuser and (veh_group.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return veh_group


@router.post("/", response_model=Veh_GroupPublic)
def create_veh_group(
    *, session: SessionDep, current_user: CurrentUser, veh_group_in: Veh_GroupCreate
) -> Any:
    """
    Create new veh_group.
    """
    veh_group = Veh_Group.model_validate(veh_group_in, update={"owner_id": current_user.id})
    session.add(veh_group)
    session.commit()
    session.refresh(veh_group)
    return veh_group


@router.put("/{id}", response_model=Veh_GroupPublic)
def update_veh_group(
    *, session: SessionDep, current_user: CurrentUser, id: int, veh_group_in: Veh_GroupUpdate
) -> Any:
    """
    Update an veh_group.
    """
    veh_group = session.get(Veh_Group, id)
    if not veh_group:
        raise HTTPException(status_code=404, detail="Veh_Group not found")
    if not current_user.is_superuser and (veh_group.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = veh_group_in.model_dump(exclude_unset=True)
    veh_group.sqlmodel_update(update_dict)
    session.add(veh_group)
    session.commit()
    session.refresh(veh_group)
    return veh_group


@router.delete("/{id}")
def delete_veh_group(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an veh_group.
    """
    veh_group = session.get(Veh_Group, id)
    if not veh_group:
        raise HTTPException(status_code=404, detail="Veh_Group not found")
    if not current_user.is_superuser and (veh_group.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(veh_group)
    session.commit()
    return Message(message="Veh_Group deleted successfully")
