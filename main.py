from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def main():
    # 접속할 웹 도메인 주소
    url = "https://www.google.com"
    # ChromeDriverManager를 사용하여 드라이버 경로를 가져와 Service 객체 생성
    service = Service(ChromeDriverManager().install())
    # Service 객체를 webdriver.Chrome의 service 인자로 전달
    driver = webdriver.Chrome(service=service)
    # 드라이버로 해당 주소를 오픈
    driver.get(url)
    # 3초 기다리기
    time.sleep(5)
    # 드라이버 종료
    driver.quit()


# 스크립트 실행 진입
if __name__ == "__main__":
    main()  # 함수 실행
