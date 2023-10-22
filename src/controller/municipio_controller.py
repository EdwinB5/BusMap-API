from src import models
from src.utils import geometry
from src.utils.geojson import municipio_geojson

class MunicipioController:
    def __init__(self, session):
        self.db = session
    
    def get_municipio_by_id(self, municipio_id):
        return self.db.query(models.Municipio).filter(models.Municipio.id == municipio_id).first()
    
    def get_municipio_by_name(self, municipio_nombre):
        return self.db.query(models.Municipio).filter(models.Municipio.nombre == municipio_nombre).first()
    
    def get_municipio_by_aparcadero(self):
        return self.db.query(models.Municipio).filter(models.Municipio.tiene_aparcadero).all()

    def get_municipios(self, skip: int = 0, limit: int = 1000):
        municipios = self.db.query(models.Municipio).offset(skip).limit(limit).all()

        for municipio in municipios:
            municipio.localizacion = geometry.wkt_str_to_point(geometry.convert_wkb_to_string(municipio.localizacion))
            municipio.extension = geometry.wkt_to_poligons(geometry.convert_wkb_to_string(municipio.extension))
        return municipio_geojson(municipios)

