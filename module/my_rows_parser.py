from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from data.selectors import MY_BUTTON, GET_MY_ASSET_BUTTON, MY_KRW, TOTAL_ROWS, TOTAL_PURCHASE, TOTAL_EVALUATION, \
    AVAILABLE_BALANCE, TOTAL_PROFIT_LOSS, TOTAL_PROFIT_RATE
import help.hold


def parse_profit(driver: WebDriver):



    try:
        wait = WebDriverWait(driver, 30)
        # My 버튼 클릭
        driver.find_element(*MY_BUTTON).click()
        time.sleep(3)

        # 내 자산 보기 버튼 클릭
        driver.find_element(*GET_MY_ASSET_BUTTON).click()
        time.sleep(3)

        my_rows = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".MyTrade .MyTrade__TradeState.TradeState .TradeState__section")))


    except Exception as e:
        print(f" 요소를 못찾음  ", e)
        my_rows = []
        driver.quit()

    my_results = []

    for i, row in enumerate(my_rows, start=1):
        try:
            wait = WebDriverWait(driver, 30)
            # 1.  '보유 KRW' 찾기
            assets_krw_value_text = wait.until(EC.presence_of_element_located(MY_KRW)).text

            # 2. '총 보유자산' 값 찾기
            total_assets_krw_text = wait.until(EC.presence_of_element_located(TOTAL_ROWS)).text

            # 3. 총 매수
            total_purchases_krw_text = wait.until(EC.presence_of_element_located(TOTAL_PURCHASE)).text
            # 4. 총평가손익
            total_profit_text = wait.until(EC.presence_of_element_located(TOTAL_PROFIT_LOSS)).text

            # 5. 총 평가
            try:
                # 텍스트가 비어있지 않을 때까지 대기하고 텍스트를 받아옵니다.
                evaluation_balance = wait.until(EC.presence_of_element_located(TOTAL_EVALUATION)).text


            except TimeoutException:
                # 텍스트가 지정된 시간 내에 채워지지 않은 경우
                print(f"row {i}: '총 평가' 텍스트 로딩 시간 초과. 0으로 처리.")
                evaluation_balance = 0.0

            except Exception as e:
                # 기타 모든 예외 (예: 파싱 오류)
                print(f"row {i}: '총 평가' 처리 중 알 수 없는 에러 발생: {e}")
                evaluation_balance = 0.0

            # 6. 총평가수익률
            total_profit_rate_text = wait.until(EC.presence_of_element_located(TOTAL_PROFIT_RATE)).text
            # 7. 주문가능
            total_evaluation_balance_text = wait.until(EC.presence_of_element_located(AVAILABLE_BALANCE)).text

            # float 파싱
            assets_krw_value = help.hold.num(assets_krw_value_text)
            total_assets_krw = help.hold.num(total_assets_krw_text)
            total_purchases_krw = help.hold.num(total_purchases_krw_text)
            total_profit = help.hold.num(total_profit_text)
            total_profit_rate = help.hold.num(total_profit_rate_text)
            total_evaluation_balance = help.hold.num(total_evaluation_balance_text)

            my_results.append({"assets_krw_value" : assets_krw_value,
                               "total_assets_krw" : total_assets_krw,
                               "total_purchases_krw" : total_purchases_krw,
                               "total_profit" : total_profit,
                               "evaluation_balance" : evaluation_balance,
                               "total_profit_rate" : total_profit_rate,
                               "total_evaluation_balance" : total_evaluation_balance,
                               })


        except Exception as e:
            print(f"row {i}  , 파싱 에러 발생 ", e)
            return False

        return my_results

    return True
