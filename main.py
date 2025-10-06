from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
from module import login_manager, asset_parser, my_rows_parser
from module.buy_manager import buy


def main():
    # 접속할 웹 도메인 주소
    url = "https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC&utm_source=google&utm_medium=SA&utm_campaign=up_all&utm_group=%EB%B8%8C%EB%9E%9C%EB%93%9C_%EC%BD%94%EC%9D%B8%EB%AA%85&utm_term=%EC%97%85%EB%B9%84%ED%8A%B8%EB%B9%84%ED%8A%B8&gad_source=1&gad_campaignid=22666379673&gbraid=0AAAAABNSEzQrGNp_xVhSjfU8myshj9dKI&gclid=CjwKCAjwlt7GBhAvEiwAKal0cqI_eR71M_1Rdy2Evs5qVoK0FY2LM712cd5K009C0x7XGcNHFqiUgxoCEboQAvD_BwE"
    # ChromeDriverManager를 사용하여 드라이버 경로를 가져와 Service 객체 생성
    service = Service(ChromeDriverManager().install())
    # Service 객체를 webdriver.Chrome의 service 인자로 전달
    driver = webdriver.Chrome(service=service)
    # 드라이버로 해당 주소를 오픈
    driver.get(url)
    # 5초 대기
    time.sleep(3)

    # 로그인이 True 가 아니라면 ?
    if not login_manager.perform_login(driver):
       # 드라이버 종료
       driver.quit()
       # 이어서 계속
       return

    holdings_data = asset_parser.parse_holdings(driver)
    if holdings_data:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"=== 보유 자산 스냅샷 ({current_time}) ===")

        for r in holdings_data:
            print(
                # 보유한 코인명과 수량 , 평가금액 , 매수 평균가 , 수익률 , 수익금액 출력
                f"{r['coin']:10} | 보유: {r['holding_raw']:20} | 평가금액 : {r['holding_krw'] :20} |매수평균가: {r['avg_price_raw']:15} | 수익률: {r['profit_raw']:10} | {r['profit_kwr']}")


    time.sleep(3)

    my_rows = my_rows_parser.parse_profit(driver)
    if my_rows:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"===  My - 내 자산 목록 스냅샷 ({current_time}) ===")

        for m in my_rows:
            print(
                f"| 보유 KRW :{m['assets_krw_value']:10,.0f} KRW \n"
                f"| 총 보유자산 :{m['total_assets_krw']:10,.0f} KRW \n"
                f"| 총 매수 :{m['total_purchases_krw']:10,.0f} KRW \n"
                f"| 총 평가손익 :{m['total_profit']:10,.0f} KRW \n"
                f"| 총 평가 :{m['evaluation_balance']:10,.0f} KRW \n"
                f"| 총평가수익률 :{m['total_profit_rate']:10.2f}% \n"  # % 기호는 뒤에 붙여야 함
                f"| 주문가능 :{m['total_evaluation_balance']:10,.0f} KRW"
            )
    buy(driver)
    time.sleep(3)
    driver.quit()
    #드라이버 종료
    driver.quit()

# 스크립트 실행 진입
if __name__ == "__main__":
    main()  # 함수 실행
