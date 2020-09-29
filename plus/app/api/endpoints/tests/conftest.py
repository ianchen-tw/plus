from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import server


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(server) as c:
        yield c
