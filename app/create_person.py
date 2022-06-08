from sqlalchemy.orm import Session
from . import models, schemas


def create_person_function(db:Session, mutant: schemas.Mutant):
    db_mutant=models.Mutant(
        dna=mutant.dna,
    )
    db.add(db_mutant)
    db.commit()
    db.refresh(db_mutant)
    return db_mutant