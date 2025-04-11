import os

os.environ["DB_URL"] = "sqlite:///:memory:"
os.environ["ENV"] = "testing"

import pytest
from src.main import app
from src.models.blacklist import Base
from src.session import engine

@pytest.fixture(scope="module")
def test_client():
    app.config["TESTING"] = True
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)
