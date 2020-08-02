from fastapi import status


def test_auth_redirect(client, mocker):
    response = client.get("/auth/nctu", allow_redirects=False)
    assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT

    target_redirect_url = "https://id.nctu.edu.tw/o/authorize/?client_id=TestingClientId&response_type=code&scope=profile"
    assert response.headers["Location"] == target_redirect_url
