from sqlalchemy import Column, String, Float, Index
from .database import Base
import uuid

class Address(Base):
    __tablename__="addresses"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()),index=True)
    name = Column(String, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

# Optimized geo-search performance.
    __table_args__ = (
        Index("idx_lat_long", "latitude", "longitude"),
    )