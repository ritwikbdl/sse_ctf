# docker build -t lottery .
# sudo docker run -d -p 1024:1024 --rm  lottery --name lottery

FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --reinstall libc6-i386

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "root:sseCTF_2223" | chpasswd
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY pokemon_hosted .
COPY ynetd .


RUN chown -R root:root /home/ctf && \
    chmod -R a-w /home/ctf


#RUN chmod -R u+x /home/ctf

USER ctf
EXPOSE 1024 

CMD ./ynetd -p 1024 -a 0.0.0.0 ./pokemon_hosted
