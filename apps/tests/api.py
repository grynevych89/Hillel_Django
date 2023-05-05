# from currency.models import RateSource
from source.models import Source


def test_get_api_rate_list(api_client):
    response = api_client.get('/v1/api/currency/')
    assert response.status_code == 200


def test_post_api_rate_list(api_client):
    response = api_client.post('/v1/api/currency/')
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.']
    }


def test_get_api_source_list(api_client):
    response = api_client.get('/v1/api/source/')
    assert response.status_code == 200


def test_post_source_list(api_client):
    response = api_client.post('/v1/api/source/')
    assert response.status_code == 400
    assert response.json() == {
        'name': ['This field is required.'],
        'text': ['This field is required.'],
    }


def test_post_source_create(api_client):
    data = {
        'id': 1,
        'name': 'Test',
        'text': 'test',
        'logo_url': '/static/default-logo.png',
        'price': 0,
    }
    response = api_client.post('/v1/api/source/', data=data)
    assert response.status_code == 201
    assert response.json() == data


def test_post_source_update(api_client):
    Source.objects.create(
        id=1,
    )

    data = {
        'id': 1,
        'name': 'Test2',
        'text': 'test2',
        'logo_url': '/static/default-logo.png',
        'price': 22,
    }
    response = api_client.put('/v1/api/source/1/', data=data)
    assert response.status_code == 200
    assert response.json() == data


def test_delete_source(api_client):
    Source.objects.create(
        id=1,
    )
    response = api_client.delete('/v1/api/source/1/')
    assert response.status_code == 204
