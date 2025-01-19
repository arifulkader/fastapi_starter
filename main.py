import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from core import views
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(views.router, prefix="/core")

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: HTTPException):
    error_body = {}
    for error in exc.errors():
        try:
            error_body[f"{error.get('loc')[1]}"] = str(
                error.get('msg')).capitalize()
        except:
            error_body[f"{error.get('loc')[0]}"] = str(
                error.get('msg')).capitalize()
    error_body['request_body'] = jsonable_encoder(exc.body)
    return JSONResponse({"error": error_body}, status_code=status.HTTP_400_BAD_REQUEST)

