# main.py (수정된 코드)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
from module import login_manager, asset_parser, my_rows_parser
from module.market_buy_manager import market_buy
from module.market_sell_manager import market_sell
from module.trade_execution_parser import trade_execution_parser
from display.display import print_login_failure, print_holdings_summary, print_total_asset_report, print_trade_failure


def main():
    url = "https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC&utm_source=google&utm_medium=SA&utm_campaign=up_all&utm_group=%EB%B8%8C%EB%9E%9C%EB%93%9C_%EC%BD%94%EC%9D%B8%EB%AA%85&utm_term=%EC%97%85%EB%B9%84%ED%8A%B8%EB%B9%84%ED%8A%B8&gad_source=1&gad_campaignid=22666379673&gbraid=0AAAAABNSEzQrGNp_xVhSjfU8myshj9dKI&gclid=CjwKCAjwlt7GBhAvEiwAKal0cqI_eR71M_1Rdy2Evs5qVoK0FY2LM712cd5K009C0x7XGcNHFqiUgxoCEboQAvD_BwE"

    service = Service(ChromeDriverManager().install())

    # Context Manager 사용: main 함수 종료 시 driver.quit() 자동 실행
    with webdriver.Chrome(service=service) as driver:
        driver.get(url)
        time.sleep(3)

        # 1. 로그인
        if not login_manager.perform_login(driver):
            print_login_failure(driver)
            return  # driver.quit()은 with 블록 종료 시 자동 실행

        # 2. 거래소 화면 보유 자산 파싱 및 출력
        holdings_data = asset_parser.parse_holdings(driver)
        print_holdings_summary(holdings_data)  # display 모듈 호출
        time.sleep(3)

        # 3. My 페이지 총 자산 파싱 및 출력
        my_asset_report = my_rows_parser.parse_profit(driver)
        print_total_asset_report(my_asset_report)  # display 모듈 호출
        time.sleep(3)

        # 4. DOGE 시장가 매수
        print("--- DOGE 시장가 매수 시도 ---")
        trade_buy_success = market_buy(driver)
        print_trade_failure(trade_buy_success)

        time.sleep(3)

        # 5. 거래내역 리스트 파싱 (출력은 함수 내부에서 처리 가정)
        trade_execution_parser(driver)

        # 6. My 페이지 총 자산 다시 파싱 및 출력 (매수 후 확인)
        my_asset_report_after_buy = my_rows_parser.parse_profit(driver)
        print_total_asset_report(my_asset_report_after_buy)

        # 7. DOGE 시장가 매도
        print("--- DOGE 시장가 매도 시도 ---")
        trade_sell_success = market_sell(driver)
        print_trade_failure(trade_sell_success)

        time.sleep(3)
        # 8. 거래내역 리스트 파싱 (출력은 함수 내부에서 처리 가정)
        trade_execution_parser(driver)

        # 9. 최종 종료 대기
        time.sleep(3)



# 스크립트 실행 진입
if __name__ == "__main__":
    main()