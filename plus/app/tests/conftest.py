# Conftest: test configurations
#   Setup some common Fixtures

from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


from app.tests.utils.session import TestingSessionLocal
from app.main import server


@pytest.fixture(scope="session")
def db() -> Generator:
    yield TestingSessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(server) as c:
        yield c
