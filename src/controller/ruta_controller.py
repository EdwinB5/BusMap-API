from src import models
from src.utils import geometry

import requests

class RutaController:
    def __init__(self, session):
        self.db = session
    
    def get_ruta(self, municipio_origen, municipio_destino):
        ruta = self.db.query(models.Ruta).filter(models.Ruta.municipio_origen == municipio_origen, models.Ruta.municipio_destino == municipio_destino).first()
        if ruta is None:
            ruta = self.set_ruta(municipio_origen, municipio_destino)

        return ruta.id
    
    def set_ruta(self, municipio_origen, municipio_destino):
        # 0 Latitud / 1 Longitud
        lat_a, lon_a = self.get_point(municipio_origen) 
        lat_b, lon_b = self.get_point(municipio_destino)

        url_api = f"https://router.project-osrm.org/route/v1/driving/{lon_a},{lat_a};{lon_b},{lat_b}?overview=full&geometries=geojson&annotations=distance"
        response = requests.get(url_api)
        data = response.json()

        ruta = self.create_ruta(municipio_origen, municipio_destino, data)

        return ruta 

    def get_point(self, municipio):
        municipio_localizacion = geometry.wkt_str_to_point(geometry.convert_wkb_to_string(municipio.localizacion))
        return municipio_localizacion
    
    def create_ruta(self, municipio_origen, municipio_destino, data):
        distancia_total = data['routes'][0]['distance']
        ruta_trazada = data['routes'][0]['geometry']['coordinates']
        distancias = data['routes'][0]['legs'][0]['annotation']['distance']

        ruta = models.Ruta(distancia_total, ruta_trazada, distancias, municipio_origen, municipio_destino)
        
        self.db.add(ruta)
        self.db.commit()
        self.refresh(ruta)

        return ruta