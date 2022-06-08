from typing import List

from pydantic import BaseModel, Field

from fastapi import status
from fastapi import FastAPI
from fastapi import Body
from fastapi import HTTPException
from app.mutant import is_mutant


class Mutant(BaseModel):
    dna: List[str] = Field(...,
                     example=["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
                     )

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post(path="/mutant/",
          status_code=status.HTTP_200_OK,
          tags=["Mutant"],
          response_model=Mutant,
          summary="Ingresa el ADN.")
def validation_mutant(mutant: Mutant = Body(...)):
    """
    *Verificar si es mutante o no.*

    """
    if is_mutant(mutant.dna) != True:
        raise HTTPException(status_code=403, detail="Item not found")
    return mutant

