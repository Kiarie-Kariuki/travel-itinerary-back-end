from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from database import Base, Session, engine
from user import User

Session = sessionmaker(bind=engine)

class Destination(Base):
    __tablename__ = 'destinations'

    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer, ForeignKey('trips.id'), nullable=False)
    name = Column(String(100), nullable=False)

    # Define the relationship between Destination and Activity
    activities = relationship("Activity", back_populates="destination")


    # Define the relationship between Destination and Trip
    trip = relationship("Trip", back_populates="destinations")

# Create the table for the Destination class
Base.metadata.create_all(engine)


def add_destination(user_id, name):
    session = Session()

    # Get the user with the specified user_id
    user = session.query(User).filter_by(id=user_id).first()

    if user:
        # Prompt the user to select a trip
        trips = user.trips
        if not trips:
            print("You don't have any trips yet. Please create a trip first.")
        else:
            print("Select a trip to add the destination:")
            for i, trip in enumerate(trips, 1):
                print(f"{i}. {trip.trip_name}")

            trip_choice = input("Enter the number of the trip: ")
            try:
                trip_choice = int(trip_choice)
                if 1 <= trip_choice <= len(trips):
                    selected_trip = trips[trip_choice - 1]

                    # Create a new destination and associate it with the selected trip
                    destination = Destination(trip=selected_trip, name=name)
                    session.add(destination)
                    session.commit()

                    print(f"Destination '{name}' added to trip '{selected_trip.trip_name}'.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    else:
        print("User not found.")

    session.close()