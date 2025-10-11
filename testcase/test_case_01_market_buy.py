from display.display import print_login_failure, print_holdings_summary, print_total_asset_report, print_trade_failure
from module import login_manager, asset_parser, my_rows_parser
from selenium.webdriver.remote.webdriver import WebDriver
import time
from module.market_buy_manager import market_buy
from module.trade_execution_parser import trade_execution_parser


def test_case_01_market_buy(driver: WebDriver):
    # 1. 로그인
    if not login_manager.perform_login(driver):
        print_login_failure(driver)
        return

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

    # 5. 거래내역 리스트 파싱 (출력은 함수 내부에서 처리)
    # TODO : 거래내역 리스트 출력 함수도 따로 모듈로 만들기
    trade_execution_parser(driver)

    # 6. My 페이지 총 자산 다시 파싱 및 출력 (매수 후 확인)
    my_asset_report_after_buy = my_rows_parser.parse_profit(driver)
    print_total_asset_report(my_asset_report_after_buy)

    time.sleep(3)
    # 7. 로그아웃 호출
    login_manager.logout(driver)
    driver.quit()