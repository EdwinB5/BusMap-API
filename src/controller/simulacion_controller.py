from src import models, schemas

class SimulacionController:
    def __init__(self, session):
        self.db = session

    def get_simulacion(self):
        return self.db.query(models.Simulacion).first()