import requests
import pytest

@pytest.fixture
def response():
    url = "https://api.github.com/search/repositories"
    url +=  "?q=language:python+sort:stars+stars:>1000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r= requests.get(url, headers = headers)
    return r

def test_status_code(response):
    assert response.status_code == 200
    
def test_total_items(response):
    response_dict = response.json()
    assert response_dict['total_count']>0
    
def test_number_of_results(response):
    response_dict = response.json()
    assert len(response_dict['items']) == 30
#BEFORE RUN CODE RUN WITH THIS IN TERNMINAL
#py -m pytest 17-3_exe.py -v
#py -m pytest thepython/API_CODE/17-3_exe.py -v