import requests


URL = "http://ec2-3-92-165-17.compute-1.amazonaws.com"

s = requests.Session()


def get_token(email: str, password: str):
    url = f"{URL}/api/user/token/"

    payload = {'email': email,
               'password': password}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()

        data = response.json()
        token = data['token']

        headers = {"Authorization": f"Bearer {token}"}

        s.headers.update(headers)
        print(response.status_code)

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
        response = requests.post(url, data=payload)

        return f"Status Code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
