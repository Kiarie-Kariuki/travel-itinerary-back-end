from user import User 
from sqlalchemy.orm import sessionmaker
from database import engine

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
