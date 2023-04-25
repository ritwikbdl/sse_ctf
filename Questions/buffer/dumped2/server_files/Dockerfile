# docker build -t dumped .
# sudo docker run -d -p 1337:1337 --rm  dumped

FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --reinstall libc6-i386 && apt install -y xinetd

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN useradd -d /home/waldo/ -m -s /bin/bash waldo
RUN echo "root:sseCTF2022" | chpasswd
RUN echo "ctf:deadbeef" | chpasswd
RUN echo "waldo:deadbeef" | chpasswd


WORKDIR /home/ctf

COPY dumped .
COPY dumped_flag.txt .
COPY meeting_notes.txt .
COPY dumped.xinetd /etc/xinetd.d/dumped

RUN chown -R root:root /home/ctf
# make the file system readonly
RUN chmod -R a-w /home/ctf

# USER ctf
# EXPOSE 1024

CMD xinetd -dontfork