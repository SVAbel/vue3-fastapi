# FastAPI
from imp import reload
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter, File, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse

from fastapi.templating import Jinja2Templates

# Standard
from typing import List, Union, Optional
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Custom
from db.db import DatabaseLayer
from models.models import UserModel, Token, TokenData, UserWithHashModel
from util.connect_with_sqlalchemy import build_sqla_connection_string, test_connection
from util.passwords import hash, verify
from routes import (
    calendar,
    counsel,
    dashboard,
    payment,
    reception,
    reservation,
    surgery,
    van,
    bom,
)


app = FastAPI(
    title="Meta CRM",
    description="Meta CRM Demo",
    version=1.0,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CONNECTION_STRING = build_sqla_connection_string(
#     "postgresql://root:root@localhost:26257/users"
# )

# database = DatabaseLayer(CONNECTION_STRING)
# test_connection(database.engine)


# Auth
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_user(username: str):
    return database.get_user(username=username)


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify(user.password, password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: UserWithHashModel = Depends(get_current_user),
):
    return current_user


@app.post("/token", response_model=TokenData)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response = {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
    }
    return response


def include_router(app):
    app.include_router(calendar)
    app.include_router(counsel)
    app.include_router(dashboard)
    app.include_router(reception)
    app.include_router(payment)
    app.include_router(reservation)
    app.include_router(surgery)
    app.include_router(van)
    app.include_router(bom)


app.mount("/static", StaticFiles(directory="./dist", html=True), name="static")

templates = Jinja2Templates(directory="./dist")


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}


@app.get("/", response_class=RedirectResponse)
async def entrypoint_root():
    return "/static"


@app.get("/static", response_class=HTMLResponse)
async def read_root_r(request: Request):
    context = {}
    context["request"] = request
    return templates.TemplateResponse("index.html", context=context)


# async def main(app):
#     config = uvicorn.Config(app, port=5000, log_level="info")
#     server = uvicorn.Server(config=config)
#     await server.serve()


# if __name__ == "__main__":
#     # Use this for debugging purposes only
#     import asyncio
#     import uvicorn

#     include_router(app)
#     asyncio.run(main(app))
