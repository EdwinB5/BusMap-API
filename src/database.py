from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

USER = os.environ.get('BM_USER')
PASSWORD = os.environ.get('BM_PASSWORD')
HOST = os.environ.get('BM_HOST')
PORT = os.environ.get('BM_PORT')
DB = os.environ.get('BM_DB')

SQLALCHEMY_DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

metadata = MetaData()
metadata.reflect(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(metadata=metadata)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()