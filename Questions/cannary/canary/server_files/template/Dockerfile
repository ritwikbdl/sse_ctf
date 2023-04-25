FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --reinstall libc6-i386

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN useradd -d /home/waldo/ -m -s /bin/bash waldo
RUN echo "root:sseCTF2022" | chpasswd
RUN echo "ctf:deadbeef" | chpasswd
RUN echo "waldo:deadbeef" | chpasswd

# RUN apt install -y --reinstall libc6-i386

WORKDIR /home/ctf

COPY dumped .
COPY dumped_flag.txt .
COPY meeting_notes.txt .
COPY ynetd .

RUN chown -R root:root /home/ctf
# make the file system readonly
RUN chmod -R a-w /home/ctf

# USER ctf

EXPOSE 1024


CMD ./ynetd -p 1024 -a 0.0.0.0 ./dumped