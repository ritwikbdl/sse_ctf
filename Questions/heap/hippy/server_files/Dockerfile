# docker build -t notes .
# sudo docker run -d -p 1339:1339 --rm  notes

FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --reinstall libc6-i386 && apt install -y xinetd

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "root:sseCTF2022" | chpasswd
RUN echo "ctf:deadbeef" | chpasswd

WORKDIR /home/ctf

COPY notes .
COPY flag.txt .
COPY notes.xinetd /etc/xinetd.d/notes

RUN chown -R root:root /home/ctf
# make the file system readonly
RUN chmod -R a-w /home/ctf

# USER ctf
# EXPOSE 1024

CMD xinetd -dontfork