FROM pwn.red/jail
# copy the root files from any Docker image
COPY --from=ubuntu:latest / /srv

RUN mkdir /srv/app 
COPY ./flag.txt /srv/app/flag.txt
COPY ./whatformat /srv/app/run

