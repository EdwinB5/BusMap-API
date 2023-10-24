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
    localizacion: Optional[List[float]] | None = None
    estado: str | None = None
    fecha_salida: datetime.datetime | None = None
    fecha_entrada: datetime.datetime | None = None
    fecha_disponible: datetime.datetime | None = None
    cupos_maximos: int | None = None
    cupos_actuales: int | None = None
    velocidad_promedio: int | None = None
    distancia_actual: float | None = None
    tiempo_viaje: float | None = None
    indice_ruta: int | None = None
    fk_ruta: int | None = None
    distancia_teorica: float | None = None

class BusCreate(BaseModel):
    fecha_salida: datetime.datetime

class BusUpdate(BaseModel):
    fecha_salida: datetime.datetime

class MunicipioBusBase(BaseModel):
    id_municipio: int
    id_bus: int

class Municipio(MunicipioBase):
    id: int

    class Config:
        from_attributes = True

class RutaCreate(RutaBase):
    pass

class Ruta(RutaBase):
    id: int | None = None

    class Config:
        from_attributes = True

class Bus(BusBase):
    id: int

    class Config:
        from_attributes = True

class SimulacionBase(BaseModel):
    multiplicador: int | None = None
    maximo_viaje: int | None = None
    aumento_tiempo: int | None = None
    aumento_real: int | None = None
    tiempo: datetime.datetime | None = None
    estado: str | None = None
    
class Simulacion(SimulacionBase):
    id: int | None = None

    class Config:
        from_attributes = True

class MunicipioBusCreate(MunicipioBusBase):
    pass

class MunicipioBus(MunicipioBusBase):
    pass
