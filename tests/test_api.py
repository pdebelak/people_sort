import pytest

from people_sort.api import app, people


@pytest.fixture(autouse=True)
def reset_people():
    people._people = []
    yield


def test_404():
    client = app.test_client()
    resp = client.post('/', data='Debelak|Peter|M|Orange|1/1/2018')
    assert resp.status_code == 404
    body = resp.json
    assert body['error'] == 'Not found'


def test_adding_person():
    client = app.test_client()
    resp = client.post('/records', data='Debelak|Peter|M|Orange|1/1/2018')
    assert resp.status_code == 204
    person = people._people[0]
    assert person.last_name == 'Debelak'


def test_adding_person_unparseable():
    client = app.test_client()
    resp = client.post('/records', data='hello')
    assert resp.status_code == 400
    body = resp.json
    assert body['error'] == 'Incorrect field count: Expected 5 fields'


def test_adding_person_missing_field():
    client = app.test_client()
    resp = client.post('/records', data='Debelak|Peter|M||1/1/2018')
    assert resp.status_code == 400
    body = resp.json
    assert body['error'] == 'Missing required field: favorite_color'


def test_adding_person_invalid_date():
    client = app.test_client()
    resp = client.post('/records', data='Debelak|Peter|M|Orange|13/1/2018')
    assert resp.status_code == 400
    body = resp.json
    assert body['error'] == 'Invalid birth date'


def test_sorting_by_gender():
    client = app.test_client()
    client.post('/records', data='Debelak|Peter|M|Orange|1/1/2018')
    client.post('/records', data='Febelak|Peter|F|Light Blue|12/31/2018')
    resp = client.get('/records/gender')
    assert resp.status_code == 200
    parsed = resp.json['people']
    assert parsed[0]['last_name'] == 'Febelak'
    assert parsed[1]['last_name'] == 'Debelak'


def test_sorting_by_birth_date():
    client = app.test_client()
    client.post('/records', data='Debelak|Peter|M|Orange|1/1/2018')
    client.post('/records', data='Febelak|Peter|F|Light Blue|12/31/2018')
    resp = client.get('/records/birthdate')
    assert resp.status_code == 200
    parsed = resp.json['people']
    assert parsed[0]['last_name'] == 'Debelak'
    assert parsed[1]['last_name'] == 'Febelak'


def test_sorting_by_last_name():
    client = app.test_client()
    client.post('/records', data='Debelak|Peter|M|Orange|1/1/2018')
    client.post('/records', data='Febelak|Peter|F|Light Blue|12/31/2018')
    resp = client.get('/records/name')
    assert resp.status_code == 200
    parsed = resp.json['people']
    assert parsed[0]['last_name'] == 'Debelak'
    assert parsed[1]['last_name'] == 'Febelak'
