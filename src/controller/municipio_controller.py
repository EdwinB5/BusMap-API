from src import models
from src.utils import geometry
from src.utils.geojson import municipios_geojson, municipio_geojson

class MunicipioController:
    def __init__(self, session):
        self.db = session
    
    def get_municipio_by_id(self, municipio_id):
        municipio = self.db.query(models.Municipio).filter(models.Municipio.id == municipio_id).first()
        return self.format_municipios(municipio)
    
    def get_municipio_by_name(self, municipio_nombre):
        municipio = self.db.query(models.Municipio).filter(models.Municipio.nombre == municipio_nombre).first()
        return self.format_municipios(municipio)
    
    def get_municipio_by_aparcadero(self, aparcadero):
        municipios = self.db.query(models.Municipio).filter(models.Municipio.tiene_aparcadero == aparcadero).all()
        return self.format_municipios(municipios)

    def get_municipios(self, skip: int = 0, limit: int = 1000):
        municipios = self.db.query(models.Municipio).offset(skip).limit(limit).all()
        return self.format_municipios(municipios)

    def format_municipios(self, municipios):
        results = {}
        if isinstance(municipios, models.Municipio):
            municipios.localizacion = geometry.wkt_str_to_point(geometry.convert_wkb_to_string(municipios.localizacion))
            municipios.extension = geometry.wkt_to_poligons(geometry.convert_wkb_to_string(municipios.extension))
            results = municipio_geojson(municipios)
        
        if isinstance(municipios, list):
            for municipio in municipios:
                municipio.localizacion = geometry.wkt_str_to_point(geometry.convert_wkb_to_string(municipio.localizacion))
                municipio.extension = geometry.wkt_to_poligons(geometry.convert_wkb_to_string(municipio.extension))
            results = municipios_geojson(municipios)
        
        return results
            

