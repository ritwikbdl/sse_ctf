FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "root:esCTF_2220" | chpasswd
RUN echo "ctf:deadbeef" | chpasswd

RUN apt install -y --reinstall libc6-i386
RUN apt install -y gcc libssl-dev

WORKDIR /home/ctf

COPY main.c .
COPY flag.txt .
COPY ynetd .
COPY hash.txt .

RUN gcc -o main main.c -lssl -lcrypto

# RUN chown -R root:root /home/ctf
# make the file system readonly
# RUN chmod -R a-w /home/ctf

USER ctf

EXPOSE 1024


CMD ./ynetd -p 1024 -a 0.0.0.0 ./main
