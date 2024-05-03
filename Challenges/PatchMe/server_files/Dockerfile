# docker build -t patchme .
# sudo docker run -d -p 4444:1024 --rm  --name patchme patchme 

FROM python:3.11


RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "root:sseCTF_2223" | chpasswd
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf/app

COPY bin .
COPY ynetd .
#COPY bin.c .
COPY interface.py .

#RUN gcc -o bin bin.c
RUN chmod +x ./interface.py
RUN chown -R root:root /home/ctf
#    chmod -R a-w /home/ctf
RUN chmod 777 /home/ctf/app
USER ctf
EXPOSE 2048

CMD ./ynetd -p 2048 -a 0.0.0.0 ./interface.py
