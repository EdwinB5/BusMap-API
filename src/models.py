from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float, Sequence
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from .database import Base


class Municipio(Base):
    __tablename__ = "municipio"

    id = Column(Integer, Sequence('municipio_id_seq'), primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    localizacion = Column(Geometry('POINT', 4326))
    extension = Column(Geometry('MULTIPOLYGON', 4326), nullable=False)
    tiene_aparcadero = Column(Boolean, nullable=False)
    capacidad_maxima = Column(Integer)
    capacidad_actual = Column(Integer)
    buses_no_disponibles = Column(Integer)
    buses_disponibles = Column(Integer)

    __table_args__ = {'extend_existing': True}


class Ruta(Base):
    __tablename__ = "ruta"

    id = Column(Integer, Sequence('ruta_id_seq'), primary_key=True)
    distancia_total = Column(Float, nullable=False)
    ruta_trazada = Column(Geometry('LINESTRING', 4326), nullable=False)
    distancias = Column(ARRAY(Float))

    municipio_origen = Column(Integer, ForeignKey('municipio.id'), nullable=False)
    municipio_destino = Column(Integer, ForeignKey('municipio.id'), nullable=False)

    __table_args__ = {'extend_existing': True}



class Bus(Base):
    __tablename__ = "bus"

    id = Column(Integer, Sequence('bus_id_seq'), primary_key=True, index=True)
    localizacion = Column(Geometry('POINT', 4326), nullable=False)
    estado = Column(String, nullable=False)
    fecha_salida = Column(DateTime)
    fecha_entrada = Column(DateTime)
    fecha_disponible = Column(DateTime)
    cupos_maximos = Column(Integer)
    cupos_actuales = Column(Integer)
    velocidad_promedio = Column(Integer, nullable=False)
    distancia_actual = Column(Float, default=0)
    tiempo_viaje = Column(Float, default=0)

    indice_ruta = Column(Integer, default=0)
    fk_ruta = Column(Integer, ForeignKey('ruta.id'))
    distancia_teorica = Column(Float, default=0)

    __table_args__ = {'extend_existing': True}


class Simulacion(Base):
    __tablename__ = "simulacion"

    id = Column(Integer, Sequence('simulacion_id_seq'), primary_key=True, index=True)
    multiplicador = Column(Integer, nullable=False)
    maximo_viaje = Column(Integer, nullable=False)
    aumento_tiempo = Column(Integer, nullable=False)
    aumento_real = Column(Integer, nullable=False)
    tiempo = Column(DateTime, nullable=False)
    estado = Column(String, nullable=False)

    __table_args__ = {'extend_existing': True}


class MunicipioBus(Base):
    __tablename__ = "municipio_bus"

    id_municipio = Column(Integer, ForeignKey('municipio.id'), nullable=True, primary_key=True, unique=False)
    id_bus = Column(Integer, ForeignKey('bus.id'), nullable=True, primary_key=True, unique=False)

    __table_args__ = {'extend_existing': True}