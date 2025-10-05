from selenium.webdriver.remote.webdriver import WebDriver
import time
from data.selectors import LOGIN_BUTTON, QR_LOGIN_BUTTON, HOLDINGS_LINK


#로그인 버튼 -> qr 로그인
def perform_login(driver: WebDriver):

    try:
        driver.find_element(*LOGIN_BUTTON).click()
        time.sleep(3)
        driver.find_element(*QR_LOGIN_BUTTON).click()
        time.sleep(15)
        # 핸드폰으로 로그인 시나리오 마무리
        driver.find_element(*HOLDINGS_LINK).click()
    except Exception as e:
        print(f"로그인 중 오류 발생: {e}")
        return False

    return True