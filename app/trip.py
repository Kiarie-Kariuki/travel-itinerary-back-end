from sqlalchemy import Column, Integer, String, Float, ForeignKey, Delete
from sqlalchemy.orm import relationship, sessionmaker
from database import Base, Session, engine, db
from user import User
from destination import Destination
from activity import Activity
from datetime import datetime
from flask import current_app


# Create the tables
def create_trip(user_id):
    # Create a Flask application context
    with current_app.app_context():
        db.create_all()


Session = sessionmaker(bind=engine)

class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    trip_name = Column(String(100), nullable=False)
    start_date = Column(String(10), nullable=False)
    end_date = Column(String(10), nullable=False)
    budget = Column(Float, default=0.0)

    # Define the relationship between Trip and User
    user = relationship("User", back_populates="trips")

    # Define the relationship between Trip and Destination
    destinations = relationship("Destination", back_populates="trip")

# Create the table
Base.metadata.create_all(engine)

def create_trip(user_id):
    session = Session()
    
    # Prompt for trip details
    trip_name = input("Enter trip name: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    budget = float(input("Enter budget for the trip: "))
    
    # Create a new trip
    trip = Trip(user_id=user_id, trip_name=trip_name, start_date=start_date, end_date=end_date, budget=budget)
    session.add(trip)
    session.commit()
    
    print(f"Trip '{trip_name}' created successfully.")
    
    session.close()

def generate_travel_summary(user_id):
    session = Session()
    
    # Retrieve all trips for the given user
    trips = session.query(Trip).filter_by(user_id=user_id).all()

    # Check if the user has any trips
    if not trips:
        print("You don't have any trips yet.")
    else:
        print("Your trips:")
        for i, trip in enumerate(trips, 1):
            print(f"{i}. {trip.trip_name}")

        trip_choice = input("Select a trip (enter the number): ")
        try:
            trip_choice = int(trip_choice)
            if 1 <= trip_choice <= len(trips):
                selected_trip = trips[trip_choice - 1]
                print(f"Summary for trip '{selected_trip.trip_name}':")

                # Retrieve all destinations for the selected trip
                destinations = selected_trip.destinations

                if not destinations:
                    print("No destinations found for this trip.")
                else:
                    total_budget = selected_trip.budget
                    total_expenses = 0.0

                    for destination in destinations:
                        print(f"- Destination: {destination.name}")

                        # Calculate and display activities and expenses for each destination
                        activities = destination.activities
                        if activities:
                            for activity in activities:
                                print(f"  - Activity: {activity.name}")
                                print(f"    - Date: {activity.date_time}")
                                print(f"    - Description: {activity.description}")
                                print(f"    - Cost: ${activity.cost:.2f}")
                                total_expenses += activity.cost

                    # Display the remaining budget for the trip
                    remaining_budget = total_budget - total_expenses
                    print(f"Total Budget: ${total_budget:.2f}")
                    print(f"Total Expenses: ${total_expenses:.2f}")
                    print(f"Remaining Budget: ${remaining_budget:.2f}")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    session.close()



def delete_trip(trip_id):
    session = Session()

    # Query and delete all activities associated with the destinations of the trip
    destination_ids = session.query(Destination.id).filter_by(trip_id=trip_id).all()
    if destination_ids:
        # Convert the list of IDs into a flat list
        destination_ids = [id for (id,) in destination_ids]
        session.query(Activity).filter(Activity.destination_id.in_(destination_ids)).delete(synchronize_session=False)

    # Delete the destinations associated with the trip
    session.query(Destination).filter_by(trip_id=trip_id).delete(synchronize_session=False)

    # Delete the trip itself
    session.query(Trip).filter_by(id=trip_id).delete(synchronize_session=False)

    session.commit()
    print(f"Trip with ID {trip_id} deleted.")

    session.close()
