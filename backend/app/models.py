from sqlmodel import Field, Relationship, SQLModel,UniqueConstraint
from pydantic import EmailStr
from datetime import datetime, date, time
import sqlalchemy as sa
from typing import Optional

class CreatedModifiedBase():
        created_datetime: datetime | None = Field(
            default=None,
            sa_type= sa.DateTime(timezone=True),
            sa_column_kwargs={"server_default": sa.func.now()},
            nullable=False,
        )
        updated_datetime: datetime | None = Field(
            default=None,
            sa_type= sa.DateTime(timezone=True),
            sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()}
        )
       

##### users
    # Shared properties
    # TODO replace email str with EmailStr when sqlmodel supports it
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserRegister(SQLModel):
    email: str = Field(max_length=255)
    password: str = Field(min_length=8, max_length=40)
    full_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on update, all are optional
class UserUpdate(UserBase):
    email: str | None = Field(default=None, max_length=255)  # type: ignore
    password: str | None = Field(default=None, min_length=8, max_length=40)


class UserUpdateMe(SQLModel):
    full_name: str | None = Field(default=None, max_length=255)
    email: str | None = Field(default=None, max_length=255)


class UpdatePassword(SQLModel):
    current_password: str = Field(min_length=8, max_length=40)
    new_password: str = Field(min_length=8, max_length=40)


# Database model, database table inferred from class name
class User(UserBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        hashed_password: str
        assigned_source_id: int | None = Field(default=None, foreign_key="source.id", nullable=True)
        items: list["Item"] = Relationship(back_populates="owner")
        ##sources: list["Source"] = Relationship(back_populates="owner")
        suppliers: list["Supplier"] = Relationship(back_populates="owner")
        claims: list["Claim"] = Relationship(back_populates="owner")
        authorities: list["Authority"] = Relationship(back_populates="owner")
        circs_groups: list["Circs_Group"] = Relationship(back_populates="owner")
        veh_groups: list["Veh_Group"] = Relationship(back_populates="owner")
        supplier_rates: list["Supplier_Rate"] = Relationship(back_populates="owner")
        source_rates: list["Source_Rate"] = Relationship(back_populates="owner")
        referrals: list["Referral"] = Relationship(back_populates="owner")
        referral_allocations: list["Referral_Allocation"] = Relationship(back_populates="owner")
        supplier_stats: list["Supplier_Stat"] = Relationship(back_populates="owner")
        source: Optional["Source"] = Relationship(sa_relationship_kwargs={"foreign_keys": "User.assigned_source_id"})




# Properties to return via API, id is always required
class UserPublic(UserBase):
        id: int


class UsersPublic(SQLModel):
        data: list[UserPublic]
        count: int

########################################## items #####################################################

# Shared properties
class ItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str = Field(min_length=1, max_length=255)


# Properties to receive on item update
class ItemUpdate(ItemBase):
    title: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


# Database model, database table inferred from class name
class Item(ItemBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        title: str = Field(max_length=255)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        owner: User | None = Relationship(back_populates="items")


# Properties to return via API, id is always required
class ItemPublic(ItemBase):
        id: int
        owner_id: int


class ItemsPublic(SQLModel):
        data: list[ItemPublic]
        count: int

 ########################################## sources #######


# Shared properties
class SourceBase(SQLModel):
        source_name: str


# Properties to receive on source creation
class SourceCreate(SourceBase):
        pass


# Properties to receive on source update
class SourceUpdate(SourceBase):
        source_name: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Source(SourceBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        referrals: list["Referral"] = Relationship(back_populates="source")


# Properties to return via API, id is always required
class SourcePublic(SourceBase):
        id: int
        source_name: str


class SourcesPublic(SQLModel):
        data: list[SourcePublic]
        count: int 

 ####### Suppliers #######


# Shared properties
class SupplierBase(SQLModel):
        name: str 
        address_1: str | None = None
        address_town: str | None = None
        address_postcode: str | None = None
        base_rate: float
        Email: str | None = None
        Tel: int | None = None


# Properties to receive on source creation
class SupplierCreate(SupplierBase):
        pass


# Properties to receive on source update
class SupplierUpdate(SupplierBase):
        name: str | None = None
        base_rate: float | None = None


# Database model, database table inferred from class name
class Supplier(SupplierBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        owner: User | None = Relationship(back_populates="suppliers")
        supplier_stats: list["Supplier_Stat"] = Relationship(back_populates="supplier")

# Properties to return via API, id is always required
class SupplierPublic(SupplierBase):
        id: int


class SuppliersPublic(SQLModel):
        data: list[SupplierPublic]
        count: int 


######## Claim


 # Shared properties
class ClaimBase(SQLModel):
        client_firstname: str 
        client_lastname: str 
        client_address_1: str | None = None
        client_address_town: str | None = None
        client_address_postcode: str | None = None
        client_vehicle_reg: str | None = None
        client_insurer: str | None = None
        client_insurer_policyno: str | None = None
        client_phone: str | None = None
        client_mobile: str | None = None
        client_email: str | None = None
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
        
    

# Properties to receive on claim creation
class ClaimCreate(ClaimBase):
        pass


# Properties to receive on claim update
class ClaimUpdate(ClaimBase):
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
        authority_id: int | None = None
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


# Database model, database table inferred from class name
class Claim(ClaimBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        owner: User | None = Relationship(back_populates="claims")



# Properties to return via API, id is always required
class ClaimPublic(ClaimBase):
        id: int
    
    

class ClaimsPublic(SQLModel):
        data: list[ClaimPublic]
        count: int  


######## Authority


# Shared properties
class AuthorityBase(SQLModel):
        name: str | None = None


# Properties to receive on authority creation
class AuthorityCreate(AuthorityBase):
        pass


# Properties to receive on authority update
class AuthorityUpdate(AuthorityBase):
        name: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Authority(AuthorityBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        owner: User | None = Relationship(back_populates="authorities")
    

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
class Circs_Group(Circs_GroupBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        owner: User | None = Relationship(back_populates="circs_groups")


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
        group: str | None = None
        desc: str | None = None


# Properties to receive on veh_group creation
class Veh_GroupCreate(Veh_GroupBase):
        pass


# Properties to receive on veh_group update
class Veh_GroupUpdate(Veh_GroupBase):
        group: str | None = None  # type: ignore
        desc: str | None = None  # type: ignore


# Database model, database table inferred from class name
class Veh_Group(Veh_GroupBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        owner: User | None = Relationship(back_populates="veh_groups")



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
        authority_id: int | None = Field(default=None, foreign_key="authority.id", nullable=False)
        plate_type: str | None = None
        veh_group_id: int | None = Field(default=None, foreign_key="veh_group.id", nullable=False)
        circs_group_id: int | None = Field(default=None, foreign_key="circs_group.id", nullable=False)
        type: str | None = None
        rate: float | None = None
        hire_length: int | None = None
        supplier_id: int | None = Field(default=None, foreign_key="supplier.id", nullable=False)
        


# Properties to receive on supplier_rate creation
class Supplier_RateCreate(Supplier_RateBase):
        pass


# Properties to receive on supplier_rate update
class Supplier_RateUpdate(Supplier_RateBase):
        authority_id: int | None = None
        plate_type: str | None = None
        veh_group_id: int | None = None
        circs_group_id: int | None = None
        type: str | None = None
        rate: float | None = None
        hire_length: int | None = None
        supplier_id: int | None = None


# Database model, database table inferred from class name
class Supplier_Rate(Supplier_RateBase, CreatedModifiedBase,table=True):
        __table_args__ = (
            UniqueConstraint("authority_id", "veh_group_id", "circs_group_id","supplier_id", name="supplier_rate_constraint"),
        )
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        owner: User | None = Relationship(back_populates="supplier_rates")
        rate_override: str | None = Field(default = 'No', sa_column_kwargs={"server_default": "No"})



# Properties to return via API, id is always required
class Supplier_RatePublic(Supplier_RateBase):
        id: int
        owner_id: int


class Supplier_RatesPublic(SQLModel):
        data: list[Supplier_RatePublic]
        count: int 



#################################### Referral ############################################


# Shared properties
class ReferralBase(SQLModel):
        source_id: int | None = Field(default=None, foreign_key="source.id", nullable=False)
        claim_id: int | None = Field(default=None, foreign_key="claim.id", nullable=False)
        supplier_id: int  | None = Field(default=None, foreign_key="supplier.id", nullable=True)
        type: str | None = None
        authority_id: int  | None = Field(default=None, foreign_key="authority.id", nullable=True)


# Properties to receive on referral creation
class ReferralCreate(ReferralBase):
        pass


# Properties to receive on referral update
class ReferralUpdate(ReferralBase):
        source_id: int | None = None
        claim_id: int | None = None
        supplier_id: int  | None = None
        type: str | None = None
        daystohire: int | None = None
        creditrepair: str | None = None
        authority_id: int  | None = None


# Database model, database table inferred from class name
class Referral(ReferralBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        owner: User | None = Relationship(back_populates="referrals")
        source: Source | None = Relationship(back_populates="referrals")
        daystohire: int | None = None
        creditrepair: str | None = None
        circs_group_id: int | None = Field(default=None, foreign_key="circs_group.id", nullable=True)
        veh_group_id: int | None = Field(default=None, foreign_key="veh_group.id", nullable=True)



# Properties to return via API, id is always required
class ReferralPublic(ReferralBase):
        id: int
        source: Source



class ReferralsPublic(SQLModel):
        data: list[ReferralPublic]
        count: int 



##################################### Referral_Allocation ################################


# Shared properties
class Referral_AllocationBase(SQLModel):
        supplier_id: int | None = Field(default=None, foreign_key="supplier.id", nullable=False)
        referral_id: int | None = Field(default=None, foreign_key="referral.id", nullable=False)
        sentdate: datetime | None = None
        status: str | None = None
        responsedate: datetime | None = None


# Properties to receive on referral_allocation creation
class Referral_AllocationCreate(Referral_AllocationBase):
        supplier_id: int 
        referral_id: int 
        sentdate: datetime 
        status: str 
        responsedate: datetime | None = None


# Properties to receive on referral_allocation update
class Referral_AllocationUpdate(Referral_AllocationBase):
        supplier_id: int | None = None
        referral_id: int | None = None 
        sentdate: datetime | None = None 
        status: str | None = None 


# Database model, database table inferred from class name
class Referral_Allocation(Referral_AllocationBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        owner: User | None = Relationship(back_populates="referral_allocations")


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
        authority_id: int | None = Field(default=None, foreign_key="authority.id", nullable=False)
        plate_type: str | None = None
        veh_group_id: int | None = Field(default=None, foreign_key="veh_group.id", nullable=False)
        circs_group_id: int | None = Field(default=None, foreign_key="circs_group.id", nullable=False)
        type: str | None = None
        rate: float | None = None
        hire_length: int | None = None
        source_id: int | None = Field(default=None, foreign_key="source.id", nullable=False)


# Properties to receive on source_rate creation
class Source_RateCreate(Source_RateBase):
        pass


# Properties to receive on source_rate update
class Source_RateUpdate(Source_RateBase):
        authority_id: int | None = None
        plate_type: str | None = None
        veh_group_id: int | None = None
        circs_group_id: int | None = None
        type: str | None = None
        rate: float | None = None
        hire_length: int | None = None
        source_id: int | None = None


# Database model, database table inferred from class name
class Source_Rate(Source_RateBase, CreatedModifiedBase,table=True):
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
        owner: User | None = Relationship(back_populates="source_rates")


# Properties to return via API, id is always required
class Source_RatePublic(Source_RateBase):
        pass



class Source_RatesPublic(SQLModel):
        data: list[Source_RatePublic]
        count: int 


####### Supplier_stats


# Shared properties
class Supplier_StatBase(SQLModel):
        authority_id: int | None = Field(default=None, foreign_key="authority.id", nullable=True)
        plate_type: str | None = None
        veh_group_id: int | None = Field(default=None, foreign_key="veh_group.id", nullable=True)
        circs_group_id: int | None = Field(default=None, foreign_key="circs_group.id", nullable=True)
        rate: float | None = None
        rate_rank: int | None = None
        hire_length: int | None = None
        supplier_id: int | None = Field(default=None, foreign_key="supplier.id", nullable=True)
        daystohire: int | None = None
        daystohire_rank: int | None = None
        conversion: int | None = None 
        conversion_rank: int | None = None
        total_rank: int | None = None


# Properties to receive on supplier_stat creation
class Supplier_StatCreate(Supplier_StatBase):
        pass


# Properties to receive on supplier_stat update
class Supplier_StatUpdate(Supplier_StatBase):
        authority_id: int | None = None  # type: ignore
        plate_type: str | None = None  # type: ignore
        veh_group_id: int | None = None  # type: ignore
        circs_group_id: int | None = None  # type: ignore
        rate: float | None = None  # type: ignore
        rate_rank: int | None = None
        hire_length: int | None = None  # type: ignore
        supplier_id: int | None = None  # type: ignore
        daystohire: int | None = None
        daystohire_rank: int | None = None
        conversion: int | None = None 
        conversion_rank: int | None = None
        total_rank: int | None = None



# Database model, database table inferred from class name
class Supplier_Stat(Supplier_StatBase, CreatedModifiedBase,table=True):
        __table_args__ = (
            UniqueConstraint("authority_id", "veh_group_id", "circs_group_id","supplier_id", name="supplier_stat_constraint"),
        )
        id: int | None = Field(default=None, primary_key=True)
        owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=True)
        owner: User | None = Relationship(back_populates="supplier_stats")
        supplier: Supplier | None = Relationship(back_populates="supplier_stats")



# Properties to return via API, id is always required
class Supplier_StatPublic(Supplier_StatBase):
        id: int
        owner_id: int


class Supplier_StatsPublic(SQLModel):
        data: list[Supplier_StatPublic]
        count: int 



class RequestBase(SQLModel):
        source_id: int
        type: str | None = None
        daystohire: int | None = None
        creditrepair: str | None = None
        authority_id: int | None = None
        client_firstname: str 
        client_lastname: str 
        client_address_1: str | None = None
        client_address_town: str | None = None
        client_address_postcode: str | None = None
        client_vehicle_reg: str | None = None
        client_insurer: str | None = None
        client_insurer_policyno: str | None = None
        client_phone: str | None = None
        client_mobile: str | None = None
        client_email: str | None = None
        authority_id: int | None = None
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
        circs_grade_id: int | None = None
        veh_group_id: int | None = None
        circs_group_id: int | None = None

class RequestCreate(RequestBase):
        pass


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
    new_password: str = Field(min_length=8, max_length=40)
