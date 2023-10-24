from fastapi import APIRouter, Depends, Query, HTTPException
 
from src.controller.bus_controller import BusController
from src import schemas

from sqlalchemy.orm import Session
from src.database import get_db

router_bus = APIRouter()

@router_bus.get("/api/bus", tags=['bus'], response_model=list[schemas.Bus])
async def read_buses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    buses = BusController(db)
    return buses.get_buses(limit=limit, skip=skip)

@router_bus.get("/api/bus/", tags=["bus"], response_model=list[schemas.Bus])
async def read_bus_municipio(municipio_id: int = Query(None), db: Session = Depends(get_db)):
    buses = BusController(db)
    results = buses.get_buses_by_municipio(municipio_id)

    if not results:
        raise HTTPException(status_code=404, detail=f"Buses not found in municipio_id[{municipio_id}]")
    
    return results

@router_bus.post("/api/bus/register", tags=["bus"], response_model=schemas.Bus)
async def register_bus(municipio_origen: int, municipio_destino: int, db: Session = Depends(get_db)):
    if municipio_origen == municipio_destino:
        raise HTTPException(status_code=400, detail=f"Aparcadero's can't be the same")

    buses = BusController(db)
    results = buses.register_bus(municipio_origen, municipio_destino)

    if isinstance(results, dict):
        raise HTTPException(status_code=404, detail=f"Municipio's not found. More details: {str(results['error'])}")

    if results is None:
        raise HTTPException(status_code=400, detail=f"Aparcadero on municipio_id[{municipio_origen}] is full")
    
    return results

@router_bus.patch("/api/bus/enrutar", tags=["bus"], response_model=schemas.Bus)
async def routing_bus(bus_id: int, municipio_origen: int, municipio_destino: int, db: Session = Depends(get_db)):
    buses = BusController(db)
    results = buses.routing_bus(bus_id, municipio_origen, municipio_destino)

    if results is None:
        raise HTTPException(status_code=400, detail=f"Bus on bus_id[{bus_id}] not found")
    
    return results