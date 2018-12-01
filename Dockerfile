FROM resin/raspberrypi3-python:3
# Enable systemd
ENV INITSYSTEM on

# 必要なライブラリのインストール
RUN apt-get update
ADD requirements.txt /root
WORKDIR /root
RUN pip install -r requirements.txt
