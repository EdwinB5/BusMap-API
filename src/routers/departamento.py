from fastapi import APIRouter
from src.controller.departamento_controller import DepartamentoController

router_departamento = APIRouter()

@router_departamento.get("/api/departamento", response_model=None, tags=['departamento'])
async def read_departamento():
    departamento = DepartamentoController()
    return departamento.get_departamento()
