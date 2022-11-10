from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as _sql
from sqlalchemy.orm import relationship

from database import Base


class Flat(Base):
    __tablename__ = "flats"
    id = _sql.Column(UUID(as_uuid=True), primary_key=True)
    title = _sql.Column(_sql.String)
    images = relationship("Images", back_populates="flat")


class Images(Base):
    __tablename__ = "images"
    id = _sql.Column(UUID(as_uuid=True), primary_key=True)
    image_url = _sql.Column(_sql.String)
    flat_id = _sql.Column(UUID(as_uuid=True), _sql.ForeignKey("flats.id"))
    flat = relationship("Flat", back_populates="images")

