from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from data.selectors import MY_BUTTON, GET_MY_ASSET_BUTTON, GET_MY_KRW, GET_TOTAL_ROWS
import help.hold

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
                (By.CSS_SELECTOR, ".MyTrade .MyTrade__TradeState.TradeState .TradeState__section")))


    except Exception as e:
        print(f" 요소를 못찾음  ", e)
        my_rows =[]
        driver.quit()


    my_results = []

    for i, row in enumerate(my_rows, start=1):
        try:
            # 1.  '보유 KRW' 찾기
            assets_krw_value_text = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(*GET_MY_KRW)).text

            # 2. '총 보유자산' 값 찾기
            total_assets_krw_text = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(*GET_TOTAL_ROWS)).text



            assets_krw_value = help.hold.num(assets_krw_value_text)
            total_assets_krw = help.hold.num(total_assets_krw_text)

            my_results.append({"my_holding_krw": assets_krw_value,
                           "total_rows": total_assets_krw})


        except Exception as e:
            print(f"row {i}  , 파싱 에러 발생 ", e)
            return False

        return my_results

    return True
