from pydantic import BaseModel, Field

class modeloUsuario(BaseModel):
    name:str = Field(...,min_length=3, max_length=85, description="Solo letras: min 3 max 85")
    age:int = Field(...,gt=0,lt=125)
    email:str = Field(..., example="gabriel.mzn.xx66@gmail.com", pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


class modeloAuth(BaseModel):
    email:str = Field(..., example="gabriel.mzn.xx66@gmail.com", pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña mínmo 8 caracteres")