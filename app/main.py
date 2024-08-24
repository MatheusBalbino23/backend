from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .database import SessionLocal, engine
from . import models, schemas

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

@app.post("/filmes", response_model=schemas.Filme)
def criar_filme(filme: schemas.FilmeCreate):
    db_filme = models.Filme(**filme.dict())
    db.add(db_filme)    
    db.commit()
    db.refresh(db_filme)
    return db_filme

@app.get("/filmes", response_model=List[schemas.Filme])
def listar_filmes():
    filmes = db.query(models.Filme).all()
    return filmes

@app.get("/filmes/{id}", response_model=schemas.Filme)
def obter_filme(id: int):
    filme = db.query(models.Filme).filter(models.Filme.id == id).first()
    if filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme
