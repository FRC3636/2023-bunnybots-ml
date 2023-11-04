#!/usr/bin/env bash

ssh-keygen -A

mkdir /root/.ssh
echo $SSH_PUBLIC_KEY > /root/.ssh/authorized_keys

rm -rf /run/nologin

/usr/sbin/sshd -D