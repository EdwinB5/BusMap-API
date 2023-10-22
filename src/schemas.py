from typing import List, Optional, Tuple, Union
from pydantic import BaseModel
import datetime

# Modelos esquemas

class MunicipioBase(BaseModel):
    nombre: str
    localizacion: Optional[str]
    extension: Optional[str]
    tiene_aparcadero: Optional[bool]
    capacidad_maxima: Optional[int]
    capacidad_actual: Optional[int]
    buses_no_disponibles: Optional[int]
    buses_disponibles: Optional[int]

class RutaBase(BaseModel):
    distancia_total: float
    ruta_trazada: str
    distancias: List[float]
    municipio_origen: int
    municipio_destino: int

class BusBase(BaseModel):
    localizacion: str
    estado: str
    fecha_salida: str
    fecha_entrada: str
    fecha_disponible: str
    cupos_maximos: int
    cupos_actuales: int
    velocidad_promedio: int
    distancia_actual: float
    tiempo_viaje: float
    indice_ruta: int

class SimulacionBase(BaseModel):
    multiplicador: int
    maximo_viaje: int
    aumento_tiempo: int
    aumento_real: int
    tiempo: datetime.datetime
    estado: str

class MunicipioBusBase(BaseModel):
    id_municipio: int
    id_bus: int


class Municipio(MunicipioBase):
    id: int

    class Config:
        orm_mode = True

class RutaCreate(RutaBase):
    pass

class Ruta(RutaBase):
    id: int

    class Config:
        orm_mode = True

class BusCreate(BusBase):
    pass

class Bus(BusBase):
    id: int

    class Config:
        orm_mode = True

class Simulacion(SimulacionBase):
    id: int

    class Config:
        orm_mode = True

class MunicipioBusCreate(MunicipioBusBase):
    pass

class MunicipioBus(MunicipioBusBase):
    pass
