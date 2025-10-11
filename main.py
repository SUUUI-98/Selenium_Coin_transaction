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
from testcase.test_case_01_market_buy import test_case_01_market_buy


def main():
    url = "https://upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC&utm_source=google&utm_medium=SA&utm_campaign=up_all&utm_group=%EB%B8%8C%EB%9E%9C%EB%93%9C_%EC%BD%94%EC%9D%B8%EB%AA%85&utm_term=%EC%97%85%EB%B9%84%ED%8A%B8%EB%B9%84%ED%8A%B8&gad_source=1&gad_campaignid=22666379673&gbraid=0AAAAABNSEzQrGNp_xVhSjfU8myshj9dKI&gclid=CjwKCAjwlt7GBhAvEiwAKal0cqI_eR71M_1Rdy2Evs5qVoK0FY2LM712cd5K009C0x7XGcNHFqiUgxoCEboQAvD_BwE"

    service = Service(ChromeDriverManager().install())

    with webdriver.Chrome(service=service) as driver:
        driver.get(url)
        time.sleep(3)

        # test_case_01 시장가매수
        test_case_01_market_buy(driver)


# 스크립트 실행 진입
if __name__ == "__main__":
    main()