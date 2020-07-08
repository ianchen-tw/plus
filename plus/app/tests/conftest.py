# Conftest: test configurations
#   Setup some common Fixtures

from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import server
from app.tests.utils.session import TestingSessionLocal


@pytest.fixture(scope="session")
def db() -> Generator:
    yield TestingSessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(server) as c:
        yield c
