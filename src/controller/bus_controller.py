from src import models, schemas
from src.controller.ruta_controller import RutaController
from src.utils import geometry
import random
from datetime import datetime, timedelta

class BusController:
    def __init__(self, session):
        self.db = session
    
    def get_buses(self, skip: int = 0, limit: int = 1000):
        buses = self.db.query(models.Bus).offset(skip).limit(limit).all()
        return self.format_buses(buses)

    def get_buses_by_municipio(self, municipio_id):
        results = {}
        municipio = self.db.query(models.Municipio).filter(models.Municipio.id == municipio_id).first()
        
        try:
            if municipio.tiene_aparcadero:
                buses_municipio = self.db.query(models.Bus).join(models.MunicipioBus).filter(models.MunicipioBus.id_municipio == municipio_id).all()
                results = buses_municipio
        except:
            results = {}

        return self.format_buses(results)

    def register_bus(self, municipio_origen: int, municipio_destino: int):
        result = None

        municipio = self.db.query(models.Municipio).filter(models.Municipio.id == municipio_origen).first()
        simulacion = self.db.query(models.Simulacion).first()

        try:
            if municipio.capacidad_maxima > municipio.capacidad_actual:
                
                ruta = RutaController(self.db)

                bus_localizacion = geometry.convert_wkb_to_string(municipio.localizacion)
                estado = "aparcado"
                fecha_salida = self.add_aparcadero_time(simulacion.tiempo, 30)
                print(fecha_salida)
                cupos_maximos = random.randint(20, 40)
                cupos_actuales = random.randint(1, cupos_maximos)
                velocidad_promedio = random.randint(60, 80)

                fk_ruta = ruta.get_ruta(municipio_origen, municipio_destino)

                db_bus = models.Bus(localizacion=bus_localizacion, estado=estado, fecha_salida=fecha_salida, cupos_maximos=cupos_maximos, cupos_actuales=cupos_actuales, velocidad_promedio=velocidad_promedio, fk_ruta=fk_ruta)
                self.db.add(db_bus)
                self.db.commit()

                self.db.refresh(db_bus)

                # Aumentar capacidad actual del aparcadero
                municipio.capacidad_actual += 1

                db_bus_municipio = models.MunicipioBus(id_municipio=municipio.id, id_bus=db_bus.id)
                self.db.add(db_bus_municipio)
                self.db.commit()
                
                self.db.refresh(db_bus_municipio)

                result = db_bus
                result.localizacion = geometry.wkt_str_to_point(geometry.convert_wkb_to_string(result.localizacion))
        except Exception as error:
            result = {"error": error}

        return result

    def routing_bus(self, bus_id: int, municipio_origen:int , municipio_destino: int):
        bus = self.db.query(models.Bus).filter(models.Bus.id == bus_id).first()
        simulacion = self.db.query(models.Simulacion).first()
        if bus is None: return None

        ruta = RutaController(self.db)
        ruta_update = ruta.get_ruta(municipio_origen, municipio_destino)

        # Bus Update fields
        bus.fk_ruta = ruta_update
        bus.fecha_salida = self.add_aparcadero_time(simulacion.tiempo, 30)
        bus.estado = "aparcado"
        # bus.fecha_entrada = simulacion.tiempo
        bus.cupos_actuales = random.randint(1, bus.cupos_maximos)
        bus.velocidad_promedio = random.randint(60, 80)

        # Bus Municipio update
        bus_municipio = self.db.query(models.MunicipioBus).filter(models.MunicipioBus.id_bus == bus_id).first()
        bus_municipio.id_municipio = municipio_origen
            
        self.db.commit()
        self.db.refresh(bus)
        self.db.refresh(bus_municipio)

        return self.format_buses(bus)[0]

    def format_buses(self, buses):
        results = {}
        
        if isinstance(buses, list):
            for bus in buses:
                bus.localizacion = geometry.wkt_str_to_point(geometry.convert_wkb_to_string(bus.localizacion))
            results = buses

        if isinstance(buses, models.Bus):
            buses.localizacion = geometry.wkt_str_to_point(geometry.convert_wkb_to_string(buses.localizacion))
            results = [buses]
        
        return results
    
    def add_aparcadero_time(self, fecha, minutos):
        fecha_salida = datetime.strptime(str(fecha), "%Y-%m-%d %H:%M:%S%z")
        return fecha_salida + timedelta(minutes=minutos)
    