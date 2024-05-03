FROM ubuntu:20.04 AS host
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt install -y gcc && apt install -y --reinstall libc6-i386 && rm -rf /var/lib/apt/lists/*

COPY main.c main.c
RUN gcc main.c -ldl -g -fno-stack-protector -o main

FROM pwn.red/jail
COPY --from=host / /srv


ENV JAIL_TIME=300
ENV JAIL_CONNS=200
ENV JAIL_CONNS_PER_IP=5
ENV JAIL_PIDS=100
ENV JAIL_MEM=20M
ENV JAIL_CPU=2000
ENV JAIL_PORT=6969
ENV JAIL_TMP_SIZE=2M

RUN mkdir /srv/app
COPY jail_main /srv/app/run
#COPY bash /srv/app/run
COPY flag.txt /srv/app/flag
