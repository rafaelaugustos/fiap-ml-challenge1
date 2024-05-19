from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from app.config import settings
from app.routes import production, processing, commercialization, importation, exportation
from fastapi.responses import JSONResponse

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

class Settings(BaseModel):
    authjwt_secret_key: str = settings.JWT_SECRET_KEY

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=401,
        content={"detail": exc.message}
    )

@app.post('/login')
def login(user: User, Authorize: AuthJWT = Depends()):
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token = Authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}

app.include_router(production.router, prefix="/production", tags=["Production"])
app.include_router(processing.router, prefix="/processing", tags=["Processing"])
app.include_router(commercialization.router, prefix="/commercialization", tags=["Commercialization"])
app.include_router(importation.router, prefix="/importation", tags=["Importation"])
app.include_router(exportation.router, prefix="/exportation", tags=["Exportation"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Vitiviniculture API"}
