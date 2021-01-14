FROM ubuntu:20.04
MAINTAINER song <shdth117@e2on.com>

RUN apt-get update && yes | apt-get upgrade
RUN apt-get install -y build-essential
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["csv_downloader.py"]
#CMD python csv_downloader.py

#VOLUME ["/data", "/etc/nginx/site-enabled", "/var/log/nginx"]

#WORKDIR /etc/nginx

