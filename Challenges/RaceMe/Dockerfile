FROM ubuntu AS host
RUN apt update && apt install -y vim nano tcc

FROM pwn.red/jail
COPY --from=host / /srv

ENV JAIL_TIME=3000
ENV JAIL_CONNS=200
ENV JAIL_CONNS_PER_IP=5
ENV JAIL_PIDS=100
ENV JAIL_MEM=20M
ENV JAIL_CPU=2000
ENV JAIL_PORT=6767
ENV JAIL_TMP_SIZE=2M
ENV JAIL_DEV=tty

RUN mkdir /srv/app
COPY flag /srv/app/flag
RUN chown root:root /srv/app/flag
RUN chmod 600 /srv/app/flag
COPY run.sh /srv/app/run
COPY nsjail.conf /srv/

COPY catto /srv/app/catto
COPY hook.sh /jail/hook.sh
RUN chmod +s /jail/nsjail
RUN chmod +s /jail/run
COPY start.sh /jail/start
RUN chmod +x /jail/start

CMD [ "/bin/sh" ]
