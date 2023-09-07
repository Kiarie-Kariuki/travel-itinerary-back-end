from sqlalchemy import update
from destination import Destination
from database import Session


def update_budget(destination_id, cost):
    session = Session()
    
    # Check if the destination exists
    destination = session.query(Destination).filter_by(id=destination_id).first()

    if destination:
        trip = destination.trip

        if trip.budget >= cost:
            trip.budget -= cost
            session.commit()
            print("Budget updated successfully.")
        else:
            print("Insufficient budget for this activity.")
    else:
        print("Destination not found.")

    session.close()