# GymNone
Aplikacja służąca do zapisywania progresu w treningu kulturystycznym.
Składa się z backendu Django RestFramework, oraz frontendu we Flutterze


#How to run backend with docker
1.w katalogu zawierającym dockerfile backend/
docker build -t nazwa_obrazu .
docker run -p 8888:8888 nazwa_obrazu


docker run -p 8888:8888 nazwa_obrazu
docker ps -a
docker exec -it container_id sh

jesteś w konsoli kontenera możesz wpisywać djangowe polecenia


zmień nazwę pliku 'gym/gym/example.env' na 'gym/gym/.env'
uruchom projekt na porcie 8888



Jako pracę inżynierską chciałbym napisać oraz opisać aplikację webową wraz z jej deploymentem do usługi chmurowej.
Zacząłem pisać rest api we frameworku Django wykorzystująć PostgreSQL. Aplikacja będzie zdokeryzowana. Napisałbym też do niej prosty front.
- Założeniem jest portal społecznościowy na którym użytkownicy mogą tworzyć rozbudowane plany treningowe kulturystyczne.
- Użytkownik może używać strony jako notes do ćwiczeń.
- Może podać i śledzić w czasie parametry ciała.
- Przeglądać wiele wykresów dotyczących jego treningu.
- Inni osoby mogą obserować danego użytkownika podglądać jego plany treningowe.
- Aplikacja będzie obsługiwać dodawanie zdjęć.


1.Wstęp
-Cel pracy
-Opis problemu
-Struktura pracy

2. Teoria podstawowa
-Architektura aplikacji webowej
-Django Rest Framework
-Docker jako narzędzie do zarządzania kontenerami
-REST API jako sposób komunikacji między aplikacjami
-Baza danych PostgreSQL

3. Analiza wymagań
-Analiza potrzeb użytkowników
-Analiza konkurencji
-Analiza dostępnych rozwiązań

4. Projektowanie aplikacji
-Model danych
-Architektura aplikacji
-Interfejs użytkownika
-Planowanie i koordynacja prac


5.Implementacja
-Konfiguracja środowiska z wykorzystaniem Docker
-Realizacja poszczególnych funkcjonalności z wykorzystaniem Django
-Integracja z REST API i bazą danych PostgreSQL
-Deployment
-Testowanie i debugowanie
-Dokumentacja kodu

6.Testowanie i walidacja
-Testy jednostkowe i integracyjne
-Testy użytkownika
-Analiza wyników

7. Dokumentacja
-Instrukcja obsługi
-Dokumentacja techniczna
-Raport końcowy

8. Podsumowanie
-Wnioski-Przyszłe rozwinięcia

9. Bilbiografia

Bibliografia:

Beasley, D. (2018). Docker: Up & Running: Shipping Reliable Containers in Production. O'Reilly Media.

Django Rest Framework documentation. (n.d.). Retrieved from https://www.django-rest-framework.org/

Docker documentation. (n.d.). Retrieved from https://docs.docker.com/

Gonzalez, A. (2019). Mastering Django: Core. Apress.

Kuchta, K. (2021). Framework Django – wprowadzenie do tworzenia aplikacji internetowych. Wydawnictwo Naukowe PWN.

Newman, S. (2015). Building Microservices: Designing Fine-Grained Systems. O'Reilly Media.

Richardson, L., & Ruby, S. (2007). RESTful Web Services. O'Reilly Media.

Somerville, I. (2016). Software Engineering. Pearson.

Wiliński, M. (2020). Django Rest Framework – krok po kroku. Helion.

Żmudzki, P. (2019). Django – tworzenie zaawansowanych aplikacji internetowych. Helion.

Żurawski, K. (2019). Tworzenie aplikacji Django Rest Framework. Wydawnictwo Naukowe PWN.




#swagger
./manage.py spectacular --color --file schema.yml

coverage run --omit='*/env/*' manage.py test
coverage html

#Docker
docker build -t nazwa_obrazu .
docker run -p 8888:8888 nazwa_obrazu
docker ps -a
docker exec -it container_id sh

docker save my-image > my-image.tar
docker load < my-image.tar


#django
./manage.py collectstatic
gunicorn gym.wsgi:application --bind 0.0.0.0:8888


#git
git ls-files
git rm plik
git push --force origin main

git checkout -b nazwa

git fetch
git reset --hard origin/<nazwa_gałęzi>



