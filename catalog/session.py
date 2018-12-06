from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from SECRETS import POSTGRES_DB_STRING

SQLITE_DB_STING = 'sqlite:///catalog.db?check_same_thread=false'
POSTGRES_DB_STRING = POSTGRES_DB_STRING

engine = create_engine(POSTGRES_DB_STRING)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
