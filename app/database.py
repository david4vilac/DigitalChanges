from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://eolrzaltudmipr:d7bcd13fa27021249c2810f51bcc39a5d0bbf4261f1e7a4ce6e45538131b7532@ec2-52-44-13-158.compute-1.amazonaws.com:5432/d71vti205l5bai"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()