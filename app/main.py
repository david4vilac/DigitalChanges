from typing import List



from fastapi import status
from fastapi import FastAPI
from fastapi import Body
from fastapi import HTTPException
from fastapi import Depends


from . import models, schemas, create_person
from . import database as db
from .database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session

from app.mutant import is_mutant

models.Base.metadata.create_all(bind=engine)



import uuid


app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/mutant/",
          status_code=status.HTTP_200_OK,
          tags=["Mutant"],
          response_model=schemas.Mutant,
          summary="Ingresa el ADN.")
def validation_mutant(mutant:schemas.Mutant = Body(...)):
    """
    *Verificar si es mutante o no.*

    """
    if is_mutant(mutant.dna) != True:
        raise HTTPException(status_code=403, detail="Not a Mutant !")
    return mutant





@app.post("/mutantDB/",
          tags=["DataBase"],
          response_model=schemas.Mutant,
          status_code=status.HTTP_200_OK,
          summary="Registrar mutante en la BD")
def create_mutant(entrada:schemas.Person=Body(...), db:Session=Depends(db.get_db)):
    id = uuid.uuid4()
    dna_comprobator = entrada.dna
    if is_mutant(dna_comprobator) == None:
        raise HTTPException(status_code=403, detail="403 Forbidden !")
    elif is_mutant(dna_comprobator) == True:
        mutant = models.Mutant(id=str(id), dna=entrada.dna)
        db.add(mutant)
        db.commit()
        db.refresh(mutant)
        print("Registro Mutante")
        return mutant
    elif is_mutant(dna_comprobator) == False:
        human = models.Human(id = str(id), dna=entrada.dna)
        db.add(human)
        db.commit()
        db.refresh(human)
        print("Registro Humano")
        return human

@app.get('/list_mutants')
def get_user(db: Session=Depends(db.get_db)):
    return db.query(models.Human).all()


@app.get('/stats')
def get_user(db: Session=Depends(db.get_db)):
    count_muntant_dna = db.query(models.Mutant).count()
    count_human_dna = db.query(models.Human).count()
    ratio = count_muntant_dna/(count_muntant_dna + count_human_dna)
    return {"count_mutant_dna":count_muntant_dna, "count_human_dna":count_human_dna, "ratio":ratio}


