import pytest
import requests

@pytest.fixture(params=["","cleaning_business.html"])
def test_url(request):
    return f"http://localhost:5500/{request.param}"

def test_project_status_code(test_url):
    response = requests.get(test_url)
    assert response.status_code == 200
