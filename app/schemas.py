from pydantic import BaseModel, Field
from typing import List, Optional

class Person(BaseModel):
    dna: List[str] = Field(...,
                     example = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
                            )
    class Config:
        orm_mode = True

class Human(Person):
    id: Optional[str]


class Mutant(Person):
    id: Optional[str]