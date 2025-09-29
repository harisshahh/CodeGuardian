from database.database import Base, engine
from database import models
import time
from sqlalchemy import text


def create_database():
    print("Creating Database Tables...")
    with engine.begin() as connection:
        connection.execute(text("DROP TABLE IF EXISTS reviews CASCADE;"))

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database Tables Created!")
    time.sleep(1)


if __name__ == "__main__":
    create_database()