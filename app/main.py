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

models.Base.metadata.create_all(bind=engine)

from app.mutant import is_mutant

import uuid
"""
class Mutant(BaseModel):
    dna: List[str] = 


"""

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
        raise HTTPException(status_code=403, detail="Item not found")
    return mutant


@app.post("/mutantDB/",
          tags=["Mutant"],
          response_model=schemas.Mutant,
          status_code=status.HTTP_200_OK,
          summary="Registrar mutante en la DB")
def create_mutant(entrada:schemas.Person, db:Session=Depends(db.get_db)):
    id = uuid.uuid4()
    dna_comprobator = entrada.dna
    if is_mutant(dna_comprobator) == True:
        mutant = models.Mutant(id=str(id), dna=entrada.dna)
        db.add(mutant)
        db.commit()
        db.refresh(mutant)
        print("Registro Mutante")
        return mutant
    else:
        human = models.Human(id = str(id), dna=entrada.dna)
        db.add(human)
        db.commit()
        db.refresh(human)
        print("Registro Humano")
        return human


