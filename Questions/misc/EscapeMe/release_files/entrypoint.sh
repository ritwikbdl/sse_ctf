#!/bin/bash

# Start ynetd
/usr/sbin/ynetd -p 5252 -a 0.0.0.0 /usr/local/bin/start_chroot.sh
