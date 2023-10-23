from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import municipio, simulacion, departamento, bus
from fastapi.openapi.docs import get_swagger_ui_html

#models.Base.metadata.create_all(bind=engine)
#models.Base.metadata.drop_all(engine)

description = """
BusAPI Map API for recovery database info
"""

tags_metadata = [
    {
        "name": "municipios",
        "description": "Operations with municipios. The **Municipios** logic is also here."
    },
    {
        "name": "simulacion",
        "description": "Operations with simulacion. The **Simulacion** logic is also here."
    },
    {
        "name": "departamento",
        "description": "**Departamento** info"
    },
    {
        "name": "bus",
        "description": "Operations with buses. The **Bus** logic is also here."
    },
]

app = FastAPI(title='BusMap API', description=description, license_info={
    "name": "MIT",
    "url": "http://kb.mit.edu/confluence/x/NwmVCQ",
}, openapi_tags=tags_metadata, openapi_url="/api/openapi.json")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(municipio.router_municipio)
app.include_router(simulacion.router_simulacion)
app.include_router(departamento.router_departamento)
app.include_router(bus.router_bus)

@app.get("/api/")
async def root():
    return {"message": "BusMap API - Welcome"}

@app.get("/api/docs")
async def custom_swagger():                                                                                                                      
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title="BusMap Api Docs")



