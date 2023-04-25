# sudo docker build -t dumped .
# sudo docker run -d -p 1337:1337 --rm  dumped

FROM ubuntu:20.04

RUN export DEBIAN_FRONTEND=noninteractive && apt update && apt -y install xinetd

RUN useradd -d /home/ctf/ -m -s /bin/bash ctf
RUN echo "ctf:deadbeef" | chpasswd

WORKDIR /home/ctf

RUN chown -R root:root /home/ctf
RUN chmod -R a-w /home/ctf

COPY dumped .
COPY flag.txt .
COPY dumped.xinetd /etc/xinetd.d/dumped

CMD xinetd -dontfork


