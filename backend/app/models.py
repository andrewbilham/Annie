from sqlmodel import Field, Relationship, SQLModel 
from datetime import datetime, date, time
import sqlalchemy as sa


##### users
# Shared properties
# TODO replace email str with EmailStr when sqlmodel supports it
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# TODO replace email str with EmailStr when sqlmodel supports it
class UserRegister(SQLModel):
    email: str
    password: str
    full_name: str | None = None


# Properties to receive via API on update, all are optional
# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdate(UserBase):
    email: str | None = None  # type: ignore
    password: str | None = None


# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdateMe(SQLModel):
    full_name: str | None = None
    email: str | None = None


class UpdatePassword(SQLModel):
    current_password: str
    new_password: str


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )
    items: list["Item"] = Relationship(back_populates="owner")
    sources: list["Source"] = Relationship(back_populates="owner")
    suppliers: list["Supplier"] = Relationship(back_populates="owner")
    claims: list["Claim"] = Relationship(back_populates="owner")
    authorities: list["Authority"] = Relationship(back_populates="owner")
    circs_groups: list["Circs_Group"] = Relationship(back_populates="owner")
    veh_groups: list["Veh_Group"] = Relationship(back_populates="owner")
    supplier_rates: list["Supplier_Rate"] = Relationship(back_populates="owner")
    source_rates: list["Source_Rate"] = Relationship(back_populates="owner")
    referrals: list["Referral"] = Relationship(back_populates="owner")
    referral_allocations: list["Referral_Allocation"] = Relationship(back_populates="owner")



# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: int


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int

######## items

# Shared properties
class ItemBase(SQLModel):
    title: str
    description: str | None = None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str


# Properties to receive on item update
class ItemUpdate(ItemBase):
    title: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="items")
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )


# Properties to return via API, id is always required
class ItemPublic(ItemBase):
    id: int
    owner_id: int


class ItemsPublic(SQLModel):
    data: list[ItemPublic]
    count: int

 ####### sources #######


# Shared properties
class SourceBase(SQLModel):
    source_name: str


# Properties to receive on source creation
class SourceCreate(SourceBase):
    source_name: str


# Properties to receive on source update
class SourceUpdate(SourceBase):
    source_name: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Source(SourceBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    source_name: str
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="sources")
  ##  referrals: list["Referral"] = Relationship(back_populates="source")
    source_rates: list["Source_Rate"] = Relationship(back_populates="source")
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )


# Properties to return via API, id is always required
class SourcePublic(SourceBase):
    id: int
    owner_id: int


class SourcesPublic(SQLModel):
    data: list[SourcePublic]
    count: int 

 ####### Suppliers #######


# Shared properties
class SupplierBase(SQLModel):
        name: str


# Properties to receive on source creation
class SupplierCreate(SupplierBase):
    name: str


# Properties to receive on source update
class SupplierUpdate(SupplierBase):
    name: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Supplier(SupplierBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="suppliers")
    referrals: list["Referral"] = Relationship(back_populates="supplier")
    referral_allocations: list["Referral_Allocation"] = Relationship(back_populates="supplier")
    name: str | None = None
    address_1: str | None = None
    address_town: str | None = None
    address_postcode: str | None = None
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )

    Email: str | None = None
    Tel: int | None = None


# Properties to return via API, id is always required
class SupplierPublic(SupplierBase):
    id: int
    owner_id: int


class SuppliersPublic(SQLModel):
    data: list[SupplierPublic]
    count: int 


######## Claim


 # Shared properties
class ClaimBase(SQLModel):
    client_firstname: str
    client_lastname: str
    authority_id: int
    
    

# Properties to receive on claim creation
class ClaimCreate(ClaimBase):
    client_firstname: str
    client_lastname: str


# Properties to receive on claim update
class ClaimUpdate(ClaimBase):
    client_firstname: str | None = None  # type: ignore
    client_lastname: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Claim(ClaimBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="claims")
    ##referrals: list["Referral"] = Relationship(back_populates="claim")
    client_firstname: str | None = None
    client_lastname: str | None = None
    client_address_1: str | None = None
    client_address_town: str | None = None
    client_address_postcode: str | None = None
    client_vehicle_reg: str | None = None
    client_insurer: str | None = None
    client_insurer_policyno: str | None = None
    client_phone: str | None = None
    client_mobile: str | None = None
    client_email: str | None = None
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )
    authority_id: int | None = Field(default=None, foreign_key="authority.id", nullable=False)
    plate_type: str | None = None
    accident_date: date | None = None
    accident_time: time | None = None
    accident_location: str | None = None
    accident_circs: str | None = None
    tp_firstname: str | None = None
    tp_lastname: str | None = None
    tp_address_1: str | None = None
    tp_address_town: str | None = None
    tp_address_postcode: str | None = None
    tp_vehicle_reg: str | None = None
    tp_insurer: str | None = None
    tp_insurer_polcyno: str | None = None
    tp_phone: str | None = None
    tp_mobile: str | None = None



# Properties to return via API, id is always required
class ClaimPublic(ClaimBase):
    id: int
    
    

class ClaimsPublic(SQLModel):
    data: list[ClaimPublic]
    count: int  


######## Authority


# Shared properties
class AuthorityBase(SQLModel):
    name: str


# Properties to receive on authority creation
class AuthorityCreate(AuthorityBase):
    name: str


# Properties to receive on authority update
class AuthorityUpdate(AuthorityBase):
    name: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Authority(AuthorityBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="authorities")
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )
    name: str | None = None




# Properties to return via API, id is always required
class AuthorityPublic(AuthorityBase):
    id: int
    owner_id: int
    


class AuthoritiesPublic(SQLModel):
    data: list[AuthorityPublic]
    count: int 


    ######## Circs_Group


# Shared properties
class Circs_GroupBase(SQLModel):
    group: str
    desc: str


# Properties to receive on circs_group creation
class Circs_GroupCreate(Circs_GroupBase):
    group: str
    desc: str


# Properties to receive on circs_group update
class Circs_GroupUpdate(Circs_GroupBase):
    group: str | None = None  # type: ignore
    desc: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Circs_Group(Circs_GroupBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="circs_groups")
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )
    group: str | None = None
    desc: str | None = None


# Properties to return via API, id is always required
class Circs_GroupPublic(Circs_GroupBase):
    id: int
    owner_id: int
    


class Circs_GroupsPublic(SQLModel):
    data: list[Circs_GroupPublic]
    count: int 


######## Veh_Group


# Shared properties
class Veh_GroupBase(SQLModel):
    group: str
    desc: str


# Properties to receive on veh_group creation
class Veh_GroupCreate(Veh_GroupBase):
    group: str
    desc: str


# Properties to receive on veh_group update
class Veh_GroupUpdate(Veh_GroupBase):
    group: str | None = None  # type: ignore
    desc: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Veh_Group(Veh_GroupBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="veh_groups")
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )
    group: str | None = None
    desc: str | None = None


# Properties to return via API, id is always required
class Veh_GroupPublic(Veh_GroupBase):
    id: int
    owner_id: int


class Veh_GroupsPublic(SQLModel):
    data: list[Veh_GroupPublic]
    count: int 

######## Supplier_Rate


# Shared properties
class Supplier_RateBase(SQLModel):
    rate: float


# Properties to receive on supplier_rate creation
class Supplier_RateCreate(Supplier_RateBase):
    rate: float


# Properties to receive on supplier_rate update
class Supplier_RateUpdate(Supplier_RateBase):
    rate: float | None = None  # type: ignore


# Database model, database table inferred from class name
class Supplier_Rate(Supplier_RateBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="supplier_rates")
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )
    authority_id: int | None = Field(default=None, foreign_key="authority.id", nullable=False)
    plate_type: str | None = None
    veh_group_id: int | None = Field(default=None, foreign_key="veh_group.id", nullable=False)
    circs_group_id: int | None = Field(default=None, foreign_key="circs_group.id", nullable=False)
    type: str | None = None
    rate: float | None = None
    hire_length: int | None = None
    supplier_id: int | None = Field(default=None, foreign_key="supplier.id", nullable=False)



# Properties to return via API, id is always required
class Supplier_RatePublic(Supplier_RateBase):
    id: int
    owner_id: int


class Supplier_RatesPublic(SQLModel):
    data: list[Supplier_RatePublic]
    count: int 



    ######## Referral


# Shared properties
class ReferralBase(SQLModel):
    source_id: int
    claim_id: int


# Properties to receive on referral creation
class ReferralCreate(ReferralBase):
    source_id: int
    claim_id: int


# Properties to receive on referral update
class ReferralUpdate(ReferralBase):
    source_id: int | None = None  # type: ignore


# Database model, database table inferred from class name
class Referral(ReferralBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="referrals")
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )
    source_id: int | None = Field(default=None, foreign_key="source.id", nullable=False)
    ##source: Source | None = Relationship(back_populates="referrals")
    claim_id: int | None = Field(default=None, foreign_key="claim.id", nullable=False)
    ##claim: Claim | None = Relationship(back_populates="referrals")
    supplier_id: int  | None = Field(default=None, foreign_key="supplier.id", nullable=True)
    supplier: Supplier | None = Relationship(back_populates="referrals")
    type: str | None = None
    referral_allocations: list["Referral_Allocation"] = Relationship(back_populates="referral")



# Properties to return via API, id is always required
class ReferralPublic(ReferralBase):
    id: int
    owner_id: int
    source_id: int



class ReferralsPublic(SQLModel):
    data: list[ReferralPublic]
    count: int 



    ######## Referral_Allocation


# Shared properties
class Referral_AllocationBase(SQLModel):
    Source: str


# Properties to receive on referral_allocation creation
class Referral_AllocationCreate(Referral_AllocationBase):
    Source: str


# Properties to receive on referral_allocation update
class Referral_AllocationUpdate(Referral_AllocationBase):
    Source: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Referral_Allocation(Referral_AllocationBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="referral_allocations")
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )
    supplier_id: int | None = Field(default=None, foreign_key="supplier.id", nullable=False)
    supplier: Supplier | None = Relationship(back_populates="referral_allocations")
    referral_id: int | None = Field(default=None, foreign_key="referral.id", nullable=False)
    referral: Referral | None = Relationship(back_populates="referral_allocations")
    sentdate: datetime | None = None
    status: str | None = None
    responsedate: datetime | None = None




# Properties to return via API, id is always required
class Referral_AllocationPublic(Referral_AllocationBase):
    id: int
    owner_id: int


class Referral_AllocationsPublic(SQLModel):
    data: list[Referral_AllocationPublic]
    count: int 


######## Source_Rates


# Shared properties
class Source_RateBase(SQLModel):
    rate: float


# Properties to receive on source_rate creation
class Source_RateCreate(Source_RateBase):
    rate: float


# Properties to receive on source_rate update
class Source_RateUpdate(Source_RateBase):
    rate: float | None = None  # type: ignore


# Database model, database table inferred from class name
class Source_Rate(Source_RateBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="source_rates")
    created_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )
    updated_datetime: datetime | None = Field(
        default=None,
        sa_type= sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )
    authority_id: int | None = Field(default=None, foreign_key="authority.id", nullable=False)
    plate_type: str | None = None
    veh_group_id: int | None = Field(default=None, foreign_key="veh_group.id", nullable=False)
    circs_group_id: int | None = Field(default=None, foreign_key="circs_group.id", nullable=False)
    type: str | None = None
    rate: float | None = None
    hire_length: int | None = None
    source_id: int | None = Field(default=None, foreign_key="source.id", nullable=False)
    source: Source | None = Relationship(back_populates="source_rates")



# Properties to return via API, id is always required
class Source_RatePublic(Source_RateBase):
    id: int
    owner_id: int


class Source_RatesPublic(SQLModel):
    data: list[Source_RatePublic]
    count: int 




class RequestBase(SQLModel):
    type : str
    source_id: int
    client_firstname : str
    client_lastname : str
    authority_id : int

class RequestCreate(SQLModel):
    type : str
    source_id: int
    client_firstname : str
    client_lastname : str
    authority_id : int




# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: int | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str
