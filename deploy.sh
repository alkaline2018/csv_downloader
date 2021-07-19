#!/bin/bash

echo What should the version be?
read VERSION

APP_NAME="alkaline2018/csv_downloader"
APP_NAME_VERSION="$APP_NAME:$VERSION"
CONTAINER_NAME="csv_downloader"
#HINT: HOST_SPSP_PATH 에 설정 파일 두고 싶은 곳의 폴더 지정
HOST_SPSP_PATH="D:\docker-volume\csv-downloader"
HOST_DOWNLOAD_PATH="$HOST_SPSP_PATH\download"
HOST_ENV_PATH="$HOST_SPSP_PATH/env"

#HINT: HOST_DOWNLOAD_PATH 에 저장하고 싶은 곳의 폴더 지정
APP_ENV_PATH="/app/env"
APP_DOWNLOAD_PATH="/app/download"
PULL_COMMAND="docker pull $APP_NAME_VERSION"
RUN_COMMAND="docker run -d --rm -v $HOST_ENV_PATH:$APP_ENV_PATH -v $HOST_DOWNLOAD_PATH:$APP_DOWNLOAD_PATH --name $CONTAINER_NAME $APP_NAME_VERSION /bin/bash -c \"while true; do echo 1hour live;sleep 3600; done\" "
#RUN_COMMAND=docker run -d --rm -v "D:\docker-volume\csv-downloader\env":"/app/env" -v "D:\docker-volume\csv-downloader\download":"/app/download" --name csv_downloader alkaline2018/csv_downloader:0.0.19 /bin/bash -c "while true; do echo 1hour live;sleep 3600; done"
STOP_COMMAND="docker stop $CONTAINER_NAME"

HOST_IP=192.168.0.20

echo "---------info---------"

echo "APP_NAME_VERSION:" $APP_NAME_VERSION
echo "CONTAINER_NAME:" $CONTAINER_NAME
echo "HOST_DOWNLOAD_PATH:" $HOST_DOWNLOAD_PATH
echo "HOST_ENV_PATH:" $HOST_ENV_PATH
echo "APP_ENV_PATH:" $APP_ENV_PATH
echo "APP_DOWNLOAD_PATH:" $APP_DOWNLOAD_PATH
echo "PULL_COMMAND:" $PULL_COMMAND
echo "RUN_COMMAND:" $RUN_COMMAND
echo "STOP_COMMAND:" $STOP_COMMAND
echo "HOST_IP:" $HOST_IP

echo "---------build & push---------"

docker build -t $APP_NAME:$VERSION .
docker push $APP_NAME:$VERSION
#HINT: RUN_COMMAND 는 local 에서 실행되지 않는다. 그 이유는 /bin/bash 파일이 없다고 error 나기 때문이다. 이유는 잘 모르겠다.
# 해결방안으로서는 실제 RUN_COMMAND 아래 주석 처리된 RUN_COMMAND 를 버전만 변경하여 사용하는 것이다.

#$STOP_COMMAND
#$RUN_COMMAND
echo "$RUN_COMMAND"
ssh user@$HOST_IP "$PULL_COMMAND && $STOP_COMMAND && $RUN_COMMAND "

#docker run -d --rm -v D:\docker-volume\csv-downloader\env:/app/env -v $HOST_DOWNLOAD_PATH:$APP_DOWNLOAD_PATH --name csv_downloader alkaline2018/csv_downloader:0.0.20 /bin/bash -c while true; do echo 1hour live;sleep 3600; done

echo docker process end if you wanna exit please press enter
read ENTER
