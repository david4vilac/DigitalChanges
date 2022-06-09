import uuid
from sqlalchemy.orm import Session
from . import models, schemas
from .mutant import is_mutant


def validation(db:Session, dna: str):
    val_1 = db.query(models.Human).filter(models.Human.dna==dna).first()
    val_2 = db.query(models.Mutant).filter(models.Mutant.dna==dna).first()
    if (val_1 or val_2) != None:
        return True


def create_person_function(db:Session, person:schemas.Person):
    id = uuid.uuid4()
    dna_comprobator = person.dna
    if is_mutant(dna_comprobator) == True:
        db_muntant = models.Mutant(id=str(id), dna=person.dna)
        db.add(db_muntant)
        db.commit()
        db.refresh(db_muntant )
        return {"Registro Mutante"}
    elif is_mutant(dna_comprobator) == False:
        db_human = models.Human(id=str(id), dna=person.dna)
        db.add(db_human)
        db.commit()
        db.refresh(db_human)
        return {"Registro Humano"}