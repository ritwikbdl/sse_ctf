
docker rm -f $(docker ps -a | grep 'got2win' | awk '{print $1}')
docker images -a | grep "git2win" | awk '{print $3}' | xargs docker rmi

docker build -t got2win .
docker run --rm -d -p 1338:1338 got2win 