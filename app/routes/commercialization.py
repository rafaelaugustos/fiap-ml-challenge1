from fastapi import APIRouter, Query, Depends
from fastapi_jwt_auth import AuthJWT
from app.utils.scraper import fetch_data

router = APIRouter()

@router.get("/")
def get_commercialization_data(year: int = Query(None, description="Year of the data"), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    
    data = fetch_data("commercialization", year)
    return {"data": data}
