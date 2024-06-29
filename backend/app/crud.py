from typing import Any

from sqlmodel import Session, select

from app.core.security import get_password_hash, verify_password
from app.models import Item, ItemCreate, User, UserCreate, UserUpdate, Source, SourceCreate, Supplier,SupplierCreate


def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def update_user(*, session: Session, db_user: User, user_in: UserUpdate) -> Any:
    user_data = user_in.model_dump(exclude_unset=True)
    extra_data = {}
    if "password" in user_data:
        password = user_data["password"]
        hashed_password = get_password_hash(password)
        extra_data["hashed_password"] = hashed_password
    db_user.sqlmodel_update(user_data, update=extra_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user_by_email(*, session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    session_user = session.exec(statement).first()
    return session_user


def authenticate(*, session: Session, email: str, password: str) -> User | None:
    db_user = get_user_by_email(session=session, email=email)
    if not db_user:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user


def create_item(*, session: Session, item_in: ItemCreate, owner_id: int) -> Item:
    db_item = Item.model_validate(item_in, update={"owner_id": owner_id})
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

def create_source(*, session: Session, source_in: SourceCreate, owner_id: int) -> Source:
    db_source = Source.model_validate(source_in, update={"owner_id": owner_id})
    session.add(db_source)
    session.commit()
    session.refresh(db_source)
    return db_source

def create_supplier(*, session: Session, supplier_in: SupplierCreate, owner_id: int) -> Supplier:
    db_supplier = Supplier.model_validate(supplier_in, update={"owner_id": owner_id})
    session.add(db_supplier)
    session.commit()
    session.refresh(db_supplier)
    return db_supplier

def create_claim(*, session: Session, claim_in: SupplierCreate, owner_id: int) -> Supplier:
    db_claim = Supplier.model_validate(claim_in, update={"owner_id": owner_id})
    session.add(db_claim)
    session.commit()
    session.refresh(db_claim)
    return db_claim

def create_authority(*, session: Session, authority_in: SupplierCreate, owner_id: int) -> Supplier:
    db_authority = Supplier.model_validate(authority_in, update={"owner_id": owner_id})
    session.add(db_authority)
    session.commit()
    session.refresh(db_authority)
    return db_authority    
    
def create_circs_group(*, session: Session, circs_group_in: SupplierCreate, owner_id: int) -> Supplier:
    db_circs_group = Supplier.model_validate(circs_group_in, update={"owner_id": owner_id})
    session.add(db_circs_group)
    session.commit()
    session.refresh(db_circs_group)
    return db_circs_group

def create_veh_group(*, session: Session, veh_group_in: SupplierCreate, owner_id: int) -> Supplier:
    db_veh_group = Supplier.model_validate(veh_group_in, update={"owner_id": owner_id})
    session.add(db_veh_group)
    session.commit()
    session.refresh(db_veh_group)
    return db_veh_group

def create_referrals_allocation(*, session: Session, referrals_allocation_in: SupplierCreate, owner_id: int) -> Supplier:
    db_referrals_allocation = Supplier.model_validate(referrals_allocation_in, update={"owner_id": owner_id})
    session.add(db_referrals_allocation)
    session.commit()
    session.refresh(db_referrals_allocation)
    return db_referrals_allocation

def create_source_rate(*, session: Session, source_rate_in: SupplierCreate, owner_id: int) -> Supplier:
    db_source_rate = Supplier.model_validate(source_rate_in, update={"owner_id": owner_id})
    session.add(db_source_rate)
    session.commit()
    session.refresh(db_source_rate)
    return db_source_rate

def create_supplier_rate(*, session: Session, supplier_rate_in: SupplierCreate, owner_id: int) -> Supplier:
    db_supplier_rate = Supplier.model_validate(supplier_rate_in, update={"owner_id": owner_id})
    session.add(db_supplier_rate)
    session.commit()
    session.refresh(db_supplier_rate)
    return db_supplier_rate

