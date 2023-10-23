from geoalchemy2.shape import to_shape
from shapely.geometry import MultiPolygon, Point, LineString
from shapely.wkt import loads


def convert_wkb_to_string(wkb_element):
    if wkb_element is not None:
        shape = to_shape(wkb_element)
        return shape.wkt if shape is not None else None
    return None


def wkt_str_to_point(wkt_str):
    if wkt_str is None: return None

    punto = loads(wkt_str)
    return [punto.x, punto.y]


def wkt_to_poligons(wkt_str):
    if wkt_str is None: return None

    multipoligono = loads(wkt_str)
    poligonos = []
    for poligono in multipoligono.geoms:
        anillos = []
        for anillo in poligono.exterior.coords:
            anillos.append(list(anillo))
        poligonos.append(anillos)
    return poligonos


def array_to_linestring(array):
    linestring = LineString(array)
    return str(linestring)