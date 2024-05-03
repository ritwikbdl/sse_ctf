#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <IP>"
    exit 1
fi

stty raw -echo
nc "$1" 6767
stty sane
