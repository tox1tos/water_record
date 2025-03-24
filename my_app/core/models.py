from sqlalchemy import Column, Integer, Date
from setup.database import Base

class HydrationRecord(Base):
    __tablename__ = "hydration_records"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    glasses = Column(Integer)