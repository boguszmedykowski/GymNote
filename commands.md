#swagger
./manage.py spectacular --color --file schema.yml

coverage run --omit='*/env/*' manage.py test
coverage html

#Docker
docker build -t nazwa_obrazu .
docker run -p 8888:8888 nazwa_obrazu
docker ps -a
docker exec -it nazwa_kontenera sh

docker save my-image > my-image.tar
docker load < my-image.tar

gunicorn gym.wsgi:application --bind 0.0.0.0:8888


git ls-files
git rm plik
git push --force origin main

git checkout -b nazwa

git fetch
git reset --hard origin/<nazwa_gałęzi>