FROM ubuntu:20.04

# 환경변수 먼저 설정
ENV DEBIAN_FRONTEND=noninteractive \
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    LANG=ko_KR.UTF-8 \
    LANGUAGE=ko_KR.UTF-8 \
    LC_ALL=ko_KR.UTF-8
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# 패키지 설치
RUN apt-get update && apt-get install -y \
    locales \
    wget \
    curl \
    git \
    python3 \
    python3-pip \
    openjdk-8-jdk \
    fonts-nanum* \
    && locale-gen ko_KR.UTF-8 \
    && update-locale LANG=ko_KR.UTF-8 \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치
RUN pip3 install fastapi uvicorn[standard] requests JPype1==1.4.1 python-multipart

WORKDIR /app

COPY . /app

EXPOSE 7860

CMD ["python3", "main.py"]