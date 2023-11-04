#!/usr/bin/env bash

echo "Entered bunnybots vast.ai env."

ssh-keygen -A
echo "Generated host keys..."

mkdir /root/.ssh
echo $SSH_PUBLIC_KEY > /root/.ssh/authorized_keys
echo "Authorized public key '${SSH_PUBLIC_KEY}'" 

rm -rf /run/nologin

echo "Starting sshd..."
/usr/sbin/sshd -D