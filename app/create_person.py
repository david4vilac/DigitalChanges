from sqlalchemy.orm import Session
from . import models, schemas
from .mutant import is_mutant
import uuid



def create_person_function(db:Session, dna):
    id = uuid.uuid4()
    dna_comprobator = dna
    if is_mutant(dna_comprobator) == True:
        db_muntant = models.Mutant(id=str(id), dna=dna)
        db.add(db_muntant)
        db.commit()
        db.refresh(db_muntant )
        print("Registro Mutante")
        return db_muntant
    elif is_mutant(dna_comprobator) == False:
        db_human = models.Human(id=str(id), dna=dna)
        db.add(db_human)
        db.commit()
        db.refresh(db_human)
        print("Registro Humano")
        return db_human