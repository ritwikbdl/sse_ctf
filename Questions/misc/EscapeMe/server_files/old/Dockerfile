#FROM python:3.10.14 AS app
# RUN pip install --no-cache-dir progress

#COPY --from=ubuntu:noble-20240225 / /srv

FROM ubuntu:noble-20240225 AS app
RUN apt-get update && apt-get install -y python3 && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

FROM pwn.red/jail

COPY --from=app / /srv
COPY test /srv/app/test
COPY a /srv/app/a
COPY nc /srv/bin/nc
COPY test.py /srv/app/run
COPY run.sh /srv/app/run
RUN chmod +x /srv/app/run

ENV JAIL_MEM=20M  JAIL_ENV_NUM=5 JAIL_TMP_SIZE=2M JAIL_TIME=3600 
