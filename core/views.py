
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm.session import Session
from fastapi.param_functions import Body, Depends
from typing import List
from dependencies import get_db, getAuthenticity
from . import crud
from . import schemas

router = APIRouter(tags=["core"])

@router.get("/hello")
async def hello_world():
    return {"message": "Hello, World!"}


@router.get("/staff", response_model=List[schemas.StaffRes])
async def allUsers(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return crud.get_users(db, skip, limit)
