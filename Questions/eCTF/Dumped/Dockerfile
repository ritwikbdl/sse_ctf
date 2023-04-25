# sudo docker build -t A5 .
# sudo docker run -d -p 5555:5555 --rm  A5

FROM ubuntu:20.04

RUN apt update
# RUN apt upgrade

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:deadbeef" | chpasswd

# RUN useradd -d /home/waldo/ -m -p "$1$eMoL1xKh$d8bCC9TE9TqtipQtuseHM0" -s /bin/bash waldo
RUN useradd -d /home/waldo/ -m -s /bin/bash waldo
RUN echo "root:sseCTF2022" | chpasswd
RUN echo "waldo:deadbeef" | chpasswd

WORKDIR /home/ctf

COPY stars .
COPY ynetd .

RUN chown -R root:root /home/ctf
RUN chmod -R a-w /home/ctf

USER ctf
EXPOSE 1023



CMD ./ynetd -p 1023 -a 0.0.0.0 ./stars
