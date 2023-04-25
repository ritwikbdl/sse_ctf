# docker stop $(docker ps -a -q)
# docker ps -a | grep 'dumped' | awk 'print $1'
# docker rm -f $(docker ps -a -q)
docker rm -f $(docker ps -a | grep 'dumped' | awk '{print $1}')
docker images -a | grep "dumped" | awk '{print $3}' | xargs docker rmi

# docker build -t dumped .
# docker run --rm -d -p 1337:1337 dumped 