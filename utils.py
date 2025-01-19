from passlib.context import CryptContext
from jose import JWTError, jwt
import datetime

pass_manager = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "382098ceb4937a014ff1a33341c55d4052f1f1fefc6cc84dfcf7e6952afdae12"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_jwt(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.now(
    ) + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return token
