from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from setup.database import Base  # Импорт базового класса из настроек БД

class HydrationRecord(Base):
    __tablename__ = "hydration_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)

    user = relationship("User", back_populates="hydration_records")

    def __repr__(self):
        return f"<HydrationRecord(id={self.id}, amount={self.amount}ml, time={self.timestamp})>"