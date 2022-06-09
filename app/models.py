from sqlalchemy import Column, String, ARRAY
from .database import Base 


class Human(Base):
    __tablename__ = "human"
    id = Column(String, primary_key=True, index=True)
    dna = Column(ARRAY(String), index=True, unique=True)

    

class Mutant(Base):
    __tablename__ = "mutant"
    id = Column(String, primary_key=True, index=True)
    dna = Column(ARRAY(String), index=True, unique=True)