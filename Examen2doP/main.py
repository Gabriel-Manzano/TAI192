from fastapi import FastAPI,HTTPException
from typing import Optional,List
from models import modeloConductor

app=FastAPI()

conductores=[
    {"Nombre": "Ash", "TipoDeLicencia": "A", "NoLicencia": "QWERASDFZXC1"},
    {"Nombre": "Dawn", "TipoDeLicencia": "B", "NoLicencia": "TYUIGHJKBNM2"},
    {"Nombre": "Helio", "TipoDeLicencia": "C", "NoLicencia": "ZXCVASDFQWE3"},
    {"Nombre": "Venus", "TipoDeLicencia": "D", "NoLicencia": "BNMMGHJKTYU4"},
]

# Endpoint mostrar conductores
@app.get('/mostrar', tags=['Mostrar'])
def mostrar():
    return conductores

# Endpoint para agregar un conductor

@app.post('/agregar/', response_model=modeloConductor, tags=['Agregar'])
def agregar(conductor: modeloConductor):
    for con in conductores:
        if con["NoLicencia"] == conductor.NoLicencia:
            raise HTTPException(status_code=400, detail="El conductor ya existe!!!")
    
    conductores.model_dump()
    return conductor


# Endpoint para editar un conductor

@app.put('/editar/{NoLicencia}', response_model=modeloConductor, tags=['Editar'])
def editar(NoLicencia: str, conductorActualizado: modeloConductor):
    for index, con in enumerate(conductores):
        if con["NoLicencia"] == NoLicencia:
            conductores[index] = conductorActualizado.model_dump()
            return conductores[index]
    
    raise HTTPException(status_code=400, detail="El conductor no existe!!!")
