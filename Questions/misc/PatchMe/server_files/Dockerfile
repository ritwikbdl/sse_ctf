# docker build -t patchme .
# sudo docker run -d -p 4444:1024 --rm  --name patchme patchme 

FROM python:3.9.16


RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "root:sseCTF_2223" | chpasswd
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

#COPY bin .
COPY ynetd .
COPY bin.c .
COPY interface.py .

RUN gcc -o bin bin.c

RUN chown -R root:root /home/ctf
#    chmod -R a-w /home/ctf

USER ctf
EXPOSE 1024

CMD ./ynetd -p 1024 -a 0.0.0.0 ./interface.py
