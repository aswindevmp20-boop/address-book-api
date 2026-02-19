from sqlalchemy.orm import Session
from . import models, schemas
from .utils import haversine_distance

def create_addresses(db: Session, address: schemas.AddressCreate):
    db_address = models.Address(**address.model_dump())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def get_address(db: Session, address_id: str):
    print("Searching for:", address_id)
    addresses = db.query(models.Address).all()
    print("Available IDs:", [a.id for a in addresses])
    return db.query(models.Address).filter(models.Address.id == address_id).first()

# Added pagination
def get_all_addresses(db:Session, skip: int =0, limit: int =10):
    return db.query(models.Address).all()

def update_addresses(db: Session, address_id: str, address_update: schemas.AddressUpdate):
    db_address = get_address(db, address_id)
    if not db_address:
        return None
    
    for field, value in address_update.model_dump(exclude_unset=True).items():
        setattr(db_address, field, value)

    db.commit()
    db.refresh(db_address)
    return db_address

def delete_address(db: Session, address_id: str):
    db_address = get_address(db, address_id)
    if not db_address:
        return None
    db.delete(db_address)
    db.commit()
    return db_address

def get_addresses_within_radius(db:Session, latitude: float, longitude:float, radius_km: float):
    addresses = get_all_addresses(db)
    return [
        address for address in addresses
        if haversine_distance(latitude, longitude, address.latitude, address.longitude <= radius_km)
    ]
