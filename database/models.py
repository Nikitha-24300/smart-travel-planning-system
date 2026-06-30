from sqlalchemy import Column, Integer, String, Float, Text
from database.connection import Base


class TripHistory(Base):

    __tablename__ = "trip_history"

    id = Column(Integer, primary_key=True, index=True)

    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)

    route = Column(Text, nullable=False)

    total_distance = Column(Float, default=0)

    preference = Column(String, default="fastest")

    status = Column(String, default="SUCCESS")