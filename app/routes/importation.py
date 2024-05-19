from fastapi import APIRouter, Query, Depends
from fastapi_jwt_auth import AuthJWT
from app.utils.scraper import fetch_data

router = APIRouter()

@router.get("/")
def get_importation_data(year: int = Query(None, description="Year of the data"), suboption: str = Query("subopt_01", description="Suboption for importation data"), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    
    data = fetch_data("importation", year, suboption)
    return {"data": data}
