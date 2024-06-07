from sqlmodel import Field, Relationship, SQLModel

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