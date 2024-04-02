from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.crud import crud_user
from app.schemas import schemas
from app.api.dependencies import get_db
# Inside user.py
from app.schemas.schemas import User, UserCreate
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import hash_password

router = APIRouter()

# @router.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud_user.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud_user.create_user(db=db, user=user)









@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if required fields are included
    if not all([user.email, user.name, user.password, user.phone]):
        missing_fields = [field for field in ["email", "name", "password", "phone"] if not getattr(user, field)]
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Missing fields for user creation: {', '.join(missing_fields)}."
        )

    # Check if the user already exists
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the user's password before creating the user
    hashed_password = hash_password(user.password)
    # Create the user with the hashed password
    return crud_user.create_user(db=db, user=user, hashed_password=hashed_password)


    # # Hash the user's password before creating the user
    # hashed_password = hash_password(user.password)
    # return crud_user.create_user(db=db, user=user, hashed_password=hashed_password)
