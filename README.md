# SPSP/OPENDATA-DOWNLOADER 뉴딜사업 
---

1. 목적
    - 매일 csv, zip, xlsx 데이터 수집하여 적재
2. 사용처
    - e2on
3. 데이터
    - 경찰청 위치, 소방청 위치, CCTV 위치, 위험벨 위치, 날씨정보
4. 운영
    - LANGUAGE
        - python 3.X    
    - 주의사항
        - 데이터 적재는 download/당일연도/당일월/당일일 폴더에 쌓인다.
        - 데이터 재 다운로드시 overwrite 된다.
        - 날씨 데이터는 매일 변경된다. 전일 데이터가 축적된다.
        - 위험벨, CCTV는 주기적으로 변경이 있는 듯 하다.
        - url 변경, 파일 이름 변경으로 인한 데이터 수집 불가 이슈가 있을 수 있다. 해당 내용을 참고할 것
    - 추가 고민사항    
        - 데이터 수집이 에러가 생겼을 시 정해진 매일주소로 메일을 보내는 방법을 고민한다.
5. 수집
    1. flask_nice_queue.py 를 실행
    2. http://localhost:9000 에서 수집 요청
        - 개별 brand_cd 수집 http://localhost:9000/crawl_nice?brand_cd=${brand_cd}
        - 해당 view_way 수집 http://localhost:9000/crawl_group?view_way=${view_way}
        - 전체 brand 수집 http://localhost:9000/crawl_nice?all_scrape=yes
    3. 주의사항
        - 수집 중에는 재 수집 요청은 거부된다.  
        - active = true 인 brand만 수집된다.
        - 포탈 수집은 kakao 에서 수집되기에 수집시 차단되지 않도록 유의한다.
        - DB는 51 server와 연결 되어있다. 
        - all or view_way 수집시 하나 수집 끝나면 다음 수집이 바로 진행된다.
        

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
