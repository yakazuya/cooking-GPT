FROM ubuntu:20.04
# RUN sed -i 's@archive.ubuntu.com@ftp.yz.yamagata-u.ac.jp/pub/Linux@g' /etc/apt/sources.list

RUN perl -p -i.bak -e 's%(deb(?:-src|)\s+)https?://(?!archive\.canonical\.com|security\.ubuntu\.com)[^\s]+%$1http://linux.yz.yamagata-u.ac.jp/pub/linux/ubuntu/archives/%' /etc/apt/sources.list

LABEL maintainer="yabashikazuya"

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    nano

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        python3-pip \
        python3-dev \
        build-essential \
        gnupg \
        curl \
        unzip \
        pkg-config \
        libssl-dev \
        libgl1-mesa-dev \
        language-pack-ja-base \
        language-pack-ja \
        libjpeg8-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV LANG=ja_JP.UTF-8

RUN echo "PYTHONIOENCODING=utf-8" >> /etc/bash.bashrc && \
    echo "export PS1='\[\033[01;32m\]trandy-sercher@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /etc/bash.bashrc

RUN pip3 install \
        setuptools \
        Cython \
        wheel --verbose

# 矩形作成のためのモジュール
RUN pip3 install \
    opencv-python==4.7.0.72 \
    numpy==1.23.5 \
    rembg 
# DeepLを用いるためのモジュール
RUN pip3 install \
    selenium==4.2.0 \
    beautifulsoup4==4.12.2 \
    webdriver_manager==3.8.6
    

# userの設定
ARG username=cooking-GPT
ARG wkdir=/home
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID $username && \
    useradd -m -s /bin/bash -u $UID -g $GID -G sudo $username && \
    echo $username:$username | chpasswd && \
    echo "$username   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# RUN wget https://chromedriver.storage.googleapis.com/113.0.5672.24/chromedriver_linux64.zip && unzip chromedriver_linux && \
#     mv /chromedriver /usr/local/bin/ && chmod 755 /usr/local/bin/chromedriver

# 

# RUN wget https://www.slimjet.com/chrome/download-chrome.php?file=files%2F104.0.5112.102%2Fgoogle-chrome-stable_current_amd64.deb
# RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libxcomposite1 \
    xdg-utils

RUN wget https://www.slimjet.com/chrome/download-chrome.php?file=files%2F104.0.5112.102%2Fgoogle-chrome-stable_current_amd64.deb -O google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb

# chrome driverのインストール
RUN wget https://chromedriver.storage.googleapis.com/104.0.5112.79/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm chromedriver_linux64.zip



# workdirの権限をルートからユーザーに変更
RUN chown ${username}:${username} ${wkdir}
# ユーザー
USER ${username}

WORKDIR ${wkdir}