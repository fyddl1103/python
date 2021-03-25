# 5.3 주식 시세를 매일 DB로 업데이트 하기
# KRX에서 전체 종목 리스트 조회 > 네이버 금융의 주식 시세를 뷰티풀수프와 팬더스로 읽어옴 > mariaDB에 매일 자동으로 업데이트
import pymysql
import pandas as pd
from datetime import datetime
import BeautifulSoup


class DBUpdater:
    def __init__(self):
        """
        생성자 ; MariaDB 연결 및 종목코드 딕셔너리 생성
        """
        self.conn = pymysql.connect(
            host='localhost', user='root', password='1234', db='INVESTAR', charset='utf8')

        with self.conn.cursor() as curs:
            sql = """
                CREATE TABLE IF NOT EXISTS `company_info` (
                    `code` VARCHAR(20) NOT NULL COLLATE 'utf8_general_ci',
                    `company` VARCHAR(40) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
                    `last_update` DATE NULL DEFAULT NULL,
                    PRIMARY KEY (`code`))
            """
            curs.execute(sql)
            sql = """
                CREATE TABLE IF NOT EXISTS `daily_price` (
                        `code` VARCHAR(20) NOT NULL COLLATE 'utf8_general_ci',
                        `date` DATE NOT NULL,
                        `open` BIGINT(20) NULL DEFAULT NULL,
                        `high` BIGINT(20) NULL DEFAULT NULL,
                        `low` BIGINT(20) NULL DEFAULT NULL,
                        `close` BIGINT(20) NULL DEFAULT NULL,
                        `diff` BIGINT(20) NULL DEFAULT NULL,
                        `volume` BIGINT(20) NULL DEFAULT NULL,
                        PRIMARY KEY (`code`, `date`) )
            """
            curs.execute(sql)
        self.conn.commit()

        self.codes = dict()
        self.update_comp_info()

    def __del__(self):
        """
        소멸자 ; MariaDB 연결 해제
        """
        self.conn.close()

    def read_krx_code(self):
        """
        KRX로부터 상장법인목록 파일 읽어와서 데이터프레임으로 변환
        """
        url = 'https://kind.krx.co.kr/corpgeneral/corpList.do?method='\
            'download&searchType=13'
        krx = pd.read_html(url, header=0)[0]  # 데이터프레임으로 반환
        krx = krx[['종목코드', '회사명']]  # df에서 특정컬럼만 추출
        krx = krx.rename(columns={'종목코드': 'code', '회사명': 'company'})
        krx.code = krx.code.map('{:06d}'.format)  # 종목코드 000000 6자리로 출력
        krx = krx.sort_values(by='code', ascending=True)
        return krx

    def update_comp_info(self):
        """
        종목코드를 company_info table에 업데이트. > 딕셔너리에 저장 
        """
        sql = "SELECT * FROM company_info"
        df = pd.read_sql(sql, self.conn)
        for idx in range(len(df)):
            # 종목코드와 회사명으로 codes 딕셔너리 만듦
            self.codes[df['code'].values[idx]] = df['company'].values[idx]

        with self.conn.cursor() as curs:
            sql = "SELECT MAX(last_update) FROM company_info"
            curs.execute(sql)
            rs = curs.fetchone()
            today = datetime.today().strftime('%Y-%m-%d')

            if rs[0] == None or rs[0].strftime('%Y-%m-%d') < today:
                krx = self.read_krx_code()
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]
                    sql = f"REPLACE INTO company_info (code, company, last_update)"\
                          f"VALUES ('{code}', '{company}', '{today}')"
                    curs.execute(sql)
                    # codes 딕셔너리에 code : company 형태로 추가
                    self.codes[code] = company
                    tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                    print(f"[{tmnow}] {idx:04d} REPLACE INTO company_info "
                          f"VALUES ({code}, {company}, {today})")
                self.conn.commit()

    def read_naver(self, code, company, pages_to_fetch):
        """
        네이버 금융에서 주식 시세를 읽어서 데이터프레임으로 변환
        """
        try:
            url = f"http://finance.naver.com/item/sise_day.nhn?code={code}"
            with urlopen(url) as doc:
                if doc is None:
                    return None
                html = BeautifulSoup(doc, 'lxml')
                pgrr = html.find("td", class_="pgRR")
                if pgrr is None:
                    return None
                s = str(pgrr.a["href"]).split('=')
                lastpage = s[-1]
            df = pd.DataFrame()
            pages = min(int(lastpage), pages_to_fetch)
            for page in range(1, pages + 1):
                pg_url = '{}&page={}'.format(url, page)
                df = df.append(pd.read_html(pg_url, header=0)[0])
                tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                print('[{}] {} ({}) : {:04d}/{:04d} pages are downloading....'.
                      format(tmnow, company, code, page, pages), end="\r")
            df = df.rename(columns={'날짜': 'date', '종가': 'close', '전일비': 'diff',
                                    '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})
            df['date'] = df['date'].replace('.', '-')
            df = df.dropna()
            df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[[
                'close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)  # BIGINT > int형으로 변경
            df = df[['close', 'diff', 'open', 'high', 'low', 'volume']]

        except Exception as e:
            print('Exception occured : ', str(e))
            return None
        return df

    def replace_into_db(self, df, num, code, company):
        """
        네이버 금융에서 읽어온 주식 시세를 DB에 REPLACE
        """

    def update_daily_price(self, pages_to_fetch):
        """
        KRX 상장법인의 주식 시세를 네이버로부터 읽어서 DB에 업데이트
        """

    def execute_daily(self):
        """
        실행 즉시 및 매일 오후 다섯시에 daily_price 테이블 업데이트
        """


if __name__ == '__main__':
    dbu = DBUpdater()
    # dbu.execute_daily()
    dbu.update_comp_info()
