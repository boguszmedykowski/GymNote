# Pobierz obraz bazowy Pythona
FROM python:3.9-alpine

# Ustaw zmienne środowiskowe
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Skopiuj pliki wymagane do uruchomienia projektu
COPY gym/requirements.txt /code/gym/
COPY gym /code/gym/

# Ustaw katalog roboczy
WORKDIR /code/gym
#aktualizuj pip
RUN pip install --upgrade pip
# Zainstaluj wymagane biblioteki
RUN pip install -r requirements.txt

# Otwórz port 8888
EXPOSE 8888

# Uruchom serwer Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]
