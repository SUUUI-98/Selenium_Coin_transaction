import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from selector.selectors import EXCHANGE_TAB, DOGE_COIN, BUY_TAB, MARKET_BUY, PRICE_INPUT_FIELD, INPUT_VALUE, BUY_BUTTON, \
    DONE_BUTTON, HISTORY_TAB, TRADE_EXECUTION, DIM_LAYER_SELECTOR


def market_buy(driver: WebDriver):
    try:
        wait = WebDriverWait(driver, 30)
        # 거래소 화면 이동
        driver.find_element(*EXCHANGE_TAB).click()
        time.sleep(3)
        # 도지코인 거래소로 이동
        driver.find_element(*DOGE_COIN).click()

        # 매수 탭 클릭
        try:
            wait.until(EC.element_to_be_clickable(BUY_TAB)).click()
            print("1. 매수 탭 클릭 성공")

        except NoSuchElementException:
            print("요소 찾기 실패 ")
        except Exception as e:
            print(f"매수 버튼 에러 발생 :{e}")

        time.sleep(2)
        # 시장가 매수 선택
        wait.until(EC.element_to_be_clickable(MARKET_BUY)).click()
        print("2. 시장가 선택 성공 ")

        # 금액을 입력할 input 창 선택
        price_input: WebElement = wait.until(
            EC.element_to_be_clickable(PRICE_INPUT_FIELD))

        # 입력 필드 초기화
        price_input.clear()
        print("3. 입력 필드 선택 성공 ")
        # 4.매수 금액 5500 입력
        price_input.send_keys(INPUT_VALUE)
        print(f" 4. 입력 필드에 값 '{INPUT_VALUE}'을(를) 성공적으로 입력")

        driver.find_element(*BUY_BUTTON).click()
        print("5. 매수 버튼 클릭 완료 ")

        # 팝업창의 확인 버튼 클릭
        wait.until(EC.element_to_be_clickable(DONE_BUTTON)).click()
        print("6. 시장가 매수 완료")

        # time.sleep(3)
        # 레이어가 사라질때까지 대기
        # wait.until(EC.invisibility_of_element_located(DIM_LAYER_SELECTOR))
        # print("딤레이어 사라짐 이동 준비 ")

        wait.until(EC.element_to_be_clickable(HISTORY_TAB)).click()
        print("7. 거래내역 클릭 완료 , 거래내역으로 이동 ")

        wait.until(EC.element_to_be_clickable(TRADE_EXECUTION)).click()
        print("8. 시장가 매수 체결 내역 확인 완료 ")
        time.sleep(5)
        return True

    except NoSuchElementException as e:
        print(f" 요소찾기 실패  :{e}")
        return False
    except Exception as e:
        print(f"매수 작업 중 에러 발생 :{e}")
        return False
    except TimeoutException:
        print("로딩 시간 초과 ")
        return False