from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(main)

# Initialize the declarative base
Base = declarative_base()

# Create the database engine
engine = create_engine('sqlite:///database.db')

# Create a session factory
Session = sessionmaker(bind=engine)
