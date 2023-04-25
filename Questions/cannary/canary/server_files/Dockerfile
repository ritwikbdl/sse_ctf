# docker build -t canary .
# sudo docker run -d -p 7777:7777 --rm  canray

FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --reinstall libc6-i386

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "root:esCTF_2220" | chpasswd
RUN echo "ctf:esCTF_2220" | chpasswd

WORKDIR /home/ctf

COPY canary .
COPY flag.txt .
COPY ynetd .


RUN chown -R root:root /home/ctf && \
    chmod -R a-w /home/ctf

USER ctf
EXPOSE 1024

CMD ./ynetd -p 1024 -a 0.0.0.0 ./canary
