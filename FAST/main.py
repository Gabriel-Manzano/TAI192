from fastapi import FastAPI,HTTPException
from typing import Optional

app= FastAPI(
    title= 'Mi primerAPI 192',
    description= 'Gabriel Manzano Ruíz',
    version= '1.0.1'
)

usuarios=[
    {"id": 1,"nombre":"ivan", "edad":37},
    {"id": 2, "nombre":"isay", "edad":15},
    {"id": 3, "nombre":"luis", "edad":18},
    {"id": 4, "nombre":"ana", "edad":37}
]

#Endponit home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello':'Hello World'}

#Endponit CONSULTA TODOS
@app.get('/TodosUsuarios', tags=['Operaciones CRUD'])
def leerUsuarios():
    return {"Los usuarios registrados son ": usuarios}

#Endponit Agregar nuevos
@app.post('/usuarios/', tags=['Operaciones CRUD'])
def agregarUsuarios(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El ID ya existe")
            
    usuarios.append(usuario)
    return usuario

#Endponit Actualizar
@app.put('/usuarios/{id}', tags=['Operaciones CRUD'])
def actualizarUsuarios(id:int,usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

#Endponit Eliminar
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminarUsuarios(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {"Los usuarios existentes restantes son": usuarios}
    raise HTTPException(status_code=400, detail="El usuario no existe")