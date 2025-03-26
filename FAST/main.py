from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
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
@app.get('/TodosUsuarios', tags=['Operaciones CRUD'])
def leerUsuarios():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))

    except Exception as e:
        return JSONResponse(status_code=500, content ={"message": "Error al guardar el usuario", "Exception": str(e)})

    finally:
        db.close()

# Endponit Agregar nuevos
@app.post('/usuarios/', response_model= modeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuarios(usuario:modeloUsuario):
    db = Session()
    try: 
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content ={"message": "Usuario Guardado", 
                                                    "usuario": usuario.model_dump()})
 
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content ={"message": "Error al guardar el usuario", "Exception": str(e)})
    finally:
        db.close()


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


#Endpoint buscar por id
@app.get('/usuario/{id}', tags =['Operaciones CRUD'])
def buscarUno(id:int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consultaUno:
            return JSONResponse (status_code=404, content= {"Mensaje":"Usuario no encontrado"})

        return JSONResponse(content= jasonable_encoder(ConsultaUno))

    except Exception as e:
        return JSONResponse(status_code = 500, content={"message":"Error al consultar", "Exception": str(e)})
        
    finally:
        db.close()
