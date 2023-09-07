import click
from user import create_user, get_user_by_username
from trip import Trip, create_trip, generate_travel_summary, delete_trip
from destination import add_destination, Destination
from activity import schedule_activity, Activity
from datetime import datetime
from budget import update_budget
from trip_management import list_user_trips, delete_activity
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(main)

def get_password():
    while True:
        password = click.prompt('Password', hide_input=True, confirmation_prompt=True)
        confirmation_password = click.prompt('Repeat for confirmation', hide_input=True)
        if password == confirmation_password:
            return password
        else:
            click.echo('Error: The two entered values do not match.')

@click.command()
@click.option('--username', prompt='Username')
@click.password_option()
def main(username, password):
    user = get_user_by_username(username)
    
    if user:
        print(f'Welcome back, {username}!')
    else:
        password = get_password()
        create_user(username, password)
        print(f'Welcome, {username}!')

    print()
    print()
    print("WELCOME TO TRAVEL ITENERARY!")

    while True:
        print("\nMain Menu:")
        print("1. Create a new trip")
        print("2. Add a destination")
        print("3. Schedule an activity")
        print("4. View all trips")
        print("5. Delete a trip")
        print("6. Delete an activity")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_trip(user.id)
        elif choice == "2":
            trip_id = int(input("Enter the ID of the trip you want to add a destination to: "))
            destination_name = input("Enter destination name: ")
            add_destination(trip_id, destination_name)
        elif choice == "3":
            destination_id = int(input("Enter the ID of the destination for the activity: "))
            activity_name = input("Enter activity name: ")
            activity_date = datetime.strptime(input("Enter activity date (YYYY-MM-DD HH:MM:SS): "), '%Y-%m-%d %H:%M:%S')
            activity_description = input("Enter activity description: ")
            activity_cost = float(input("Enter activity cost: "))
            schedule_activity(destination_id, activity_name, activity_date, activity_description, activity_cost)
        elif choice == "4":
            list_user_trips(user.id)
        elif choice == "5":
            trip_id = int(input("Enter the ID of the trip you want to delete: "))
            delete_trip(trip_id)
        elif choice == "6":
            activity_id = int(input("Enter the ID of the activity you want to delete: "))
            delete_activity(activity_id)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
