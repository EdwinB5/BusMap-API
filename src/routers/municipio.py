from fastapi import APIRouter, Depends
from src.controller.municipio_controller import MunicipioController
from sqlalchemy.orm import Session
from src.database import get_db

router_municipio = APIRouter()

@router_municipio.get("/api/municipios")
def read_municipios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    municipio = MunicipioController(db)
    return municipio.get_municipios(limit=limit, skip=skip)