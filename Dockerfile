FROM nvidia/cuda:12.2.2-runtime-rockylinux8

RUN dnf install python39 python39-pip openssh-server -y

WORKDIR /root/app
COPY ./requirements.txt ./requirements.txt

RUN python3.9 -m pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/bin/bash"]