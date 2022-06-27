FROM python:slim-bullseye

# Installing mysqldump and cleaning apt cache
RUN apt update && apt install -y default-mysql-client && \
  apt-get clean autoclean && \
  apt-get autoremove --yes && \
  rm -rf /var/lib/{apt,dpkg,cache,log}/


WORKDIR /job
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
