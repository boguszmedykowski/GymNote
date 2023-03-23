#swagger
./manage.py spectacular --color --file schema.yml
docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui

coverage run --omit='*/env/*' manage.py test
coverage html

#Docker
sudo docker build django-on-docker -f Dockerfile .
sudo docker run -it -p 80:8888 django-on-docker



gunicorn gym.wsgi:application --bind 0.0.0.0:8000