FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "root:sseCTF2022" | chpasswd
RUN echo "ctf:deadbeef" | chpasswd

RUN apt install -y --reinstall libc6-i386

WORKDIR /home/ctf

COPY notes .
COPY flag.txt .
COPY ynetd .

RUN chown -R root:root /home/ctf
# make the file system readonly
RUN chmod -R a-w /home/ctf

USER ctf

EXPOSE 1024


CMD ./ynetd -p 1024 -a 0.0.0.0 ./notes