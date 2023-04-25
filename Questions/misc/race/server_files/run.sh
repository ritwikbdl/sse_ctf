#!/bin/bash

sudo fuser -k 9999/tcp
socat tcp-listen:9999,reuseaddr,fork exec:"./start.sh",pty,stderr,setsid,sigint,sane &
echo "Listening on 9999"
