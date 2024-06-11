from sqlmodel import Field, Relationship, SQLModel, DateTime, func, Column

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
    items: list["Item"] = Relationship(back_populates="owner")
    sources: list["Source"] = Relationship(back_populates="owner")
    suppliers: list["Supplier"] = Relationship(back_populates="owner")


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
    name: str
    address_1: str
    address_town: str
    address_postcode: str
    created_on: str | None = Column(DateTime(timezone=True), server_default=func.now())
    modified_on: str | None = Column(DateTime(timezone=True), onupdate=func.now())
    Email: str
    Tel: int




# Properties to return via API, id is always required
class SupplierPublic(SupplierBase):
    id: int
    owner_id: int


class SuppliersPublic(SQLModel):
    data: list[SupplierPublic]
    count: int 


















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
