docker build -t dumped .

docker run -d -p 1337:1337 --rm dumped 