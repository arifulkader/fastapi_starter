from fastapi.exceptions import HTTPException
from fastapi.security.utils import get_authorization_scheme_param
from utils import ALGORITHM, SECRET_KEY
from fastapi import status, Request
from jose import JWTError, jwt

from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def getAuthenticity(request: Request):
    if 'Authorization' in request.headers:
        auth = request.headers.get('Authorization')
        param, token = get_authorization_scheme_param(auth)
        try:
            jwt.decode(token, SECRET_KEY, ALGORITHM)
        except JWTError as e:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, {
                'Token': f'{e}!'})
        return token
    raise HTTPException(status.HTTP_401_UNAUTHORIZED, {
                        'Error': 'User credential is not exist !'})


def _finditem(obj, key):
    if key in obj:
        return obj[key]
    for k, v in obj.items():
        if isinstance(v, dict):
            item = _finditem(v, key)
            if item is not None:
                return item

