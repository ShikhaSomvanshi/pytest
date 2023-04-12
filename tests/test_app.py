import requests

def test_get_users():
    response = requests.get('https://gorest.co.in/public/v2/users')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert len(response.json()) > 0

def test_get_users_auth():
    url = 'https://gorest.co.in/public/v2/users'
    headers = {'Authorization': 'Bearer fafad1e0cfad7fde47ecf8d14f114a66fd92c08023e08b74e14691097604960c'} # replace <your_access_token> with your actual token
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert 'data' in response.json().keys()

def test_get_user():
    response = requests.get('https://gorest.co.in/public/v2/users/902633')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    print(response.json())
    assert len(response.json()) > 1

def test_create_user():
    data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "gender": "male",
        "status": "active"
    }
    response = requests.post('https://gorest.co.in/public/v2/users', json=data, headers={'Authorization': 'access_token fafad1e0cfad7fde47ecf8d14f114a66fd92c08023e08b74e14691097604960c'})
    assert response.status_code == 201
    assert response.json()['data']['name'] == data['name']
    assert response.json()['data']['email'] == data['email']
    assert response.json()['data']['gender'] == data['gender']
    assert response.json()['data']['status'] == data['status']

def test_update_user():
    user_id = 1234  # replace with a valid user ID
    data = {
        "name": "John Doe Jr.",
        "email": "johndoejr@example.com",
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(f'https://gorest.co.in/public/v2/users/{user_id}', json=data)
    assert response.status_code == 200
    assert response.json()['data']['name'] == data['name']
    assert response.json()['data']['email'] == data['email']
    assert response.json()['data']['gender'] == data['gender']
    assert response.json()['data']['status'] == data['status']

def test_delete_user():
    user_id = 1234  # replace with a valid user ID
    response = requests.delete(f'https://gorest.co.in/public/v2/users/{user_id}')
    assert response.status_code == 204

