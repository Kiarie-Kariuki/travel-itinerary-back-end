from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from database import Base, Session, engine
from datetime import datetime
from destination import Destination
from budget import update_budget

Session = sessionmaker(bind=engine)

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    destination_id = Column(Integer, ForeignKey('destinations.id'), nullable=False)
    name = Column(String(100), nullable=False)
    date_time = Column(DateTime, nullable=False)
    description = Column(String(200))
    cost = Column(Float)

    # Define the relationship between Activity and Destination
    destination = relationship("Destination", back_populates="activities")

# Create the 'activities' table in the database
Base.metadata.create_all(bind=engine)


def schedule_activity(destination_id, name, date_time, description=None, cost=None):
    session = Session()

    # Check if the destination exists
    destination = session.query(Destination).filter_by(id=destination_id).first()

    if not destination:
        print("Destination not found.")
        session.close()
        return

    # Prompt for activity details
    activity_name = name

    # Convert the activity_date to a string if it's not already
    if isinstance(date_time, datetime):
        date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')

    activity_date = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')

    # Calculate the cost if not provided
    if cost is None:
        cost = float(input("Enter activity cost: "))

    # Create a new activity
    activity = Activity(destination_id=destination_id, name=activity_name, date_time=activity_date, description=description, cost=cost)
    session.add(activity)
    session.commit()

    print(f"Activity '{activity_name}' scheduled successfully.")

    # Deduct the cost from the user's budget
    update_budget(destination_id, cost)

    session.close()
