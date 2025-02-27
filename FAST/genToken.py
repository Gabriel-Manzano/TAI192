import jwt

def createToken(datos:dict):
    token:str= jwt.encode(payload=datos,key='secretkey', agorithm='HS256')
    return token
    