from fastapi import APIRouter, Query, Depends
from fastapi_jwt_auth import AuthJWT
from app.utils.scraper import fetch_data

router = APIRouter()

@router.get("/")
def get_processing_data(year: int = Query(None, description="Year of the data"), suboption: str = Query("subopt_01", description="Suboption for processing data"), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    
    data = fetch_data("processing", year, suboption)
    return {"data": data}
