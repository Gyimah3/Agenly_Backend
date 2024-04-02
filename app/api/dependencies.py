# /backend/app/api/dependencies.py

from sqlalchemy.orm import Session
from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# /backend/app/api/dependencies.py (Continued)

# /backend/app/api/dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from typing import Optional

from app.core.config import settings
from app.models.models import User  # Adjust import as necessary
from app.schemas.schemas import TokenData  # Make sure this import matches your project structure
#from app.crud.crud_user import get_user_by_username  # Adjust this to your actual function
from sqlalchemy.orm import Session
from ..database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# /backend/app/api/dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from typing import Optional

from app.core.config import settings  # Make sure this import is correct
from app.models.models import User  # Adjust the import path as necessary
from app.schemas.schemas import TokenData  # Adjust the import path as necessary
from app.crud.crud_user import get_user  # Adjust the import path as necessary

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)  # Assuming TokenData schema has a user_id field now
    except JWTError:
        raise credentials_exception
    
    user = get_user(db, user_id=token_data.user_id)
    if user is None:
        raise credentials_exception
    return user



