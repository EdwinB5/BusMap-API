from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src import schemas
from src.controller.simulacion_controller import SimulacionController

router_simulacion = APIRouter()

@router_simulacion.get("/api/simulacion", response_model=schemas.Simulacion)
def read_simulacion(db: Session = Depends(get_db)):
    simulacion = SimulacionController(db)
    return simulacion.get_simulacion()
