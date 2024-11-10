from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country':'France'})
    assert response.status_code == 200


def test_edit_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<int:id>' page is posted to (PUT)
    THEN check the response is valid and the account is updated
    """
    
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country':'France'})
    assert response.status_code == 200
    
    account_id = response.json['id']

    response = testing_client.put(f'/accounts/{account_id}', json={'name': 'Jane Doe', 'country': 'Germany'})
    
    assert response.status_code == 200
    
    updated_account = response.json
    assert updated_account['name'] == 'Jane Doe'
    assert updated_account['country'] == 'Germany'
