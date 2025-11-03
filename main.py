from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

libros = []

@app.get("/")
def index():
    return {"message": "Hola Pythonianos"}

@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"data": id}


@app.get("/libros")
def mostrar_libros():
    return {"data": libros}

@app.post("/libros")
def insertar_libro(libro: Libro):
    libros.append(libro)
    return {"message": f"libro {libro.titulo} insertado"}