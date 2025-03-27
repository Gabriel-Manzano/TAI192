from fastapi import FastAPI
from DB.conexion import engine,Base
from routers.usuario import routerUsuario
from routers.auth import routerAuth

#from fastapi import FastAPI,HTTPException
#from fastapi.responses import JSONResponse
#from fastapi.encoders import jsonable_encoder
#from typing import Optional,List
#from modelsPydantic import modeloUsuario, modeloAuth
#from genToken import createToken
#from DB.conexion import Session,engine,Base
#from models.modelsDB import User
#from fastapi import APIRouter

app= FastAPI(
    title= 'Mi primerAPI 192',
    description= 'Gabriel Manzano Ruíz',
    version= '1.0.1'
)

app.include_router(routerUsuario)
app.include_router(routerAuth)

Base.metadata.create_all(bind=engine)

# BD ficticia
#usuarios=[
#    {"id": 1,"nombre":"ivan", "edad":37, "correo":"ivan@gmail.com"},
#    {"id": 2, "nombre":"isay", "edad":15, "correo":"isay@gmail.com"},
#    {"id": 3, "nombre":"luis", "edad":18, "correo":"luis@gmail.com"},
#    {"id": 4, "nombre":"ana", "edad":37, "correo":"ana@gmail.com"}
#]

# Endponit home

@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello':'Hello World'}