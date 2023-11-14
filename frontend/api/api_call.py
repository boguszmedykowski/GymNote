import requests


URL = "http://ec2-54-80-52-84.compute-1.amazonaws.com"
# URL = "http://0.0.0.0:8000"

s = requests.Session()


def get_token(email: str, password: str):
    url = f"{URL}/api/user/token/"

    payload = {'email': email,
               'password': password}

    try:
        response = s.post(url, data=payload)
        response.raise_for_status()

        data = response.json()
        token = data['token']

        headers = {"Authorization": f"Token {token}"}

        s.headers.update(headers)
        print(data)
        print(response.status_code)
        print(headers)

        return f"Token obtained successfully. Status Code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        print(str(e))
        return f"Error getting token: {str(e)}"


def register(name: str, email: str, password: str):
    url = f"{URL}/api/user/create/"

    payload = {
        'name': name,
        'email': email,
        'password': password
    }

    try:
        response = s.post(url, data=payload)

        return f"Status Code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


def get_workouts():
    url = f"{URL}/api/note/workouts/"
    try:
        response = s.get(url, headers=s.headers)
        data = response.json()
        print(response)
        print(data)
        print(s.headers)
        return data

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


def create_workout(title: str):
    url = f"{URL}/api/note/workouts/"
    payload = {
        'title': title
    }
    try:
        response = s.post(url, headers=s.headers, data=payload)

        return f"status Code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
