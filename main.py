from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from src.routers import municipio, simulacion

#models.Base.metadata.create_all(bind=engine)
#models.Base.metadata.drop_all(engine)

app = FastAPI()

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

@app.get("/api/")
async def root():
    return {"message": "BusMap API - Welcome"}



