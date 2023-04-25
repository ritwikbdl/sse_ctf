FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN useradd -d /home/waldo/ -m -s /bin/bash waldo
RUN echo "root:esCTF_2220" | chpasswd
RUN echo "ctf:deadbeef" | chpasswd
RUN echo "waldo:deadbeef" | chpasswd

RUN apt install -y --reinstall libc6-i386

WORKDIR /home/waldo

COPY sensitive_data.txt .

WORKDIR /home/ctf

COPY got2win .
COPY flag.txt .
COPY ynetd .

RUN chown -R waldo:waldo /home/waldo
RUN chmod 600 /home/waldo/sensitive_data.txt
RUN chown -R root:root /home/ctf
# make the file system readonly
RUN chmod -R a-w /home/ctf

USER ctf

EXPOSE 1024


CMD ./ynetd -p 1024 -a 0.0.0.0 ./got2win