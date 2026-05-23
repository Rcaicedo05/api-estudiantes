from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="API Estudiantes", version="1.0.0")

class Estudiante(BaseModel):
    id: int
    nombre: str
    correo: str
    programa: str

estudiantes_db: List[Estudiante] = []

@app.get('/estudiantes')
def listar_estudiantes():
    return estudiantes_db

@app.post('/estudiantes', status_code=201)
def crear_estudiante(est: Estudiante):
    estudiantes_db.append(est)
    return est

@app.get('/estudiantes/{id}')
def obtener_estudiante(id: int):
    for e in estudiantes_db:
        if e.id == id:
            return e
    raise HTTPException(404, 'Estudiante no encontrado')

@app.delete('/estudiantes/{id}', status_code=204)
def eliminar_estudiante(id: int):
    global estudiantes_db
    antes = len(estudiantes_db)
    estudiantes_db = [e for e in estudiantes_db if e.id != id]
    if len(estudiantes_db) == antes:
        raise HTTPException(404, 'Estudiante no encontrado')
    return None