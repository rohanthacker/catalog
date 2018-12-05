from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

engine = create_engine('sqlite:///catalog.db?check_same_thread=false')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
