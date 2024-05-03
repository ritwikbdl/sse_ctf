# Use a base image with necessary tools and libraries
FROM ubuntu:noble-20240225

# Install necessary packages
RUN apt-get update \
    && apt-get install -y \
        python3 \
        netcat-traditional \
        libc6 \
        binutils \
    && rm -rf /var/lib/apt/lists/*

# Create directories for the chroot jail
RUN mkdir -p /chroot/jail/usr/bin \
    && mkdir -p /chroot/jail/bin \
    && mkdir -p /chroot/jail/lib \
    && mkdir -p /chroot/jail/lib64 \
    && mkdir -p /chroot/jail/usr/lib \
    && mkdir -p /chroot/jail/usr/share \
    && mkdir -p /chroot/jail/tmp \
    && chmod 1777 /chroot/jail/tmp \
    && mkdir -p /chroot/jail/app \
    && chmod 777 /chroot/jail/app \
    && mkdir -p /chroot/jail/dev \
    && cp -a /dev/null /chroot/jail/dev/

# Copy nc, echo, ls, cat, and sh binaries into chroot jail bin directory
RUN cp /bin/nc /bin/echo /bin/ls /bin/cat /bin/sh /chroot/jail/bin/

# Copy your binary and any required files into the chroot directory
COPY ynetd /usr/sbin/
COPY test.py /chroot/jail/app/
COPY flag /chroot/jail/app/
COPY test /chroot/jail/app/

# Copy all of /lib and /lib64 into chroot jail
RUN cp -a /lib/. /chroot/jail/lib/ \
    && cp -a /lib64/. /chroot/jail/lib64/

# Copy Python binary and required libraries into chroot jail
RUN cp /usr/bin/python3 /chroot/jail/usr/bin/python3

# Copy Python related directories and files into the chroot jail
RUN cp -R /usr/lib/py* /chroot/jail/usr/lib/ \
    && cp -R /usr/share/py* /chroot/jail/usr/share/ \
    && find /usr/lib/python3.12/ -name '*.so' -exec cp {} /chroot/jail/usr/lib/ \;

# Copy environment variables used by /bin/sh into chroot jail
RUN mkdir -p /chroot/jail/etc \
    && cp /etc/passwd /etc/group /etc/nsswitch.conf /etc/ld.so.conf /etc/hosts /etc/host.conf /etc/resolv.conf /etc/localtime /etc/environment /chroot/jail/etc/

# Set up overlayfs for chroot jail
RUN mkdir -p /overlay/work \
    && mkdir -p /overlay/upper \
    && mkdir -p /overlay/root \
    && mount -t overlay overlay -o lowerdir=/chroot/jail,upperdir=/overlay/upper,workdir=/overlay/work /overlay/root \
    && cp -a /overlay/root/. /chroot/jail/

# Create a shell script to start /bin/sh in the chroot
RUN echo '#!/bin/sh' > /usr/local/bin/start_chroot.sh \
    && echo 'chroot /chroot/jail /bin/sh' >> /usr/local/bin/start_chroot.sh \
    && chmod +x /usr/local/bin/start_chroot.sh

# Expose the port used by ynetd
EXPOSE 5252

# Set up entrypoint script to start ynetd
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
