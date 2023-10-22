from src import models

class SimulacionController:
    def __init__(self, session):
        self.db = session

    def get_simulacion(self):
        return self.db.query(models.Simulacion).first()
    
    def update_simulacion(self, simulacion_id, simulacion_update):
        simulacion = self.db.query(models.Simulacion).filter(models.Simulacion.id == simulacion_id).first()
        if simulacion is None: return None
        
        update_data = simulacion_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(simulacion, key, value)
            
        self.db.commit()
        self.db.refresh(simulacion)
        
        return simulacion