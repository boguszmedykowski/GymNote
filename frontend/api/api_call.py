import requests


URL = "http://ec2-54-80-52-84.compute-1.amazonaws.com"
# URL = "http://0.0.0.0:8000"


def get_token(email: str, password: str):
    url = f"{URL}/api/user/token/"

    payload = {'email': email,
               'password': password}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()

        data = response.json()
        token = data['token']

        return token

    except requests.exceptions.RequestException as e:
        print(str(e))
        return "Error"


def register(name: str, email: str, password: str):
    url = f"{URL}/api/user/create/"

    payload = {
        'name': name,
        'email': email,
        'password': password
    }

    try:
        response = requests.post(url, data=payload)

        return f"Status Code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


def get_workouts(token: str):
    url = f"{URL}/api/note/workouts/"
    try:
        headers = {'Authorization': f'Token {token}'}
        response = requests.get(url, headers=headers)
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


def create_workout(token: str, title: str):
    url = f"{URL}/api/note/workouts/"

    headers = {'Authorization': f'Token {token}'}
    payload = {
        'title': title
    }
    try:
        response = requests.post(url, headers=headers, data=payload)

        return f"status Code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


def get_workout(token: str, id: int):
    url = f"{URL}/api/note/workouts/{id}/"
    try:
        headers = {'Authorization': f'Token {token}'}
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"{str(e)}"
