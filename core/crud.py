from typing import Optional
import datetime
from sqlalchemy.orm import Session
from . import models, schemas

from passlib.context import CryptContext
from jose import JWTError, jwt
from dependencies import SECRET_KEY, ALGORITHM


pass_manager = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_staff(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Staff).offset(skip).limit(limit).all()


def createStaff(db: Session, user: schemas.StaffCreate):
    hashed_password = pass_manager.hash(user.password)
    db_user = models.Staff(
        username=user.username,
        email=user.email,
        password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_staff_by_data(db: Session, username: Optional[str] = None, id: Optional[str] = None):
    if username:
        return db.query(models.Staff).filter(models.Staff.username == username).first()
    elif id:
        return db.query(models.Staff).get(id)
    

def check_password(db: Session, username: str, password: str):
    userIndb = db.query(models.Staff).filter(
        models.Staff.username == username).first()
    check = pass_manager.verify(password, userIndb.password)
    return check


def getStaffByToken(db, token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except JWTError as e:
        return None
    return get_staff_by_data(db, username=payload['username'])