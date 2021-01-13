import datetime
import time
import requests
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

class CsvDownloader:

    def __init__(self):
        self.FIRE_NAME = "fireAgency.zip"
        self.FIRE_URL = "https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId=FILE_000000001491645&fileDetailSn=1&dataNm=%EC%86%8C%EB%B0%A9%EC%B2%AD_%EC%A0%84%EA%B5%AD%20%EC%86%8C%EB%B0%A9%EC%84%9C%20%EB%B0%8F%20119%EC%95%88%EC%A0%84%EC%84%BC%ED%84%B0%20%EC%A0%95%EB%B3%B4(2018.11.28)"

        self.POLICE_NAME = "policeAgency.csv"
        self.POLICE_URL = "https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId=FILE_000000002303113&fileDetailSn=1&dataNm=%EA%B2%BD%EC%B0%B0%EC%B2%AD_%EA%B2%BD%EC%B0%B0%EA%B4%80%EC%84%9C%20%EC%9C%84%EC%B9%98,%20%EC%A3%BC%EC%86%8C_20200409"

        self.CCTV_URL ="https://www.localdata.go.kr/lif/etcDataDownload.do?sigunguCodeEx=&opnSvcIdEx=12_04_01_E&startDateEx=&endDateEx=&fileType=xlsx&opnSvcNmEx=%25EA%25B3%25B5%25EC%25A4%2591%25ED%2599%2594%25EC%259E%25A5%25EC%258B%25A4%25EC%25A0%2595%25EB%25B3%25B4"

        self.BALL_NAME = "ball.csv"
        self.BALL_URL = "https://www.data.go.kr/tcs/dss/stdFileDown.do"
        self.BALL_DATA = {"publicDataPk": 15028206,
                 "publicDataSj": "전국안전비상벨위치표준데이터",
                 "file": "csv"}

        self.WEATHER_URL = "https://data.kma.go.kr/download/fileDownload.do"
        self.WEATHER_NAME = "weather.csv"

        today = datetime.datetime.today()
        yesterday = today - datetime.timedelta(days=1)
        str_yesterday = yesterday.strftime("%Y%m%d")
        start_date = str_yesterday
        end_date = str_yesterday

        self.DIR_PATH = "../download/"\
                        +today.strftime("%Y")+"/"\
                        +today.strftime("%m")+"/"\
                        +today.strftime("%d")+"/"
        createFolder(self.DIR_PATH)

        self.WEATHER_START_URL = "https://data.kma.go.kr/data/common/downloadDataCVS.do"
        "fileType=csv" \
        "&cmmnCdList=F00501%2CF00502%2CF00503%2CF00512%2CF00513" \
        "&upperCmmnCode=F005" \
        "&lrgClssCd=SFC" \
        "&mddlClssCd=SFC01" \
        "&menuNo=32" \
        "&pageIndex=1" \
        "&stnIds=154_116%2C154_108&serviceSe=F00102&elementCds=SFC01001001%2CSFC01002001" \
        "&elementGroupSns=339%2C91&dwldSetupPd=0&firstLoading=N&pageRowCount=24&validateGbn=" \
        "&dataReqstSn=&dataReqstFileSn=&startYear=&endYear=&elementGroupSn=" \
        "&schTotalCnt=10&mngRprtNo=&ctlgNo=&pgmNo=36&stnTreeId=ztree_3_check%2Cztree_4_check" \
        "&elementTreeId=ztree1_12_check%2Cztree1_15_check&mapTreeId=&dataFormCd=F00502" \
        "&startDt=" + start_date + "&startHh=00&endDt=" + end_date + "&endHh=23&startDt=&startMt=01" \
                                                                     "&endDt=&endMt=01&txtStnNm=%EA%B4%80%EC%95%85%EC%82%B0%2C%EC%84%9C%EC%9A%B8&txtElementNm=%EA%B8%B0%EC%98%A8%2C%EA%B0%95%EC%88%98%EB%9F%89&isSample=Y"
        self.WEATHER_START_DATA = {"fileType": "csv",
                      "cmmnCdList": "F00501,F00502,F00503,F00512,F00513",
                      "upperCmmnCode": "F005",
                      "lrgClssCd": "SFC",
                      "mddlClssCd": "SFC01",
                      "menuNo": "32",
                      "pageIndex": "1",
                      "stnIds": "154_116,154_108,155_159,156_143,156_176,157_201,157_102,157_112,158_156,159_133,160_152,161_98,161_119,161_202,161_203,161_99,162_105,162_100,162_106,162_104,162_93,162_214,162_90,162_121,162_114,162_211,162_217,162_95,162_101,162_216,162_212,163_226,163_221,163_131,163_135,163_127,164_238,164_235,164_236,164_129,164_232,164_177,165_172,165_251,165_140,165_247,165_243,165_254,165_244,165_248,165_146,165_245,166_259,166_262,166_266,166_165,166_164,166_258,166_174,166_168,166_252,166_170,166_260,166_256,166_175,166_268,166_261,166_169,167_283,167_279,167_273,167_271,167_137,167_136,167_277,167_272,167_281,167_115,167_130,167_278,167_276,167_138,168_294,168_284,168_253,168_295,168_288,168_255,168_289,168_257,168_263,168_192,168_155,168_162,168_264,168_285,169_185,169_189,169_187,169_188,169_265,169_184,1312_239",
                      "serviceSe": "F00102",
                      "elementCds": "SFC01001001,SFC01002001,SFC01003001,SFC01004001",
                      "elementGroupSns": "339,91,92,93",
                      "dwldSetupPd": "0",
                      "firstLoading": "N",
                      "pageRowCount": "24",
                      "dataReqstSn": "6299246",
                      "schTotalCnt": "10",
                      "pgmNo": "36",
                      "stnTreeId": "ztree_3_check,ztree_4_check,ztree_6_check,ztree_8_check,ztree_9_check,ztree_11_check,ztree_12_check,ztree_13_check,ztree_15_check,ztree_17_check,ztree_19_check,ztree_21_check,ztree_22_check,ztree_23_check,ztree_24_check,ztree_25_check,ztree_27_check,ztree_28_check,ztree_29_check,ztree_30_check,ztree_31_check,ztree_32_check,ztree_33_check,ztree_34_check,ztree_35_check,ztree_36_check,ztree_37_check,ztree_38_check,ztree_39_check,ztree_40_check,ztree_41_check,ztree_43_check,ztree_44_check,ztree_45_check,ztree_46_check,ztree_47_check,ztree_49_check,ztree_50_check,ztree_51_check,ztree_52_check,ztree_53_check,ztree_54_check,ztree_56_check,ztree_57_check,ztree_58_check,ztree_59_check,ztree_60_check,ztree_61_check,ztree_62_check,ztree_63_check,ztree_64_check,ztree_65_check,ztree_67_check,ztree_68_check,ztree_69_check,ztree_70_check,ztree_71_check,ztree_72_check,ztree_73_check,ztree_74_check,ztree_75_check,ztree_76_check,ztree_77_check,ztree_78_check,ztree_79_check,ztree_80_check,ztree_81_check,ztree_82_check,ztree_84_check,ztree_85_check,ztree_86_check,ztree_87_check,ztree_88_check,ztree_89_check,ztree_90_check,ztree_91_check,ztree_92_check,ztree_93_check,ztree_94_check,ztree_95_check,ztree_96_check,ztree_97_check,ztree_99_check,ztree_100_check,ztree_101_check,ztree_102_check,ztree_103_check,ztree_104_check,ztree_105_check,ztree_106_check,ztree_107_check,ztree_108_check,ztree_109_check,ztree_110_check,ztree_111_check,ztree_112_check,ztree_114_check,ztree_115_check,ztree_116_check,ztree_117_check,ztree_118_check,ztree_119_check,ztree_121_check",
                      "elementTreeId": "ztree1_12_check,ztree1_15_check,ztree1_18_check,ztree1_23_check",
                      "dataFormCd": "F00502",
                      "startDt": start_date,
                      "startHh": "00",
                      "endDt": end_date,
                      "endHh": "23",
                      "startMt": "01",
                      "endMt": "01",
                      "txtStnNm": "관악산,서울,부산,대구,대구(기),강화,백령도,인천,광주,대전,울산,동두천,수원,양평,이천,파주,강릉,대관령,동해,북강릉,북춘천,삼척,속초,영월,원주,인제,정선군,철원,춘천,태백,홍천,보은,제천,청주,추풍령,충주,금산,보령,부여,서산,천안,홍성,고창,고창군,군산,남원,부안,순창군,임실,장수,전주,정읍,강진군,고흥,광양시,목포,무안,보성군,순천,여수,영광군,완도,장흥,주암,진도(첨찰산),진도군,해남,흑산도,경주시,구미,문경,봉화,상주,안동,영덕,영주,영천,울릉도,울진,의성,청송군,포항,거제,거창,김해시,남해,밀양,북창원,산청,양산시,의령군,진주,창원,통영,함양군,합천,고산,서귀포,성산,성산,성산포,제주,세종",
                      "txtElementNm": "기온,강수량,풍속,습도"}
        self.LOCAL_CODE_EXS = [{"value": "6110000", "sido": "서울특별시"},
                               {"value": "6260000", "sido": "부산광역시"},
                               {"value": "6270000", "sido": "대구광역시"},
                               {"value": "6280000", "sido": "인천광역시"},
                               {"value": "6290000", "sido": "광주광역시"},
                               {"value": "6300000", "sido": "대전광역시"},
                               {"value": "6310000", "sido": "울산광역시"},
                               {"value": "5690000", "sido": "세종특별자치시"},
                               {"value": "6410000", "sido": "경기도"},
                               {"value": "6420000", "sido": "강원도"},
                               {"value": "6430000", "sido": "충청북도"},
                               {"value": "6440000", "sido": "충청남도"},
                               {"value": "6450000", "sido": "전라북도"},
                               {"value": "6460000", "sido": "전라남도"},
                               {"value": "6470000", "sido": "경상북도"},
                               {"value": "6480000", "sido": "경상남도"},
                               {"value": "6500000", "sido": "제주특별자치도"}]



    def get_response_content_decode(self, url, data=None):
        response = requests.request(method="GET", url=url, data=data)
        print(response.content)
        decode_url = response.content.decode("utf-8")
        return decode_url

    def download(self, url, file_name, data=None, option=None):
        file_path = self.DIR_PATH + file_name
        if option and data:
            if "headers" in option:
                response = requests.request(method="POST", url=url, data=data, headers=option['headers'])
            else:
                response = requests.request(method="POST", url=url, data=data)
        else:
            response = requests.request(method="GET", url=url)
        csv_content = response.content
        csv_file = open(file_path, "wb")
        csv_file.write(csv_content)
        csv_file.close()

if __name__ == "__main__":
    stime = time.time()  # 시작시간
    csv_downloader = CsvDownloader()

    # HINT: 소방청 완료 파일이름 .zip GET
    csv_downloader.download(url=csv_downloader.FIRE_URL,
                            file_name=csv_downloader.FIRE_NAME)
    # HINT: 경찰청 완료 파일이름 .csv GET
    csv_downloader.download(url=csv_downloader.POLICE_URL,
                            file_name=csv_downloader.POLICE_NAME)
    # HINT: CCTV 파일이름 .csv GET 시도별
    for localCodeEx in csv_downloader.LOCAL_CODE_EXS:
        # 추후 날짜 변경해야함
        csv_downloader.download(url=csv_downloader.CCTV_URL + "&localCodeEx=" + localCodeEx['value'] + "&sidoCodeEx=" + localCodeEx['value'],
                                file_name="cctv_"+localCodeEx['sido']+".xlsx")

    # HINT: 비상벨 파일이름 .csv POST
    csv_downloader.download(url=csv_downloader.BALL_URL,
                            file_name=csv_downloader.BALL_NAME,
                            data=csv_downloader.BALL_DATA,
                            option={"method": "POST"})
    # HINT: 날씨 파일이름 .csv POST
    file_url = csv_downloader.get_response_content_decode(url=csv_downloader.WEATHER_START_URL, data=csv_downloader.WEATHER_START_DATA)
    data = {"file": file_url}
    csv_downloader.download(url=csv_downloader.WEATHER_URL, file_name=csv_downloader.WEATHER_NAME, data=data, option={
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    })

    etime = time.time()  # 종료시간
    duration_time = str(datetime.timedelta(seconds=etime - stime))
    print(duration_time)
