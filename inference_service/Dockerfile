FROM tensorflow/tensorflow:2.6.1-gpu

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Munich

# Fix GPG error
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub

# tensorflow object detection api dependence
RUN apt-get update &&\
    apt-get install -y \
    tzdata \
    git \
    protobuf-compiler

RUN python -m pip install --upgrade pip

RUN pip install cmake
RUN pip install notebook
RUN pip install geojson
RUN pip install cython

# Install Onject Detection API
COPY models models
# RUN git clone https://github.com/tensorflow/models
RUN git clone https://github.com/cocodataset/cocoapi.git
RUN cd cocoapi/PythonAPI && make &&\
    cp -r pycocotools ../../models/research &&\
    cd ../../models/research &&\
    protoc object_detection/protos/*.proto --python_out=. &&\
    cp object_detection/packages/tf2/setup.py . &&\
    python -m pip install .


WORKDIR /app
# COPY requirements.txt .
# RUN pip install -r requirements.txt
COPY src src

# ohsome2label dependence
COPY ohsome2label ohsome2label
RUN apt-get update &&\
    apt-get install -y \
    build-essential \
    libsqlite3-dev \
    zlib1g-dev \
    libgeos-dev \
    libgdal-dev \
    libgnutls28-dev \
    libcurl4-openssl-dev \
    protobuf-compiler \
    python-pil \
    python-lxml \
    python-tk \
    tzdata

# install ohsome2label
RUN cd ohsome2label &&\
    pip install --editable .

# microservice dependencies
RUN pip install flask
RUN pip install flask_cors
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

