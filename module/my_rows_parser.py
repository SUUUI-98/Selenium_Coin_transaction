from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from data.selectors import MY_BUTTON, GET_MY_ASSET_BUTTON, GET_MY_KRW, HOLDING_ELEMENT


def parse_profit(driver: WebDriver):
    # My 버튼 클릭
    try :
        driver.find_element(*MY_BUTTON).click()
        time.sleep(3)

        # 내 자산 보기 버튼 클릭
        driver.find_element(*GET_MY_ASSET_BUTTON).click()
        time.sleep(3)

        wait = WebDriverWait(driver, 30)
        my_rows = wait.until(
                EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "MyTrade.MyTrade__TradeState TradeState.TradeState__section")))


    except Exception as e:
        print(f" 요소를 못찾음  ", e)
        my_rows =[]
        driver.quit()


    my_results = []
    for i, row in enumerate(my_rows, start=1):
        try:
            # 코인명은 th 태그
            my_holding_krw = row.find_element(*GET_MY_KRW).text

            # 보유수량/평가 금액 (첫 번째 td의 자식 요소 )
            total_rows = row.find_element(*HOLDING_ELEMENT)

            my_results.append({"my_holding_krw": my_holding_krw,
                           "total_rows": total_rows})

            return bool

        except Exception as e:
            print(f"row {i}  , 파싱 에러 발생 ", e)
            return False

    return my_results


