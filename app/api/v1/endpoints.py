from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import user as schema
from app.db import session, crud

router = APIRouter()


@router.post("/users/", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(session.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.create_user(db, user)


@router.get("/users/", response_model=list[schema.User])
async def get_users(db: Session = Depends(session.get_db)):
    return crud.get_users(db)


@router.get("/users/{user_id}", response_model=schema.User)
async def get_user(user_id: int, db: Session = Depends(session.get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
