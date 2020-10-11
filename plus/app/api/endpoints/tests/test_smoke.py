import pytest


@pytest.mark.smoke
def test_backend_start_success(client):
    res = client.get("/")
    assert res.status_code == 200
