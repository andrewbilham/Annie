from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import Authority, AuthorityCreate, AuthorityPublic, AuthoritiesPublic, AuthorityUpdate, Message

router = APIRouter()


@router.get("/", response_model=AuthoritiesPublic)
def read_authorities(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve authorities.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Authority)
        count = session.exec(count_statement).one()
        statement = select(Authority).offset(skip).limit(limit)
        authorities = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Authority)
            .where(Authority.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Authority)
            .where(Authority.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        authorities = session.exec(statement).all()

    return AuthoritiesPublic(data=authorities, count=count)


@router.get("/{id}", response_model=AuthorityPublic)
def read_authority(session: SessionDep, current_user: CurrentUser, id: int) -> Any:
    """
    Get authority by ID.
    """
    authority = session.get(Authority, id)
    if not authority:
        raise HTTPException(status_code=404, detail="Authority not found")
    if not current_user.is_superuser and (authority.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return authority


@router.post("/", response_model=AuthorityPublic)
def create_authority(
    *, session: SessionDep, current_user: CurrentUser, authority_in: AuthorityCreate
) -> Any:
    """
    Create new authority.
    """
    authority = Authority.model_validate(authority_in, update={"owner_id": current_user.id})
    session.add(authority)
    session.commit()
    session.refresh(authority)
    
    return authority


@router.put("/{id}", response_model=AuthorityPublic)
def update_authority(
    *, session: SessionDep, current_user: CurrentUser, id: int, authority_in: AuthorityUpdate
) -> Any:
    """
    Update an authority.
    """
    authority = session.get(Authority, id)
    if not authority:
        raise HTTPException(status_code=404, detail="Authority not found")
    if not current_user.is_superuser and (authority.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = authority_in.model_dump(exclude_unset=True)
    authority.sqlmodel_update(update_dict)
    session.add(authority)
    session.commit()
    session.refresh(authority)
    return authority


@router.delete("/{id}")
def delete_authority(session: SessionDep, current_user: CurrentUser, id: int) -> Message:
    """
    Delete an authority.
    """
    authority = session.get(Authority, id)
    if not authority:
        raise HTTPException(status_code=404, detail="Authority not found")
    if not current_user.is_superuser and (authority.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(authority)
    session.commit()
    return Message(message="Authority deleted successfully")
