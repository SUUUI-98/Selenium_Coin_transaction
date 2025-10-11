from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from data.selectors import SELL_TAB, MARKET_BUY, AVAILABLE_ORDER, AVAILABLE_ORDER_COIN_NAME, AVAILABLE_ORDER_KRW, \
    ORDER_100_SELECT, SELL_BUTTON, DONE_BUTTON, HISTORY_TAB, TRADE_EXECUTION, DIM_LAYER_SELECTOR, \
    SELL_PRICE_INPUT_FIELD, EXCHANGE_TAB, DOGE_COIN
from selenium.webdriver.support import expected_conditions as EC


def market_sell(driver: WebDriver):
    wait = WebDriverWait(driver, 30)

    try:
        # 거래소 화면 이동
        driver.find_element(*EXCHANGE_TAB).click()
        time.sleep(3)
        # 도지코인 거래소로 이동
        driver.find_element(*DOGE_COIN).click()
        # 매도 탭 클릭
        driver.find_element(*SELL_TAB).click()
        time.sleep(3)
        # 시장가 라디오 박스 선택
        wait.until(EC.element_to_be_clickable(MARKET_BUY)).click()

        # 주문 가능 수량, 코인, 원화 출력 및 값 저장
        available_order = wait.until(EC.presence_of_element_located(AVAILABLE_ORDER)).text
        print(f"1. 주문 가능 수량 : {available_order}")

        available_order_coin_name = wait.until(EC.presence_of_element_located(AVAILABLE_ORDER_COIN_NAME)).text
        print(f"2. 주문 가능 코인명 : {available_order_coin_name}")

        available_order_krw = wait.until(EC.presence_of_element_located(AVAILABLE_ORDER_KRW)).text
        print(f"3. 주문 가능 원화 : {available_order_krw} ")


        print(f"| 주문 가능 수량 : {available_order:5} {available_order_coin_name} \n"
              f"| 주문 가능 원화 : {available_order_krw} ")

        time.sleep(2)


        # 주문 수량 100% 선택
        driver.find_element(*ORDER_100_SELECT).click()
        print("100% 선택 완료 ")
        time.sleep(2)

        # 100% 선택 시 주문 가능 수량과 똑같은지 확인 하기 위해 값을 가져옴
        wait.until(EC.text_to_be_present_in_element_value(SELL_PRICE_INPUT_FIELD, available_order[:5]))
        print("input 값이 채워질때까지 기다리는중 .. ")

        # input 필드 값은 .get_attribute('value')로 가져옴
        order_price_value = driver.find_element(*SELL_PRICE_INPUT_FIELD).get_attribute('value')
        print(f"input 창 주문 수량 100% 출력 {order_price_value}")


        if available_order == order_price_value:
            print(f"주문 가능 수량 ({available_order})과 주문 수량 100%({order_price_value}) 값이 일치함, 시장가 매도 진행 ")

            # 매도 버튼 클릭
            driver.find_element(*SELL_BUTTON).click()
            print("매도 버튼 클릭 완료")

            # 확인 버튼 클릭
            wait.until(EC.element_to_be_clickable(DONE_BUTTON)).click()
            print("6. 시장가 매도 완료")
            # wait.until(EC.invisibility_of_element_located(DIM_LAYER_SELECTOR))

            # 거래 내역 확인
            wait.until(EC.element_to_be_clickable(HISTORY_TAB)).click()
            print("7. 거래내역 클릭 완료, 거래내역으로 이동 ")

            wait.until(EC.element_to_be_clickable(TRADE_EXECUTION)).click()
            print("8. 시장가 매도 체결 내역 확인 완료 ")
            time.sleep(5)
            return True

        else:
            print("값이 다르므로 매도 주문 종료")
            return False  # 매도가 진행되지 않았으므로 False 반환

    except NoSuchElementException as e:
        print(f"요소 찾기 실패 : {e}")
        try:
            driver.quit()
        except Exception:
            pass
        return False

    except Exception as e:
        print(f"매도 로직 실행 중 예상치 못한 에러 발생: {e}")
        driver.quit()