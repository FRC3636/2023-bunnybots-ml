FROM tensorflow/tensorflow:latest-gpu

WORKDIR /root

RUN apt-get update
RUN apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev git -y
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
ENV PYTHON_VERSION=3.9
ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"
RUN eval "$(pyenv init -)"
RUN /root/.pyenv/bin/pyenv install ${PYTHON_VERSION}
RUN /root/.pyenv/bin/pyenv global ${PYTHON_VERSION}
RUN pip install --upgrade pip
RUN pip install tflite-model-maker
RUN pip install numpy==1.23.1 pycocotools roboflow

COPY download.py .