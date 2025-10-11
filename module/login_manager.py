from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_located_to_be_selected
from selenium.webdriver.support.wait import WebDriverWait

from selector.selectors import LOGIN_BUTTON, QR_LOGIN_BUTTON, HOLDINGS_LINK, MY_BUTTON, USER_NAME, DONE_BUTTON, \
    LOGOUT_BUTTON


#로그인 버튼 -> qr 로그인
def perform_login(driver: WebDriver):

    try:
        driver.find_element(*LOGIN_BUTTON).click()
        time.sleep(3)
        # 핸드폰으로 qr 로그인 시나리오 마무리
        driver.find_element(*QR_LOGIN_BUTTON).click()
        time.sleep(15)
        # My 버튼 클릭 후
        try:
            wait = WebDriverWait(driver, 10)
            driver.find_element(*MY_BUTTON).click()
            # 로그인 한 회원의 아이디를 확인 후 출력
            username = wait.until(EC.presence_of_element_located(USER_NAME)).text
            print(f"로그인 한 유저 : {username}")

        except Exception as e:
            print(f"유저네임 찾기 실패 : {e}")
            return False
        # 보유 버튼 클릭
        driver.find_element(*HOLDINGS_LINK).click()

    except Exception as e:
        print(f"로그인 중 오류 발생: {e}")
        return False

    return True


def logout(driver: WebDriver):
    try:
        driver.find_element(*MY_BUTTON).click()
        driver.find_element(*LOGOUT_BUTTON).click()
        driver.find_element(*DONE_BUTTON).click()
    except Exception as e:
        print(f"로그 아웃 중 오류 발생 : {e}")