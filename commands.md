#swagger
./manage.py spectacular --color --file schema.yml
docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui

coverage run --omit='*/env/*' manage.py test
coverage html

#Docker
docker build -t nazwa_obrazu .
docker run -p 8888:8888 nazwa_obrazu
docker ps -a
docker exec -it nazwa_kontenera sh

docker save my-image > my-image.tar
docker load < my-image.tar

gunicorn gym.wsgi:application --bind 0.0.0.0:8000


git ls-files
git rm plik
git push --force origin main