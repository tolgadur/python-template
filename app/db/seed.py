from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import User


def seed_database(db: Session = SessionLocal()):
    # Check if the data already exists to avoid duplicate entries
    if db.query(User).first():
        return

    # Add your initial data here
    user1 = User(email="user1@example.com", hashed_password="hashedpassword1", is_active=True)
    db.add(user1)
    db.commit()
    db.close()
