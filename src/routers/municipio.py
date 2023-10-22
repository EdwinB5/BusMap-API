from fastapi import APIRouter, Depends, Query
 
from src.controller.municipio_controller import MunicipioController

from sqlalchemy.orm import Session
from src.database import get_db

router_municipio = APIRouter()

@router_municipio.get("/api/municipios", tags=['municipios'])
async def read_municipios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    municipio = MunicipioController(db)
    return municipio.get_municipios(limit=limit, skip=skip)

@router_municipio.get("/api/municipios/", tags=['municipios'], response_model=None)
async def read_municipio(nombre: str = Query(None), id: int = Query(None), aparcadero: bool = Query(None), db: Session = Depends(get_db)):
    result = {}
    municipio = MunicipioController(db)
    
    if nombre is not None:
        result = municipio.get_municipio_by_name(municipio_nombre=nombre)
    if id is not None:
        result = municipio.get_municipio_by_id(municipio_id=id)
    if aparcadero is not None:
        result = municipio.get_municipio_by_aparcadero(aparcadero=aparcadero)
        
    return result
