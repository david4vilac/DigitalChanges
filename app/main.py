#Python
from typing import List
import uuid

#FastAPI
from fastapi import status
from fastapi import FastAPI
from fastapi import Body
from fastapi import HTTPException
from fastapi import Depends

#Local
from . import models, schemas, create_person
from . import database as db
from .mutant import is_mutant

#Database
from .database import engine
from sqlalchemy.orm import Session


app = FastAPI()


@app.get("/",
         status_code=status.HTTP_200_OK,
         tags=["Home"],
         response_model=schemas.Mutant,
         summary="Presentación Magneto.")
def home():
    """
    Aquí se Presenta la Bienvenida de **Magneto.**
    """
    return {"Hello": "World"}


@app.post("/mutant/",
          status_code=status.HTTP_200_OK,
          tags=["Nivel 2"],
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
          tags=["Nivel 3"],
          response_model=schemas.Person,
          status_code=status.HTTP_200_OK,
          summary="Registrar mutante en la BD")
def create_mutant(person:schemas.Person=Body(...),
                  db:Session=Depends(db.get_db)):
    dna_comprobator = person.dna
    if is_mutant(dna_comprobator) == None:
        raise HTTPException(status_code=403, detail="403 Forbidden !")
    if create_person.validation(db=db, dna=dna_comprobator) == True:
        raise HTTPException(status_code=403, detail="Person in db")
    create_person.create_person_function(db=db, person=schemas.Person(dna=person.dna))

@app.get('/stats',
         tags=["Nivel 3"],
         status_code=status.HTTP_200_OK,
         summary="Consulta estadisticas de la BD."
         )
def get_user(db: Session=Depends(db.get_db)):
    """
    **Returns:** Devuelve un Json con las estadísticas de las verificaciones de ADN.
    """
    count_muntant_dna = db.query(models.Mutant).count()
    count_human_dna = db.query(models.Human).count()
    total = count_human_dna + count_muntant_dna
    if total != 0:
        ratio = count_muntant_dna/(count_muntant_dna + count_human_dna)
        return {"count_mutant_dna":count_muntant_dna, "count_human_dna":count_human_dna, "ratio":ratio}

@app.get('/list_mutants',
         tags=["Nivel 3"],
         status_code=status.HTTP_200_OK,
         summary="Lista mutantes registrados."
         )
def get_user(db: Session=Depends(db.get_db)):
    """
    Returns: Mutantes registrados en la BD.
    """
    return db.query(models.Mutant).all()


models.Base.metadata.create_all(bind=engine)