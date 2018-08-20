from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.main import Base

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
# Base.metadata.bind(end)
DBSession = sessionmaker(bind=engine)
session = DBSession()
