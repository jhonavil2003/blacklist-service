import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from dotenv import load_dotenv
from src.models.blacklist import Base

load_dotenv('.env.development')

class SessionConfig():
    def __init__(self):
        pass

    def url(self):
        return os.environ.get("DB_URL", "sqlite:///:memory:")
    


session_config = SessionConfig()
engine = create_engine(session_config.url())

Base.metadata.bind = engine
Session = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(engine)
