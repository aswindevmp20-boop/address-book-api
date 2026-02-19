from pydantic import BaseModel, Field, validator
import uuid

class AddressBase(BaseModel):
    name: str
    street: str
    city: str
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180,le=180)

class AddressCreate(AddressBase):
    pass

class AddressUpdate(BaseModel):
    name: str | None = None
    street: str | None = None
    city: str | None = None
    latitude: float | None = Field(None, ge=-90, le=90)
    longitude: float | None = Field(None, ge=-180, le=180)

class AddressResponse(AddressBase):
    id: uuid.UUID

    class config:
        from_attributes = True
