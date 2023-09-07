from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from database import Base, Session, engine


Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    #define the relationship between the User and Trip
    trips = relationship("Trip", back_populates="user")


    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def create_user(username, password):
    session = Session()
    user = User(username=username, password=password)
    user.set_password(password)
    session.add(user)
    session.commit()
    session.close()

def get_user_by_username(username):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    session.close()
    return user