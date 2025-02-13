from fastapi import FastAPI
from typing import Optional

app= FastAPI(
    title= 'Repaso API N.1',
    description= 'Gabriel Manzano Ruíz',
    version= '1.0.1'
)

tareas=[
    {"id": 1, "titulo":"Captura", "descripcion":"Atrapar tu primer pokemon", "vencimiento":"12-02-2025", "estado":"completada"},
    {"id": 2, "titulo":"Combate", "descripcion":"Tener tu primer combate pokemon", "vencimiento":"13-02-2025", "estado":"completada"},
    {"id": 3, "titulo":"Sanar", "descripcion":"Ir al centro pokemon", "vencimiento":"15-05-2025", "estado":"no completada"},
    {"id": 4, "titulo":"Fin", "descripcion":"Derrota a Arceus", "vencimiento":"16-05-2025", "estado":"no completada"}
]

#Endponit Obtener tareas
@app.get('/TodasTareas', tags=['CRUD'])
def consultarTareas():
    return{"Las lista de tareas es la siguente": tareas}

