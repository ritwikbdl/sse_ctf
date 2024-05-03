FROM ubuntu AS host
RUN apt-get update && apt-get install -y python3 && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*


FROM pwn.red/jail
COPY --from=host / /srv

ENV JAIL_TIME=300
ENV JAIL_CONNS=200
ENV JAIL_CONNS_PER_IP=5
ENV JAIL_PIDS=100
ENV JAIL_MEM=20M
ENV JAIL_CPU=2000
ENV JAIL_PORT=5252
ENV JAIL_TMP_SIZE=2M

RUN mkdir /srv/app
COPY test.py /srv/app/run
#COPY bash /srv/app/run
COPY flag /srv/app/flag
COPY hook.sh /jail/hook.sh
RUN cp /etc/resolv.conf /srv/etc/resolv.conf
COPY test /srv/app/test
