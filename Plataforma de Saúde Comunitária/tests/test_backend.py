import pytest
import requests

def test_receive_data():
    url = 'http://localhost:5000/data'
    data = {
        'pressure': 120,
        'glucose': 90
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201
    assert response.json()['status'] == 'success'
