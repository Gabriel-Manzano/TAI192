from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from typing import Optional,List
from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from DB.conexion import Session,engine,Base
from models.modelsDB import User


app= FastAPI(
    title= 'Mi primerAPI 192',
    description= 'Gabriel Manzano Ruíz',
    version= '1.0.1'
)

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

# Endpoitn de autentificación
@app.post('/auth', tags=['Autentificación'])
def login(autorizacion:modeloAuth):
    if autorizacion.email == 'gabriel.mzn.r.xx66@example.com' and autorizacion.passw =='123456789':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return{"Aviso: Usuario no autorizado"}

# Endponit CONSULTA TODOS
@app.get('/TodosUsuarios', response_model= List[modeloUsuario], tags=['Operaciones CRUD'])
def leerUsuarios():
    return usuarios

# Endponit Agregar nuevos
@app.post('/usuarios/', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuarios(usuario:modeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
            
    usuarios.append(usuario)
    return usuario

# Endponit Actualizar
@app.put('/usuarios/{id}', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def actualizarUsuarios(id:int,usuarioActualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]= usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

# Endponit Eliminar
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminarUsuarios(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {"Los usuarios existentes restantes son": usuarios}
    raise HTTPException(status_code=400, detail="El usuario no existe")