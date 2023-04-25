#!/bin/bash

docker build -t shell_da .
docker run -d -p 1023:1023 --name shellDa -i shell_da
