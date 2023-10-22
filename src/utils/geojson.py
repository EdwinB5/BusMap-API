def municipios_geojson(municipios):
    geojson_list = []
    
    for municipio in municipios:
        geometry = {
            "type": "GeometryCollection",
            "coordinates": {
                "Point": {
                    "type": "Point",
                    "coordinates": municipio.localizacion
                },
                "MultiPolygon": {
                    "type": "MultiPolygon",
                    "coordinates": municipio.extension
                }
            }
        }
        properties = {
            "nombre": municipio.nombre,
            "buses_disponibles": municipio.buses_disponibles,
            "buses_no_disponibles": municipio.buses_no_disponibles,
            "capacidad_actual": municipio.capacidad_actual,
            "capacidad_maxima": municipio.capacidad_maxima,
            "id": municipio.id,
            "aparcadero": municipio.tiene_aparcadero
        }
        feature = {
            "type": "Feature",
            "properties": properties,
            "geometry": geometry
        }
        geojson_list.append(feature)

    return {
        "type": "FeatureCollection",
        "features": geojson_list
    }

def municipio_geojson(municipio):
    geometry = {
            "type": "GeometryCollection",
            "coordinates": {
                "Point": {
                    "type": "Point",
                    "coordinates": municipio.localizacion
                },
                "MultiPolygon": {
                    "type": "MultiPolygon",
                    "coordinates": municipio.extension
                }
            }
        }
    
    properties = {
        "nombre": municipio.nombre,
        "buses_disponibles": municipio.buses_disponibles,
        "buses_no_disponibles": municipio.buses_no_disponibles,
        "capacidad_actual": municipio.capacidad_actual,
        "capacidad_maxima": municipio.capacidad_maxima,
        "id": municipio.id,
        "aparcadero": municipio.tiene_aparcadero
    }
    
    feature = {
        "type": "Feature",
        "properties": properties,
        "geometry": geometry
    }
    
    return {
        "type": "FeatureCollection",
        "features": feature
    }
    

def departamento_geojson(departamento):
    geojson = {
            "type": "Feature",
            "properties": {
                "nombre": departamento["departamento"],  
            },
            "geometry": {
                "type": "MultiPolygon",
                "coordinates": departamento["extension"],
            }
        }
    return geojson
