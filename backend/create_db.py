from database.database import Base, engine
from database import models

def create_database():
    print("Creating Database Tables...")
    Base.metadata.create_all(bind=engine)
    print("Database Tables Created!")


if __name__ == "__main__":
    create_database()