from common.allure_requests import AllureRequests

url = "https://httpbin.org/drip"
ar = AllureRequests(url)


def test_positive1():
    response = ar.get({"duration": 2, "numbytes": 10, "code": 200, "delay": 2})
    assert response.status_code == 200


def test_positive2():
    response = ar.post({"duration": 2, "numbytes": 10, "code": 200, "delay": 2})
    assert response.status_code == 200


def test_negative1():
    body = {
        "username": "string",
        "email": "1",
        "password": "string"
    }
    response = ar.post(body)
    assert response.status_code == 405


def test_negative2():
    body = {
        "username": "string",
        "email": "2",
        "password": "string"
    }
    response = ar.post(body)
    assert response.status_code == 405
