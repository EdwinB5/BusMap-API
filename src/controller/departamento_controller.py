import json
from src.utils.geojson import departamento_geojson

class DepartamentoController:
    def read_json(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
            
    def get_departamento(self):
        path = './src/data/cundinamarca.geojson'
        data = self.read_json(path)
        
        departamento = {}
        departamento['departamento'] = data['properties']['NAME_1']
        departamento['extension'] = data['geometry']['coordinates']
        
        return departamento_geojson(departamento)