

def test_create_foo(app):
    payload = {"description": "Foo da Silva"}
    response = app.post('/api/v1/foo', json=payload)
    assert response.status_code == 200
    assert response.get_json() == {'id': '1', 'description': 'Foo da Silva'}


def test_create_foo_with_blank_description(app):
    payload = {}
    response = app.post('/api/v1/foo', json=payload)
    assert response.status_code == 400
    assert response.get_json() == {'description': ['Missing data for required field.']}
