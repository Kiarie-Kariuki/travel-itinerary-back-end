# Travel Itinerary CLI App

Travel Itinerary is a command-line interface (CLI) application that enables users to efficiently plan and manage their trips. This README provides an overview of the application's features, installation instructions, usage guidelines, and how to contribute to the project

# Features

Travel Itinerary CLI App offers the following key features:

User Account Management:
    User registration and authentication.
Trip Management:
    Create and manage multiple trips.
    View all trips associated with the user account.
    Delete trips.
Destination Management:
    Add destinations to trips.
Activity Scheduling:
    Schedule activities within destinations.
    Delete activities.
Budget Tracking:
    Update and manage trip budgets.

# Installation

To set up and run the Travel Itinerary CLI App, follow these installation steps:

Clone the repository to your local machine:

git clone https://github.com/Kiarie-Kariuki/travel-itinerary-back-end

Navigate to the project directory:

    cd Travel\ Itinerary

Create a virtual environment (optional but recommended):

    python -m venv venv

Activate the virtual environment:

On Windows:

    venv\Scripts\activate

On macOS and Linux:

    source venv/bin/activate

Install the required dependencies:

    pip install -r requirements.txt

Run the application:

    python main.py

# Usage

Once the Travel Itinerary CLI App is running, you can use the following options from the main menu:

Create a New Trip.
Add a Destination.
Schedule an Activity.
View All Trips.
Delete a Trip.
Delete an Activity
Exit: Exit the application.

# Models and Functions

The application is structured around the following models, each with its associated functions:
User Model

    create_user(username, password): Create a new user account.
    get_user_by_username(username): Retrieve a user by their username.

Trip Model

    create_trip(user_id): Create a new trip for a user.
    generate_travel_summary(trip_id): Generate a summary of the travel itinerary.
    delete_trip(trip_id): Delete a trip and associated destinations and activities.

Destination Model

    add_destination(trip_id, name): Add a destination to an existing trip.

Activity Model

    schedule_activity(destination_id, name, date, description, cost): Schedule an activity within a destination.
    delete_activity(activity_id): Delete a specific activity and update the trip budget accordingly.

Please refer to the code and docstrings within each model for more detailed information about each function's behavior.


# Contributing

Contributions to this project are welcome! To contribute:

    Fork the repository.

    Create a new branch for your feature or bug fix:

        git checkout -b feature/my-feature

    Make your changes and commit them:

        git commit -m "Add my feature"

    Push your changes to your fork:

        git push origin feature/my-feature

    Create a pull request against the main branch of the original repository.

# License

This project is licensed under the CAK License. See the LICENSE file for details.