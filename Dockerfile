FROM ubuntu:16.04
MAINTAINER Aleksandar Velkoski <avelkoski@ethventures.io>

RUN apt-get update && apt-get install -y python-dev \
    python-pip build-essential git libldap2-dev libsasl2-dev \
    libsmi2-dev libffi-dev cmake pkg-config libtiff-dev \
    unzip libtbb-dev libjasper-dev libtbb2 libpng-dev \
    libjpeg-dev libswscale-dev qt5-default libqt5svg5-dev \
    qtcreator wget

RUN cd \
  && wget https://github.com/opencv/opencv/archive/2.4.11.zip \
	&& unzip 2.4.11.zip \
	&& cd opencv-2.4.11 \
	&& mkdir build \
	&& cd build \
	&& cmake .. \
	&& make -j4 \
	&& make install \
	&& cd \
	&& rm 2.4.11.zip

RUN cd \
  && git clone https://github.com/biometrics/openbr.git \
	&& cd openbr \
  && git checkout v1.1.0 \
  && git submodule init \
  && git submodule update \
	&& mkdir build \
	&& cd build \
	&& cmake -DCMAKE_BUILD_TYPE=Release .. \
	&& make -j4 \
	&& make install

RUN mkdir /sample
ADD ./sample /sample
