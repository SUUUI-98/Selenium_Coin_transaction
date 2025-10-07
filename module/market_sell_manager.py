
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from data.selectors import SELL_TAB, MARKET_BUY, AVAILABLE_ORDER, AVAILABLE_ORDER_COIN_NAME, AVAILABLE_ORDER_KRW, \
    ORDER_100_SELECT, SELL_BUTTON, PRICE_INPUT_FIELD, DONE_BUTTON, HISTORY_TAB, TRADE_EXECUTION, DIM_LAYER_SELECTOR
from selenium.webdriver.support import expected_conditions as EC


def market_sell (driver:WebDriver):
    try:
        wait = WebDriverWait(driver, 30)
        # 매도 탭 클릭
        driver.find_element(*SELL_TAB).click()
        time.sleep(3)
        # 시장가 라디오 박스 선택
        wait.until(EC.element_to_be_clickable(MARKET_BUY)).click()

        try:
            # 주문 가능 수량 , 코인 , 원화 출력
            available_order = wait.until(EC.presence_of_element_located(AVAILABLE_ORDER)).text
            available_order_coin_name = wait.until(EC.presence_of_element_located(AVAILABLE_ORDER_COIN_NAME)).text
            available_order_krw= wait.until(EC.presence_of_element_located(AVAILABLE_ORDER_KRW)).text
            print(f"주문 가능 수량 : {available_order}{available_order_coin_name} \n" 
                  f"주문 가능 원화 : {available_order_krw} 확인 완료")

        except Exception as e:
            print(f" 주문 가능 코인 출력 중 에러 발생 :{e}")
        except NoSuchElementException as e:
            print(f"요소 못찾음 : {e}")


        time.sleep(3)

        # 주문 수량 100% 선택
        driver.find_element(*ORDER_100_SELECT).click()
        # 100% 선택 시 주문 가능 수량과 똑같은지 확인 하기 위해 값을 가져옴
        time.sleep(3)
        order_price_value = driver.find_element(*PRICE_INPUT_FIELD).text

        if available_order==order_price_value:
            print(f"주문 가능 수량 ({available_order})과 주문 수량 100%({order_price_value}) 값이 일치함, 시장가 매도 진행 ")

            driver.find_element(*SELL_BUTTON).click()
            print("매도 버튼 클릭 완료")

            wait.until(EC.element_to_be_clickable(DONE_BUTTON)).click()
            print("6. 시장가 매도 완료")
            time.sleep(5)
            # wait.until(EC.invisibility_of_element_located(DIM_LAYER_SELECTOR))

            wait.until(EC.element_to_be_clickable(HISTORY_TAB)).click()
            print("7. 거래내역 클릭 완료 , 거래내역으로 이동 ")

            wait.until(EC.element_to_be_clickable(TRADE_EXECUTION)).click()
            print("8. 시장가 매수 체결 내역 확인 완료 ")
            time.sleep(5)
            return True

        else:
            print("값이 다르므로 매도 주문 종료")
            driver.quit()

    except NoSuchElementException as e:
        print(f"요소 찾기 실패 : {e}")
    except Exception as e:
        print(f"매도 버튼 에러 발생 :{e}")
