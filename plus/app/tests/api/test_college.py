from typing import Dict


def filter_dict(template: Dict, src: Dict):
    """
    filter `src` with only fields contains in `template`
    """
    return {k: v for k, v in src.items() if k in template.keys()}


# TODO:read, update

# CREATE
def test_create_college_success(client):
    college = {"name": "MATH", "code": "M"}
    response = client.post("/college/", json=college)
    assert response.status_code == 200


def test_create_college_return_provided_fields(client):
    college = {"name": "CSE", "code": "AX"}

    response = client.post("/college/", json=college)
    assert response.status_code == 200
    res = response.json()
    assert college == filter_dict(college, res)


def test_create_college_filter_on_additional_fields(client):
    specious_field = "SOME_STRANGE_FIELDS_WE_DONT_WANT"
    college = {
        "name": "Normal",
        "code": "n",
        specious_field: "HEHEHEHE",
    }
    response = client.post("/college/", json=college)
    assert response.status_code == 200
    assert specious_field not in response.json().keys()


def test_delete_colleges(client):
    college = {"name": "Artificial Intelligence", "code": "AI"}
    response = client.post("/college/", json=college)
    assert response.status_code == 200

    college_id = response.json()["id"]
    client.delete(f"/college/{college_id}")
    assert response.status_code == 200

    least_info = {**college, "id": college_id}
    assert least_info == filter_dict(least_info, response.json())
