from common.allure_requests import AllureRequests

url = "https://reqres.in/api/login"
ar = AllureRequests(url)


def test_positive():
    response = ar.get("1")
    assert response.status_code == 200
    data = response.text
    assert 'data' in data


def test_negative():
    response = ar.post("1")
    assert response.status_code == 400
