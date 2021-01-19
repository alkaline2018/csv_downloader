FROM ubuntu:20.04
MAINTAINER song <shdth117@e2on.com>

RUN apt-get update && yes | apt-get upgrade
RUN apt-get install -y build-essential
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev

COPY . /app
WORKDIR /app/src
RUN pip3 install -r ../requirements.txt
ENTRYPOINT ["python3"]
CMD ["csv_downloader.py"]
# 실행시킬 때 image 에서 container 생성만
#docker create --name opendata_downloader -v C:\Users\song_e\Documents\csv_download_test\a:/app/download alkaline2018/opendata-downloader:1.0.16
#docker create --name {container_name} -v {host_path}:{docker_path} {image_name}:{version}
# contianer 실행
#docker start opendata_downloader
#docker start {container_name}