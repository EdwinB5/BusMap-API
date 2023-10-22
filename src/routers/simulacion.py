from fastapi import APIRouter, Depends, Query, HTTPException

from sqlalchemy.orm import Session
from src.database import get_db

from src import schemas
from src.controller.simulacion_controller import SimulacionController

router_simulacion = APIRouter()

@router_simulacion.get("/api/simulacion", response_model=schemas.Simulacion, tags=['simulacion'])
async def read_simulacion(db: Session = Depends(get_db)):
    simulacion = SimulacionController(db)
    return simulacion.get_simulacion()

@router_simulacion.patch("/api/simulacion", response_model=schemas.Simulacion, tags=['simulacion'])
async def update_simulacion(id: int = Query(None), simulacion_request: schemas.Simulacion = None, db: Session = Depends(get_db)):
    simulacion = SimulacionController(db)
    result = simulacion.update_simulacion(id, simulacion_request)
    
    if result is None:
        raise HTTPException(status_code=404, detail=f"Simulacion with id[{id}] not found")
        
    return result

