
FROM ubuntu:noble-20240225  
RUN apt-get update && apt-get install -y python3 && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

RUN mkdir app

WORKDIR /app
COPY ynetd .
COPY test test
COPY flag flag
COPY test.py test.py
RUN chmod +x ./test.py

EXPOSE 5000

CMD ./ynetd -p 5000 -a 0.0.0.0 ./test.py
