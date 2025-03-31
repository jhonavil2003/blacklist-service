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
        db_url = os.getenv("DB_URL")
        if db_url:
            return db_url
        db_user = os.environ['DB_USER']
        db_pass = os.environ['DB_PASSWORD']
        db_host = os.environ['DB_HOST']
        db_port = os.environ['DB_PORT']
        db_name = os.environ['DB_NAME']
        return f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

session_config = SessionConfig()
engine = create_engine(session_config.url())

Base.metadata.bind = engine
Session = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(engine)
