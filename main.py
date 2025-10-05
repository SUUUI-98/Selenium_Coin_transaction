from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time
from selenium.webdriver.support import expected_conditions as EC
import help.hold
from datetime import datetime

from data.selectors import *


def main():
    # 접속할 웹 도메인 주소
    url = "https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC&utm_source=google&utm_medium=SA&utm_campaign=up_all&utm_group=%EB%B8%8C%EB%9E%9C%EB%93%9C_%EC%BD%94%EC%9D%B8%EB%AA%85&utm_term=%EC%97%85%EB%B9%84%ED%8A%B8%EB%B9%84%ED%8A%B8&gad_source=1&gad_campaignid=22666379673&gbraid=0AAAAABNSEzQrGNp_xVhSjfU8myshj9dKI&gclid=CjwKCAjwlt7GBhAvEiwAKal0cqI_eR71M_1Rdy2Evs5qVoK0FY2LM712cd5K009C0x7XGcNHFqiUgxoCEboQAvD_BwE"
    # ChromeDriverManager를 사용하여 드라이버 경로를 가져와 Service 객체 생성
    service = Service(ChromeDriverManager().install())
    # Service 객체를 webdriver.Chrome의 service 인자로 전달
    driver = webdriver.Chrome(service=service)
    # 드라이버로 해당 주소를 오픈
    driver.get(url)
    # 5초 대기
    time.sleep(5)

    try:
        # 로그인 버튼
        driver.find_element(*LOGIN_BUTTON).click()
        time.sleep(3)

        # qr 로그인
        driver.find_element(*QR_LOGIN_BUTTON).click()
        time.sleep(15)
        # 핸드폰으로 로그인 시나리오 마무리

        # a 태그로 감싸진 요소중 텍스트가 '보유' 인 요소 선택
        driver.find_element(*HOLDINGS_LINK).click()

        wait = WebDriverWait(driver, 30)

        # highlight와 holdings 클래스를 가진 table을 찾음
        # 테이블의 자식인 tbody 를 찾음
        # tbody 의 자식 요소인 tr 들을 찾음
        rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.highlight.holdings tbody tr")))

    except TimeoutException:
        print("로딩 시간 초과 ")
        rows = []

    results = []
    for i, row in enumerate(rows, start=1):
        try:
            # 코인명은 th 태그
            coin_name= row.find_element(*COIN_NAME).text

            # 보유수량/평가 금액 (첫 번째 td의 자식 요소 )
            holding_elem = row.find_element(*HOLDING_ELEMENT)

            # 보유수량은 이 td의 자식인 strong 태그
            holding_strong_elems = holding_elem.find_elements(*HOLDING_QUANTITY)
            holding_text = holding_strong_elems[0].text

            # 평가 금액은 이 td의 자식인 em 태그
            holding_em_elems = holding_elem.find_elements(*HOLDING_AMOUNT_KRW)
            if holding_em_elems:
                holding_krw = holding_em_elems[0].text
            else:
                holding_krw = "N/A"


            # 매수평균가 (두 번째 td)
            avg_price_elem = row.find_element(*AVG_PRICE_ELEMENT)
            if avg_price_elem:
                avg_price_text = avg_price_elem.find_element(*AVG_PRICE_TEXT).text
            else:
                avg_price_text = "N/A"

            # 수익률 (세 번째 td)
            # 보유 코인 중 평가금액과 평균가가 없는 코인도 있기 때문에
            # 요소를 못찾는 예외가 아닌 n/a 를 반환하기 위함

            # 3번째 td(수익률)  의 요소를 모두 가져옴
            profit_elem_list = row.find_elements(*PROFIT_ELEMENT)

            if profit_elem_list:
                # 세 번째 td가 존재하면 리스트의 첫 번째 요소를 가져옴
                profit_elem = profit_elem_list[0]
                # profit_elem 안에서 각각의 자식 요소(.PriceRate--Ratio(수익률), .PriceRate--Measure(수익금액))가 있는지 확인
                profit_ratio_list = profit_elem.find_elements(*PROFIT_RATIO)
                if profit_ratio_list:
                    profit_text = profit_ratio_list[0].text
                else:
                    profit_text = "N/A"

                profit_kwr_list = profit_elem.find_elements(*PROFIT_AMOUNT_KRW)
                if profit_kwr_list:
                    profit_kwr = profit_kwr_list[0].text
                else:
                    profit_kwr = "N/A"
            else:
                # 세 번째 td 자체가 존재하지 않으면 모든 값을 "N/A"로 설정
                profit_text = "N/A"
                profit_kwr = "N/A"

            #숫자형 파싱
            holding_value = help.hold.num(holding_text)
            avg_price = help.hold.num(avg_price_text)
            profit = help.hold.num(profit_text)

            results.append({
                "coin": coin_name,
                "holding_raw": holding_text,
                "holding_krw": holding_krw,
                "holding_value": holding_value,
                "avg_price_raw": avg_price_text,
                "avg_price": avg_price,
                "profit_raw": profit_text,
                "profit_kwr" : profit_kwr,
                "profit": profit
            })


        except Exception as e:
            print(f"row {i}  , 파싱 에러 발생 ", e)


        # 현재시간
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"=== 보유 자산 스냅샷 ({current_time}) ===")

        for r in results:
            print(
                # 보유한 코인명과 수량 , 평가금액 , 매수 평균가 , 수익률 , 수익금액 출력
                f"{r['coin']:10} | 보유: {r['holding_raw']:20} | 평가금액 : {r['holding_krw'] :20} |매수평균가: {r['avg_price_raw']:15} | 수익률: {r['profit_raw']:10} | {r['profit_kwr']}")



# 스크립트 실행 진입
if __name__ == "__main__":
    main()  # 함수 실행
