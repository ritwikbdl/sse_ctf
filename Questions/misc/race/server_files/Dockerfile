FROM ubuntu:20.04

RUN apt update && apt upgrade
RUN apt install -y \
        vim \
        gcc \
        nano \
        tmux

RUN echo "root:ctf_r00t" | chpasswd

RUN useradd -m ctf && \
    echo 'ctf:ctf' | chpasswd && \
    chsh -s /bin/bash ctf 

RUN useradd superadmin && \
    echo 'superadmin:password' | chpasswd && \
    chsh -s /bin/bash superadmin 

COPY read.c /home/ctf/read.c
COPY fake /home/ctf/Dockerfile
RUN gcc /home/ctf/read.c -o /home/ctf/read && \
    chmod +s /home/ctf/read



COPY flag.txt /home/ctf/flag.txt
RUN chown root:root /home/ctf/flag.txt && chmod 400 /home/ctf/flag.txt
RUN chown root:root /home/ctf/Dockerfile && chmod 400 /home/ctf/Dockerfile

WORKDIR /home/ctf





