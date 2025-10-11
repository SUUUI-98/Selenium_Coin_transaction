from display.display import print_login_failure, print_holdings_summary, print_total_asset_report, print_trade_failure
from module import login_manager, asset_parser, my_rows_parser
import time
from module.market_sell_manager import market_sell
from module.trade_execution_parser import trade_execution_parser


def test_case_02_market_sell(driver):
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

    # 4. DOGE 시장가 매도
    print("--- DOGE 시장가 매도 시도 ---")
    trade_sell_success = market_sell(driver)
    print_trade_failure(trade_sell_success)
    time.sleep(3)
    # 5. 거래내역 리스트 파싱 (출력은 함수 내부에서 처리 가정)
    trade_execution_parser(driver)

    # 6. 최종 종료 대기
    time.sleep(3)
    # 7. 로그아웃 호출
    login_manager.logout(driver)
    driver.quit()