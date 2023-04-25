FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "root:sseCTF2022" | chpasswd
RUN echo "ctf:srh56fgn" | chpasswd

WORKDIR /home/ctf
COPY users2_mod1.o .
COPY ynetd .
COPY flag.txt .
RUN chmod -R a-w /home/ctf
RUN chmod +x users2_mod1.o

USER ctf
EXPOSE 5555

CMD ./ynetd -p 5555 -a 0.0.0.0 './users2_mod1.o'