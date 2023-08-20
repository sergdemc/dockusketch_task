from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_root_pos():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Everybody be cool"


def test_get_your_job_pos():
    response = client.get("/jobs/1")
    assert response.status_code == 200
    assert response.json() == "Your job is: Virtual Reality Designer"


def test_get_your_job_neg():
    response = client.get("/jobs/l")
    assert response.status_code == 422
    expected_resp = {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["path", "job_id"],
                "msg": "Input should be a valid integer, "
                       "unable to parse string as an integer",
                "input": "l",
                "url": "https://errors.pydantic.dev/2.2/v/int_parsing"
            }
        ]
    }
    assert response.json() == expected_resp
