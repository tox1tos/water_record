from datetime import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..setup.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)

    hydration_records = relationship("HydrationRecord", back_populates="user")


class HydrationRecord(Base):
    __tablename__ = "hydration_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    date = Column(Date, index=True)
    glasses = Column(Integer)

    user = relationship("User", back_populates="hydration_records")

    def __repr__(self):
        return f"<HydrationRecord(id={self.id}, amount={self.amount}ml, time={self.timestamp})>"
