# SPSP/OPENDATA-DOWNLOADER 뉴딜사업 
---

1. 목적
    - 매일 csv, zip, xlsx 데이터 수집하여 적재
2. 사용처
    - e2on
3. 데이터
    - 경찰청 위치, 소방청 위치, CCTV 위치, 비상벨 위치, 시간대별 날씨정보
4. 운영
    - LANGUAGE
        - python 3.X    
    - 주의사항
        - ~~데이터 적재는 download/당일연도/당일월/당일일 폴더에 쌓인다.~~
        - ~~데이터 재 다운로드시 overwrite 된다.~~
        - 날씨 데이터는 매일 변경된다. ~~전일 데이터가 축적된다.~~
        - 위험벨, CCTV는 주기적으로 변경이 있는 듯 하다.
        - url 변경, 파일 이름 변경으로 인한 데이터 수집 불가 이슈가 있을 수 있다. 해당 내용을 참고할 것
    - 추가 고민사항    
        - 데이터 수집이 에러가 생겼을 시 정해진 매일주소로 메일을 보내는 방법을 고민한다.

2021-01-14
Docekrfile 추가  
docker가 실행되는 곳이면 어떤 곳이라도 실행 가능  
- image 있어야만 container 생성 가능
```
    docker build  -t alkaline2018/opendata-downloader:1.0.16 .
    docker build  -t {image_name}:{version} {bulid 할 폴더/file} "." 있으니까 잊지 말길
    혹은 docker_hub 에서 pull 해서 image 를 획득한다.
```
- 실행시킬 때 image 에서 container 생성만
```
    docker create --name opendata_downloader -v C:\Users\song_e\Documents\csv_download_test\a:/app/download alkaline2018/opendata-downloader:1.0.16
    docker create --name {container_name} -v {host_path}:{docker_path} {image_name}:{version}        
```
- contianer 실행
```
    docker start opendata_downloader
    docker start {container_name}
```

    

2021-01-13       
비교 프로세스 추가
CCTV_URL 오류 화장실 -> CCTV
기존 download/연도/월/일/해당파일 -> download/해당파일 폴더 구조 변경 

opendata-downloader 프로젝트 생성 (git 반영)
 - 경찰청, 소방청, CCTV, 위험벨, 날씨데이터 매일 수집시 수집가능한 프로젝트
 - 현재 실행 X
 - 파일 생성 규칙 
     기존 파일 없으면 생성 
     기존 파일 있고 기존과 다르면 새로 생성 (기존파일 삭제)
     기존 파일 있고 기존과 같으면 변화 없음
 - 파일은 세가지 유형으로 생성됌 csv, xlsx, zip 이는 원본파일에서 제공방식유지

 
<!-- 주석 필요시 따로 사용
- [ ]  체크 X
- [x]  체크

- 점
> 인용
>> 재인용
```jsx
const name = "송"
```
```json
{"name": "송", "age": 28}
```
-->
