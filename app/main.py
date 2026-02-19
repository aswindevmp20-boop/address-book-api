from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .dependencies import get_db
from .database import engine
from .logger import logger
import uuid

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")


@app.post("/addresses/", response_model=schemas.AddressResponse)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    logger.info("Creating new address")
    return crud.create_addresses(db, address)


@app.get("/addresses/search/")
def search_addresses(
    latitude: float,
    longitude: float,
    radius_km: float,
    db: Session = Depends(get_db)
):
    return crud.get_addresses_within_radius(db, latitude, longitude, radius_km)


@app.get("/addresses/{address_id}", response_model=schemas.AddressResponse)
def read_address(address_id: uuid.UUID, db: Session = Depends(get_db)):
    address = crud.get_address(db, str(address_id))
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@app.get("/addresses/", response_model=list[schemas.AddressResponse])
def read_all_addresses(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return crud.get_all_addresses(db, skip=skip, limit=limit)


@app.put("/addresses/{address_id}", response_model=schemas.AddressResponse)
def update_address(
    address_id: uuid.UUID,
    address_update: schemas.AddressUpdate,
    db: Session = Depends(get_db)
):
    address = crud.update_addresses(db, str(address_id), address_update)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@app.delete("/addresses/{address_id}")
def delete_address(address_id: uuid.UUID, db: Session = Depends(get_db)):
    address = crud.delete_address(db, str(address_id))
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"detail": "Address deleted successfully"}
