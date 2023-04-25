# docker build -t canary .
# sudo docker run -d -p 1340:1340 --rm  canary

FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --reinstall libc6-i386 && apt install -y xinetd

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "root:sseCTF2022" | chpasswd
RUN echo "ctf:deadbeef" | chpasswd


WORKDIR /home/ctf

COPY canary .
COPY flag.txt .
COPY canary.xinetd /etc/xinetd.d/canary

RUN chown -R root:root /home/ctf
# make the file system readonly
RUN chmod -R a-w /home/ctf

CMD xinetd -dontfork