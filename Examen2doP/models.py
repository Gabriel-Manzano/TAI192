from pydantic import BaseModel, Field

# Modelo de Validaciones

class modeloConductor(BaseModel):
    Nombre:str = Field(..., min_length=3 , description="Solo letras: min 3")
    TipoDeLicencia:str = Field(..., max_length=1, description="Solo un carácter")
    NoLicencia:str = Field(..., min_length=12, max_length=12, description="12 caracteres")