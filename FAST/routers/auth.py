from fastapi.responses import JSONResponse
from modelsPydantic import modeloAuth
from genToken import createToken
#from middlewares import BearerJWT
from fastapi import APIRouter

routerAuth = APIRouter()

# Endpoitn de autentificación

@routerAuth.post('/auth', tags=['Autentificación'])
def login(autorizacion:modeloAuth):
    if autorizacion.email == 'gabriel.mzn.r.xx66@example.com' and autorizacion.passw =='123456789':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return{"Aviso: Usuario no autorizado"}