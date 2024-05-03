# docker build -t lottery .
# sudo docker run -d -p 1024:1024 --rm  lottery --name lottery

FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --reinstall libc6-i386

RUN useradd -d /home/superadmin/ -m -p password -s /bin/bash superadmin
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "root:sseCTF_2223" | chpasswd
RUN echo "ctf:ctf" | chpasswd
RUN echo "superadmin:password" | chpasswd

WORKDIR /home/ctf

COPY main .
COPY flag.txt .
COPY ynetd .
COPY supersecret.txt /home/superadmin/.

RUN chown -R superadmin:superadmin /home/superadmin && \
    chmod -R a-w /home/superadmin

RUN chown -R root:root /home/ctf && \
    chmod -R a-w /home/ctf


RUN chmod 600 /home/superadmin/supersecret.txt

USER ctf
EXPOSE 1024 

CMD ./ynetd -p 1024 -a 0.0.0.0 ./main
