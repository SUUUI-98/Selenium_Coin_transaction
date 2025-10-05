from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data.selectors import COIN_NAME, HOLDING_ELEMENT, HOLDING_QUANTITY, HOLDING_AMOUNT_KRW, \
    AVG_PRICE_ELEMENT, AVG_PRICE_TEXT, PROFIT_ELEMENT, PROFIT_RATIO, PROFIT_AMOUNT_KRW
import help.hold

def parse_holdings(driver: WebDriver):
    """보유 자산 목록을 파싱하여 반환합니다."""
    try:
        wait = WebDriverWait(driver, 30)
        rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.highlight.holdings tbody tr")))
    except TimeoutException:
        print("보유 자산 테이블 로딩 시간 초과")
        return []

    results = []
    for i, row in enumerate(rows, start=1):
        try:
           # 코인명은 th 태그
           coin_name = row.find_element(*COIN_NAME).text

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

           # 숫자형 파싱
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
            "profit_kwr": profit_kwr,
            "profit": profit
            })


        except Exception as e:
            print(f"row {i}  , 파싱 에러 발생 ", e)
            driver.quit()



    return results
