from user import User 
from sqlalchemy.orm import sessionmaker
from database import engine, Session
from activity import Activity
from destination import Destination
from budget import update_budget, add_activity_cost_to_budget

Session = sessionmaker(bind=engine)

def list_user_trips(user_id):
    session = Session()

    # Query the database to find the user by user_id
    user = session.query(User).filter_by(id=user_id).first()

    if user:
        trips = user.trips
        if not trips:
            print("You don't have any trips yet.")
        else:
            print("Your trips:")
            for trip in trips:
                print(f"Trip ID: {trip.id}, Trip Name: {trip.trip_name}")

    session.close()

def delete_activity(activity_id):
    session = Session()

    # Query the database to find the activity with the specified activity_id
    activity = session.query(Activity).filter_by(id=activity_id).first()

    if activity:
        # Get the cost of the activity
        cost = activity.cost

        # Get the destination_id to pass to update_budget
        destination_id = activity.destination_id

        # Delete the activity
        session.delete(activity)
        session.commit()
        print(f"Activity '{activity.name}' deleted.")

        # Add the cost of the deleted activity back to the budget
        add_activity_cost_to_budget(destination_id, cost)
        print(f"Cost ({cost}) added back to the budget.")
    else:
        print("Activity not found.")

    session.close()

