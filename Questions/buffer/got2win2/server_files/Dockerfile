FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y --reinstall libc6-i386 && apt install -y xinetd socat

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN useradd -d /home/waldo/ -m -s /bin/bash waldo
RUN echo "root:sseCTF2022" | chpasswd
RUN echo "ctf:deadbeef" | chpasswd
RUN echo "waldo:deadbeef" | chpasswd

WORKDIR /home/waldo

COPY sensitive_data.txt .

WORKDIR /home/ctf

COPY got2win .
COPY flag.txt .
COPY got2win.xinetd /etc/xinetd.d/got2win
ADD start.sh /root
ADD run.sh /home/ctf/.run.sh

# RUN chown -R waldo:waldo /home/waldo
RUN chmod 500 /home/waldo/sensitive_data.txt
# RUN chown -R root:root /home/ctf
# make the file system readonly
# RUN chmod -R a-w /home/ctf/


RUN chmod +x /root/start.sh && \
    chmod +x /home/ctf/.run.sh && \
    chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf/   && \
    chmod 755 /tmp 

ENTRYPOINT  /root/start.sh

# USER ctf
# EXPOSE 1024


# CMD ["socat", "TCP-LISTEN:1338,reuseaddr,fork", "EXEC:/home/ctf/got2win,nofork,stderr"]
# CMD xinetd -dontfork